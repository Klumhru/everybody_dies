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


class Utils2dTests(unittest.TestCase):

    def test_distancesqr(self):
        self.assertEqual(utils2d.distancesqr(2, 2), 8)

    def test_distancesqrt(self):
        expected = math.sqrt(18)
        # Couldn't be bothered finding a
        # number that would match sqrt(pow()+po())
        self.assertEqual(utils2d.distancesqrt(3, 3), expected)


class LevelTests(unittest.TestCase):

    def setUp(self):
        self.generator = LevelGenerator(width=20,
                                        height=20,
                                        algorithm='rooms')
        self.level = self.generator.generate()

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


class GeneratorTests(unittest.TestCase):

    def setUp(self):
        self.level_gen = LevelGenerator(width=20,
                                        height=20,
                                        algorithm='rooms')

    def test_tile_types(self):
        from .level_generator import tile_types

    def test_grid(self):
        self.level_gen._init_grid(self.level_gen.height, self.level_gen.width)
        self.assertTrue(len(self.level_gen.grid) == self.level_gen.height)
        for row in self.level_gen.grid:
            self.assertTrue(len(row) == self.level_gen.width)

    def test_rooms(self):
        self.assertTrue(self.level_gen.height == 20)
        self.assertTrue(self.level_gen.width == 20)
        level = self.level_gen.generate(rooms=10)
        self.assertGreater(len(level.rooms), 0)

    def tearDown(self):
        self.level_gen = None


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(id=10)

    def test_id(self):
        self.assertEquals(self.room.id, 10)

    def test_pos(self):
        self.assertEquals(self.room.pos, [0, 0])

    def test_grid(self):
        self.assertEquals(len(self.room.grid), 0)

    def tearDown(self):
        pass
