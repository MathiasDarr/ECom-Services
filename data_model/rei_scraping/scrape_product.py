import requests
from bs4 import BeautifulSoup
import json
import re

def get_product_detail(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    product_selection = soup.find("div", {"class": "product-color-and-size-selection"})

    script = product_selection.find('script')
    script_text = script.text

    products_json = json.loads(script_text)

    size_list = products_json['sizeList'][0]
    size_colors = size_list['colors']

    colors = {item['label'] for item in size_colors}

    product_soup = soup.find("div", {"id": "product-container"})

    price = parse_price(product_soup)

    vendor = product_soup.find('input', {'name': 'vendor'})['value']

    product_name = product_soup.find('input', {'name': 'product_desc'})['value']
    parsed_name = product_name.split(' - ')[0]
    parsed_name = parsed_name.replace(vendor, '').lstrip()

    product = {'name': parsed_name, 'vendor': vendor, 'colors': colors}
    return product


def parse_price(product_soup):
    pscript = product_soup.find('script')
    ptext = str(pscript)
    price_iterator = re.finditer('"price":[0-9]+.[0-9]+', ptext)
    first_price = next(price_iterator)
    price_string = ptext[first_price.start():first_price.end()]
    price = price_string.split(':')[1]
    return price


url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'

product = get_product_detail(url)

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
product_selection = soup.find("div", {"class": "product-color-and-size-selection"})
script_tag = product_selection.find('script')
script_text = str(script_tag)
color_iterator = re.finditer('"displayName":"[a-zA-Z]+"', script_text)

colors = set()

sizes = {'S','M','XL','XXL','L','XS'}


while True:
    try:
        next_color = next(color_iterator)
        color_match = script_text[next_color.start():next_color.end()]
        color = color_match.split(':')[1].replace('"','')
        if color not in sizes:
            colors.add(color)
    except Exception as e:
        break




# url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# product_soup = soup.find("div", {"id": "product-container"})
#
# pscript = product_soup.find('script')
# ptext = str(pscript)
#
# prices = set()
#
# price_iterator = re.finditer('"price":[0-9]+.[0-9]+',ptext)
# first_price = next(price_iterator)
# price_string = ptext[first_price.start():first_price.end()]
# price = price_string.split(':')[1]
#
# while True:
#     try:
#
#         first_price = next(price_iterator)
#         price_string = ptext[first_price.start():first_price.end()]
#         price = price_string.split(':')[1]
#         print(price)
#         prices.add(price)
#     except Exception as e:
#         break
#
ptext = ptext.replace('</script>','')
ptext = ptext.replace('<script ','')
#
# products_json = json.loads(script_text)


#
# vendor = product_soup.find('input',{'name':'vendor'})['value']
#
# product_name = product_soup.find('input',{'name':'product_desc'})['value']
# parsed_name = product_name.split(' - ')[0]
# parsed_name = parsed_name.replace(vendor, '').lstrip()
#
#
#
# product_selection = soup.find("div", {"class": "product-color-and-size-selection"})



