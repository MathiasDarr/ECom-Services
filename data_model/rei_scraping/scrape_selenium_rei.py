"""
Attempt to


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/home/mddarr/data/libraries/selenium/chromedriver')
driver.get("https://www.rei.com/c/mens-casual-jackets")


# Get the categories



categories = ['mens-casual-jackets', 'mens-boots','mens-insulated-jackets','mens-fleece-and-soft-shell-jackets'
              'mens-rain-jackets','mens-running-jackets','mens-wind-shells', 'mens-snow-jackets', 'mens-winter-boots',
              'backpacking-packs', 'day-packs', 'womens-boots', 'womens-casual-jackets', 'womens-insulated-jackets',
              'womens-fleece-and-soft-shell-jackets', 'womens-rain-jackets', 'womens-running-jackets'
              ]




https://www.rei.com/c



import requests
from bs4 import BeautifulSoup

pagenumber = 1
url =  'https://www.rei.com/c/{}'.format('mens-winter-boots')

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
navclass = soup.find("nav", {"class": "_3-4shQxwfGRyzNItrZFEiC"})
npages = len(navclass.find_all('a', href=True))

products = set()
while pagenumber <= npages:
    url = 'https://www.rei.com/c/{}?page={}'.format('mens-winter-boots',pagenumber)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    search_results = soup.find('div', {'id': 'search-results'})
    for a in search_results.find_all('a', href=True):
        products.add(a['href'])
        # print("Found the URL:", a['href'])
    pagenumber +=1

# print(pagenumber)
# url = 'https://www.rei.com/c/{}'.format('mens-casual-jackets') if pagenumber == 1 else \
#     'https://www.rei.com/c/{}?page='.format('mens-casual-jackets', pagenumber)
# page = requests.get(url)
#
# soup = BeautifulSoup(page.text, 'html.parser')
#

for a in search_results.find_all('a', href=True):
     print("Found the URL:", a['href'])


#    pagenumber +=1



# home_page requests.get('https://www.rei.com/c/mens-insulated-jackets')
#
# page = requests.get('https://www.rei.com/c/mens-insulated-jackets')
#
# soup = BeautifulSoup(page.text, 'html.parser')
#
#
# search_results = soup.find('div', {'id':'search-results'})
#
#
#
#
navclass = soup.find("nav", {"class": "_3-4shQxwfGRyzNItrZFEiC"})

