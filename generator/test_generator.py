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


class GeneratorTests(unittest.TestCase):

    def setUp(self):
        self.level_gen = LevelGenerator(width=20,
                                        height=20,
                                        algorithm='rooms',
                                        seed=123)
        self.level = self.level_gen.generate(rooms=15)

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
        self.assertGreater(len(self.level.rooms), 0)
        room1 = self.level.get_room(1)
        self.assertIsNotNone(room1)

    def test_neighbours(self):
        room15 = self.level.get_room(15)
        self.assertIsNotNone(room15)
        adjoining = [self.level.get_room(6),
                     self.level.get_room(9)]
        self.assertEqual(len(adjoining), len(room15.neighbours))
        for r in adjoining:
            self.assertTrue(r in room15.neighbours)

    def test_flood_rooms(self):
        v = self.level_gen._flood_rooms(self.level_gen.rooms[:1])

    def tearDown(self):
        self.level_gen = None
