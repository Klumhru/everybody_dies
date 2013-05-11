#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.generator.tests
==============================

Unit tests for level generation
"""
from __future__ import unicode_literals, print_function, absolute_import

import unittest

from .level import LevelGenerator
from .room import Room


class GeneratorTests(unittest.TestCase):

    def setUp(self):
        self.level_gen = LevelGenerator(width=13, height=13, algorithm='rooms')

    def test_grid(self):
        self.assertTrue(len(self.level_gen.grid) == self.level_gen.height)
        for row in self.level_gen.grid:
            self.assertTrue(len(row) == self.level_gen.width)

    def test_rooms(self):
        self.assertTrue(self.level_gen.height == 13)
        self.assertTrue(self.level_gen.width == 13)
        self.level_gen.generate(rooms=10)

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
