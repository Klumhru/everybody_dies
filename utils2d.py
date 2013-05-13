#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.utils2d
"""
from __future__ import unicode_literals, print_function, absolute_import

from math import sqrt, pow


def distancesqr(p1, p2):
    return pow(p1, 2) + pow(p2, 2)


def distancesqrt(p1, p2):
    return sqrt(distancesqr(p1, p2))
