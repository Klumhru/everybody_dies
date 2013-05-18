#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.generator.test_utils2s
==============================

Unit tests for level generation
"""
from __future__ import unicode_literals, print_function, absolute_import

import unittest
import math

import utils2d


class Utils2dTests(unittest.TestCase):

    def test_distancesqr(self):
        self.assertEqual(utils2d.distancesqr(2, 2), 8)

    def test_distancesqrt(self):
        expected = math.sqrt(18)
        # Couldn't be bothered finding a
        # number that would match sqrt(pow()+pow())
        self.assertEqual(utils2d.distancesqrt(3, 3), expected)

    def test_average(self):
        expected = [2, 2]
        param = [[1, 1], [3, 3]]
        self.assertListEqual(utils2d.average(param), expected)
        expected = [0, 0]
        param = []
        self.assertListEqual(utils2d.average(param), expected)
        self.assertListEqual(utils2d.average(None), expected)
