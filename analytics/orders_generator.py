import random
from time import sleep

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

def read_products_popularity_file():
    items = []
    weights = []
    with open("products_popularity.txt") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            line_split = line.rstrip().split(",")
            items.append(line_split[0])
            weights.append(line_split[1])
    return items, weights

items, weights= read_products_popularity_file()

while True:
    sleep(random.randint(1, 5))
    print("hey")