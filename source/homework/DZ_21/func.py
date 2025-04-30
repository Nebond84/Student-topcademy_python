import random


def random_list():
    num_list = []
    for i in range(5):
        num_list.append(random.randint(-10, 10))
    return num_list

