import requests
from bs4 import BeautifulSoup
import json


def get_product_detail(url):
    """
    This function takes a url of a product and returns a dictionary of the product name, product vendor, the colors
    in which it is sold & the price
    :param url: url of a product on rei website
    :return:
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    product_selection = soup.find("div", {"class": "product-color-and-size-selection"})

    pscript = product_selection.find('script')
    script_text = pscript.text

    products_json = json.loads(script_text)

    size_list = products_json['sizeList'][0]
    size_colors = size_list['colors']
    colors = {item['label'] for item in size_colors}

    product_soup = soup.find("div", {"id": "product-container"})
    vendor = product_soup.find('input', {'name': 'vendor'})['value']
    product_name = product_soup.find('input', {'name': 'product_desc'})['value']
    parsed_name = product_name.split(' - ')[0]
    parsed_name = parsed_name.replace(vendor, '').lstrip()

    product = {'name': parsed_name, 'vendor': vendor, 'colors': colors}
    return product


def get_products(category):
    """
    This function takes a category i.e 'mens-casual-jackets' (as found on the rei.com website) & returns a list of
    product urls :param category: :return: list of product urls
    """
    pagenumber = 1
    url =  'https://www.rei.com/c/{}'.format(category)

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    navclass = soup.find("nav", {"class": "_3-4shQxwfGRyzNItrZFEiC"})
    npages = len(navclass.find_all('a', href=True))

    products = set()
    while pagenumber <= npages:
        url = 'https://www.rei.com/c/{}?page={}'.format(category,pagenumber)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        search_results = soup.find('div', {'id': 'search-results'})
        for a in search_results.find_all('a', href=True):
            products.add(a['href'])
            # print("Found the URL:", a['href'])
        pagenumber +=1

    return ['https://www.rei.com' + str(product) for product in products if str(product).find('rei-garage') < 0]


categories = ['mens-casual-jackets', 'mens-boots','mens-insulated-jackets','mens-fleece-and-soft-shell-jackets'
              'mens-rain-jackets','mens-running-jackets','mens-wind-shells', 'mens-snow-jackets', 'mens-winter-boots',
              'backpacking-packs', 'day-packs', 'womens-boots', 'womens-casual-jackets', 'womens-insulated-jackets',
              'womens-fleece-and-soft-shell-jackets', 'womens-rain-jackets', 'womens-running-jackets']

products = get_products(categories[0])
url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'
product = get_product_detail(url)