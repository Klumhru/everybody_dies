#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.utils2d
"""
from __future__ import unicode_literals, print_function, absolute_import

from math import sqrt, pow


def distancesqr(p1, p2):
    """Calculate the squared distance between two points"""
    rel = [p1[0] - p2[0],
           p1[1] - p2[1]]
    return pow(rel[0], 2) + pow(rel[1], 2)


def distancesqrt(p1, p2):
    """Calculate the distance between two points"""
    return sqrt(distancesqr(p1, p2))


def average(a):
    """Calculate the average position of an array of points"""
    if not a or not len(a):
        return [0, 0]
    ret = [0, 0]
    for p in a:
        ret[0] += p[0]
        ret[1] += p[1]
    return [ret[0] / len(a),
            ret[1] / len(a)]
