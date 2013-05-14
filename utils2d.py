#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.utils2d
"""
from __future__ import unicode_literals, print_function, absolute_import

from math import sqrt, pow


def distancesqr(p1, p2):
    """Calculate the squared distance between two points"""
    return pow(p1, 2) + pow(p2, 2)


def distancesqrt(p1, p2):
    """Calculate the distance between two points"""
    return sqrt(distancesqr(p1, p2))


def average(a):
    """Calculate the average position of an array of points"""
    if not len(a):
        return [0, 0]
    ret = [0, 0]
    for p in a:
        ret[0] += p[0]
        ret[1] += p[1]
    return [ret[0] / len(a), ret[1] / len(a)]
