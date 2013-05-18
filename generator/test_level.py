#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.generator.tests
==============================

Unit tests for level generation
"""
from __future__ import unicode_literals, print_function, absolute_import

import unittest
import math

from .level import Level
from .level_generator import LevelGenerator
from .room import Room

import utils2d


class LevelTests(unittest.TestCase):

    def setUp(self):
        self.generator = LevelGenerator(width=20,
                                        height=20,
                                        algorithm='rooms',
                                        seed=123)
        self.level = self.generator.generate(rooms=15)

    def test_init(self):
        level = Level(grid=None, rooms=None)
        self.assertTrue(level is not None)

    def test_dimensions(self):
        self.assertTrue(self.level.width == 20)
        self.assertTrue(self.level.height == 20)

    def test_repr(self):
        s = str(self.level)
        print(s)
        self.assertTrue(len(s) > self.level.width * self.level.height)

    def tearDown(self):
        self.level = None
        self.generator = None
