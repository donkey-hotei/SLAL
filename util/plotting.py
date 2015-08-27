# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from SLALutil import vector2list, \
    listlist2matrix, \
    matrix2collist
from pylab import *


def draw_vector(soa):

    X, Y, U, V = zip(*soa)
    plt.figure()
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    ax.set_xlim([-1, 10])
    ax.set_ylim([-1, 10])
    plt.draw()


if __name__ == '__main__':

    M = listlist2matrix([[0, 0, 3, 2],
                         [0, 0, 1, 1],
                         [0, 0, 9, 9]])
    print(M)
    v_list = matrix2collist(M)
    print(v_list)

    lst = np.array([vector2list(v) for v in v_list])
    print(lst)

    draw_vector(lst)
    soa = np.array([[0, 0, 3, 2], [0, 0, 1, 1], [0, 0, 9, 9]])

    X, Y, U, V = zip(*soa)
    plt.figure()
    ax = plt.gca()
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    ax.set_xlim([-1, 10])
    ax.set_ylim([-1, 10])
    plt.draw()

    # Set limits and number points in grid
    xmax = 2.0
    xmin = -xmax
    NX = 10
    ymax = 2.0
    ymin = -ymax
    NY = 10
