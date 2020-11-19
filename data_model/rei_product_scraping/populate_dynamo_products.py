"""

"""

import csv
import os

csv_directory = 'data_model/rei_product_scraping/data'
product_csv_files = ['{}/{}'.format(csv_directory, file) for file in os.listdir(csv_directory)]

keys = ['name', 'vendor', 'colors','price', 'url', 'category']

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'])
              # , row['vendor'], row['colors'], row['price'])