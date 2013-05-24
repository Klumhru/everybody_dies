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

    def test_get_start_room(self):
        room = self.level_gen._get_start_room()
        self.assertEqual(room.id, 15)
        get_room = self.level_gen.get_room(15)
        self.assertEqual(room, get_room)

    def test_rooms(self):
        self.assertTrue(self.level_gen.height == 20)
        self.assertTrue(self.level_gen.width == 20)
        self.assertGreater(len(self.level.rooms), 0)
        room1 = self.level.get_room(1)
        self.assertIsNotNone(room1)

    def test_room_neighbours(self):
        room15 = self.level.get_room(15)
        self.assertIsNotNone(room15)
        adjoining = [self.level.get_room(6),
                     self.level.get_room(9)]
        self.assertEqual(len(adjoining), len(room15.neighbours))
        for r in adjoining:
            self.assertTrue(r in room15.neighbours)

        room3 = self.level.get_room(3)
        self.assertIsNotNone(room3)
        adjoining = [self.level.get_room(2),
                     self.level.get_room(9)]
        for r in adjoining:
            self.assertTrue(r in room3.neighbours)
        self.assertListEqual(room3.neighbours, adjoining)

    def test_flood_rooms(self):
        flooded = [self.level_gen._get_start_room()]
        dry = [r for r in self.level_gen.rooms if r not in flooded]

        self.assertListEqual(flooded, [self.level_gen.get_room(15)])

        self.level_gen._flood_rooms(flooded, dry)
        self.assertEqual(len(flooded), 7)
        self.assertEqual(len(dry), 8)

        # Ids for the rooms that should be flooded after first go
        expected = [1, 2, 3, 6, 9, 10, 15]
        self.assertListEqual(expected, sorted([r.id for r in flooded]))

    def tearDown(self):
        self.level_gen = None
