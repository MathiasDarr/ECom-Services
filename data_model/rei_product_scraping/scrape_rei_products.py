"""
This script scrapes REI.com for products & inserts


"""
# !/usr/bin/env python3

import boto3
import requests
from bs4 import BeautifulSoup
import re
import csv


def get_product_detail(url, category):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_soup = soup.find("div", {"id": "product-container"})

    colors = parse_colors(product_soup)
    price = parse_price(product_soup)

    vendor = product_soup.find('input', {'name': 'vendor'})['value']

    product_name = product_soup.find('input', {'name': 'product_desc'})['value']
    parsed_name = product_name.split(' - ')[0]
    parsed_name = parsed_name.replace(vendor, '').lstrip()
    if len(colors) == 0:
        colors = None
    product = {'name': str(parsed_name), 'vendor': str(vendor), 'colors': colors, 'price': price, 'url': url,
               'category': category}

    return product


def parse_price(product_soup):
    """
    This function parses the price from the product detail HTML
    :param product_soup:
    :return:
    """
    pscript = product_soup.find('script')
    ptext = str(pscript)
    price_iterator = re.finditer('"price":[0-9]+.[0-9]+', ptext)
    first_price = next(price_iterator)
    price_string = ptext[first_price.start():first_price.end()]
    price = price_string.split(':')[1]
    return price


def parse_colors(product_soup):
    """
    This function parses the colors from the product detail HTML
    :param product_soup:
    :return:
    """
    script_tag = product_soup.find('script')
    script_text = str(script_tag)
    color_iterator = re.finditer('"displayName":"[a-zA-Z]+"', script_text)

    colors = set()

    sizes = {'S', 'M', 'XL', 'XXL', 'XXXL', 'L', 'XS'}

    while True:
        try:
            next_color = next(color_iterator)
            color_match = script_text[next_color.start():next_color.end()]
            color = color_match.split(':')[1].replace('"', '')
            if color not in sizes:
                colors.add(color)
        except Exception as e:
            break

    return list(colors)


def get_products(category):
    """
    This function takes a category i.e 'mens-casual-jackets' (as found on the rei.com website) & returns a list of
    product urls :param category: :return: list of product urls
    """
    pagenumber = 1
    url = 'https://www.rei.com/c/{}'.format(category)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    navclass = soup.find("nav", {"class": "_3-4shQxwfGRyzNItrZFEiC"})
    npages = len(navclass.find_all('a', href=True))

    products = set()
    while pagenumber <= npages:
        url = 'https://www.rei.com/c/{}?page={}'.format(category, pagenumber)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        search_results = soup.find('div', {'id': 'search-results'})
        for a in search_results.find_all('a', href=True):
            products.add(a['href'])
            # print("Found the URL:", a['href'])
        pagenumber += 1

    return ['https://www.rei.com' + str(product) for product in products if str(product).find('rei-garage') < 0]


def insert_product(product):
    """
    Insert a product into dynamodb.
    :param product: Product dictionary
    :return:
    """
    return table.put_item(
        Item={
            'vendor': product['name'],
            'productName': product['name'],
            'colors': product['colors'],
            'price': product['price']
        }
    )


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
table = dynamodb.Table('Products')

categories = ['mens-casual-jackets', 'mens-boots', 'mens-insulated-jackets', 'mens-fleece-and-soft-shell-jackets',
              'mens-rain-jackets',
              'mens-running-jackets', 'mens-wind-shells', 'mens-snow-jackets', 'mens-winter-boots',
              'backpacking-packs', 'day-packs', 'womens-boots', 'womens-casual-jackets', 'womens-insulated-jackets',
              'womens-fleece-and-soft-shell-jackets', 'womens-rain-jackets', 'womens-running-jackets']
windshells = 'mens-wind-shells'
categories  = ['mens-snow-jackets', 'mens-winter-boots',
              'backpacking-packs', 'day-packs', 'womens-boots', 'womens-casual-jackets', 'womens-insulated-jackets',
              'womens-fleece-and-soft-shell-jackets', 'womens-rain-jackets', 'womens-running-jackets']
products = get_products(categories[0])

all_products = []

for category in categories:
    products = get_products(category)
    parsed_products = []
    for i, product_url in enumerate(products):
        print(i)
        try:
            parsed_products.append(get_product_detail(product_url, category))
        except Exception as e:
            print(e)
    keys = ['name', 'vendor', 'colors','price', 'url', 'category']
    with open('data_model/rei_product_scraping/data/{}.csv'.format(category), 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(parsed_products)

