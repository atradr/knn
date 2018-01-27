# Well, it works.

import math

import numpy as np


def calculate_distance(test_row, train_row):
    """ Returns the distance between two vectors."""
    element_sums = 0
    for i in range(len(test_row) - 1):
        element_sums += (test_row[i] - train_row[i])**2
    return math.sqrt(element_sums)


def get_nearest_class(test_row, train):
    distance = calculate_distance(test_row, train[0])
    nearest = train[0][4]
    for row in train:
        cur_dist = calculate_distance(test_row, row)
        if cur_dist < distance:
            distance = cur_dist
            nearest = row[4]
    return nearest


def main():
    data = np.genfromtxt('iris.data.txt', delimiter=',', dtype=None)

    np.random.shuffle(data)

    train = data[0:125]
    test = data[125:]

    num_correct = 0
    for row in test:
        nearest = get_nearest_class(row, train)
        if row[4] == nearest:
            num_correct += 1
    print(num_correct)


if __name__ == '__main__':
    main()
