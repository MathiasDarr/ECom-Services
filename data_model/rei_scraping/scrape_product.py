import requests
from bs4 import BeautifulSoup
import json

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
    return colors





url = 'https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens'

colors = get_product_detail(url)
