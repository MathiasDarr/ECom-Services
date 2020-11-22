import requests
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver


def get_product_detail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_soup = soup.find("div", {"id": "product-container"})

    colors = parse_colors(product_soup)
    price = parse_price(product_soup)

    vendor = product_soup.find('input', {'name': 'vendor'})['value']

    product_name = product_soup.find('input', {'name': 'product_desc'})['value']
    parsed_name = product_name.split(' - ')[0]
    parsed_name = parsed_name.replace(vendor, '').lstrip()

    return {'name': str(parsed_name), 'vendor': str(vendor), 'colors': colors, 'price':price}


def parse_price(product_soup):
    pscript = product_soup.find('script')
    ptext = str(pscript)
    price_iterator = re.finditer('"price":[0-9]+.[0-9]+', ptext)
    first_price = next(price_iterator)
    price_string = ptext[first_price.start():first_price.end()]
    price = price_string.split(':')[1]
    return price


def parse_colors(product_soup):
    script_tag = product_soup.find('script')
    script_text = str(script_tag)
    color_iterator = re.finditer('"displayName":"[a-zA-Z]+"', script_text)

    colors = set()

    sizes = {'S', 'M', 'XL', 'XXL', 'L', 'XS'}

    while True:
        try:
            next_color = next(color_iterator)
            color_match = script_text[next_color.start():next_color.end()]
            color = color_match.split(':')[1].replace('"', '')
            if color not in sizes:
                colors.add(color)
        except Exception as e:
            break

    return colors


url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'

# product = get_product_detail(url)

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

product_soup = soup.find("div", {"id": "product-container"})

colors = parse_colors(product_soup)
price = parse_price(product_soup)

vendor = product_soup.find('input', {'name': 'vendor'})['value']

product_name = product_soup.find('input', {'name': 'product_desc'})['value']
parsed_name = product_name.split(' - ')[0]
parsed_name = parsed_name.replace(vendor, '').lstrip()


string_soup = str(soup)

product_soup_string = str(product_soup)
media_iterator = re.finditer('media/', product_soup_string)

while True:
    try:
        next_media = next(media_iterator)
        print(product_soup_string[next_media.start()-100:next_media.start()+300])

        # color_match = script_text[next_color.start():next_color.end()]
        # color = color_match.split(':')[1].replace('"', '')
        # if color not in sizes:
        #     colors.add(color)
    except Exception as e:
        break


soup_string = str(soup)
image_iterator = re.finditer('media/', product_soup_string)

while True:
    try:
        next_media = next(media_iterator)
        print(product_soup_string[next_media.start() - 100:next_media.start() + 300])
    except Exception as e:
        break


soup = BeautifulSoup(page.text, 'html.parser')
# for div in soup.find_all("div", {"id": "product-container"}):
#     div.decompose()


soup.find("div", {"id": "product-container"})

soup_string = str(soup)
image_iter = re.finditer('<img src=', soup_string)
while True:
    try:
        next_img = next(image_iter)
        print(soup_string[next_img.start() - 100:next_img.start() + 300])
    except Exception as e:
        break
