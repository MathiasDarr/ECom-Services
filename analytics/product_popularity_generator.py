"""
This script assigns a 'popularity' value to each product, representing the probability that it will be ordered.


"""
# !/usr/bin/env python3

import json
import random


def sum_to_one(n):
    """
    This function generates a list of n values who sum is 1.0.
    :param n: number of values
    :return:
    """
    values = [0.0, 1.0] + [random.random() for _ in range(n - 1)]
    values.sort()
    return [values[i+1] - values[i] for i in range(n)]


# Opening JSON file
with open('products/products.json') as json_file:
    data = json.load(json_file)

## Each item is assigned a popularity score, indicating the probability that when an item is purchased, that this will be the item
popularity_values = sum_to_one(len(data))

items_dictionary = {}  # Dictionary which maps itemID to the item
items_popularity_list = []  # A list of items w/ associated item popularity

for i, item in enumerate(data):
  items_dictionary[item['productID']] = item
  items_popularity_list.append((popularity_values[i], item['productID']))


### Write the data to a file as to improve the reproducability
with open('products_popularity.txt', 'w') as f:
  f.writelines("{},{}\n".format(item[1], item[0]) for item in items_popularity_list)


def select_item(items, weights, k):
    """
    Selects an item according to the probability in weights
    :param items:
    :param weights:
    :param: k -> number of items to select
    :return:
    """
    x = random.choices(items, weights=weights, k=k)
    return x

item_popularity_zip = list(zip(*items_popularity_list))
items = item_popularity_zip[1]
popularity = item_popularity_zip[0]

select_item(items, popularity, 1)

