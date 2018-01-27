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
    """Takes a row of data and finds the entry in the
    training set which is closest to it and returns
    that entry's target.
    """
    distance = calculate_distance(test_row, train[0])
    nearest = train[0][4]
    for row in train:
        cur_dist = calculate_distance(test_row, row)
        if cur_dist < distance:
            distance = cur_dist
            nearest = row[4]
    return nearest


def main():
    """Takes in the Iris data set 
    (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
    and separates the data randomly into a training and a test set.
    Then runs a shoddy knn (k=1) algorithm on each entry in the test set
    against the training data.
    """
    data = np.genfromtxt('iris.data.txt', delimiter=',', dtype=None)

    np.random.shuffle(data)

    train = data[0:100]
    test = data[100:]

    num_correct = 0
    for row in test:
        nearest = get_nearest_class(row, train)
        if row[4] == nearest:
            num_correct += 1
    print("Proportion correct: " + str((num_correct/len(test))))


if __name__ == '__main__':
    main()
