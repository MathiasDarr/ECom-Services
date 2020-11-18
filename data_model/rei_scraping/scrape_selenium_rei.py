"""
Attempt to


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/home/mddarr/data/libraries/selenium/chromedriver')
driver.get("https://www.rei.com/c/mens-boots")


import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.rei.com/c/mens-insulated-jackets')

soup = BeautifulSoup(page.text, 'html.parser')

search_results = soup.find('div', {'id':'search-results'})


for a in search_results.find_all('a', href=True):
    print("Found the URL:", a['href'])