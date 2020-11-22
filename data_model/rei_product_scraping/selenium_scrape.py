"""
This file demonstrates how to download an image with the help of Selenium

"""


from selenium import webdriver

driver = webdriver.Chrome('/home/mddarr/data/libraries/selenium/chromedriver')
driver.get("https://www.rei.com/product/154144/patagonia-better-sweater-fleece-jacket-mens")

img = driver.find_element_by_class_name('media-center-primary-image')
src = img.get_attribute('src')
with open('filename.png', 'wb') as file:
    file.write(img.screenshot_as_png)