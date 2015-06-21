#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as pyplot


def create_data_set():
    group = np.array([[1.0, 1.1],
                      [1.0, 1.0],
                      [0.0, 0.0],
                      [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines_count = len(lines)

    return_mat = np.zeros((lines_count, 3))
    class_labels = []
    index = 0

    for line in lines:
        split_line = line.strip().split()
        return_mat[index, :] = split_line[:3]
        class_labels.append(int(split_line[-1]))
        index += 1

    return return_mat, class_labels


def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]

    diff_mat = np.tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_dist_indicies = distances.argsort()

    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    sorted_class_count = sorted(class_count, key=class_count.get, reverse=True)
    return sorted_class_count[0][0]


def main_dating():
    matrix, labels = file2matrix('data/dating2.txt')

    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.scatter(matrix[:, 1], matrix[:, 2], 15.0 * np.array(labels), 15.0 * np.array(labels))
    pyplot.show()

if __name__ == "__main__":
    main_dating()
