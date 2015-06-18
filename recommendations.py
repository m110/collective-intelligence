#!/usr/bin/python3
import json
import random
from math import sqrt


def sim_distance(items, user_a, user_b):
    common_items = {item for item in items[user_a]
                    if item in items[user_b]}

    if not common_items:
        return 0.0

    squares = [pow(items[user_a][item] - items[user_b][item], 2)
               for item in common_items]

    return 1.0 / (1.0 + sqrt(sum(squares)))


def sim_pearson(items, user_a, user_b):
    common_items = {item for item in items[user_a]
                    if item in items[user_b]}

    if not common_items:
        return 0.0

    n = len(common_items)

    sum_a = sum([items[user_a][item] for item in common_items])
    sum_b = sum([items[user_b][item] for item in common_items])

    pow_sum_a = sum([pow(items[user_a][item], 2) for item in common_items])
    pow_sum_b = sum([pow(items[user_b][item], 2) for item in common_items])

    multiply_sum = sum([items[user_a][item] * items[user_b][item] for item in common_items])

    num = multiply_sum - (sum_a * sum_b / n)
    den = sqrt((pow_sum_a - pow(sum_a, 2) / n) * (pow_sum_b - pow(sum_b, 2) / n))

    if not den:
        return 0.0

    return num / den


def main():
    with open("data/critics.json", "r") as file:
        critics = json.load(file)

    with open("data/critics_normalized.json", "r") as file:
        critics_normalized = json.load(file)

    users = (random.sample(critics.keys(), 2))
    print("Comparing {} and {}".format(*users))
    print()

    print("Euclidean distance")
    result = sim_distance(critics, *users)
    print("\tstandard: {:.10f}".format(result))
    result = sim_distance(critics_normalized, *users)
    print("\tnormalized: {:.10f}".format(result))

    print()

    print("Pearson correlation")
    result = sim_pearson(critics, *users)
    print("\tstandard: {:.10f}".format(result))
    result = sim_pearson(critics_normalized, *users)
    print("\tnormalized: {:.10f}".format(result))


if __name__ == "__main__":
    main()
