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


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(id=3)
        self.room.pos = [2, 2]
        self.room.width = 3
        self.room.height = 5
        self.room.grid = [[0 for x in range(10)]
                          for y in range(10)]

    def test_id(self):
        self.assertEquals(self.room.id, 3)

    def test_pos(self):
        self.assertEquals(self.room.pos, [2, 2])

    def test_grid(self):
        self.assertEquals(len(self.room.grid), 10)
        self.assertEquals(len(self.room.grid[9]), 10)

    def test_tiles(self):
        expected = [[2, 2], [3, 2], [4, 2],
                    [2, 3], [3, 3], [4, 3],
                    [2, 4], [3, 4], [4, 4],
                    [2, 5], [3, 5], [4, 5],
                    [2, 6], [3, 6], [4, 6]]
        self.assertListEqual(self.room.tiles, expected)

    def test_edges(self):
        self.assertEquals(len(self.room.edges), 4)

    def test_borders(self):
        self.assertEquals(len(self.room.borders), 4)

    def test_top_edge(self):
        """
        Check if the top edge matches expected results
        XXX
        O O
        O O
        O O
        OOO
        """
        self.assertListEqual(self.room.top_edge,
                             [[2, 2], [3, 2], [4, 2]])

    def test_top_border(self):
        """
        XXX
        OOO
        O O
        O O
        O O
        OOO
        """
        self.assertListEqual(self.room.top_border,
                             [[2, 1], [3, 1], [4, 1]])

    def test_bottom_edge(self):
        """
        Check if the bottom edge matches expected results
        OOO
        O O
        O O
        O O
        XXX
        """
        self.assertListEqual(self.room.bottom_edge,
                             [[2, 6], [3, 6], [4, 6]])

    def test_bottom_border(self):
        """
        OOO
        O O
        O O
        O O
        OOO
        XXX
        """
        self.assertListEqual(self.room.bottom_border,
                             [[2, 7], [3, 7], [4, 7]])

    def test_left_edge(self):
        """
        Check if the left edge matches expected results
        XOO
        X O
        X O
        X O
        XOO
        """
        self.assertListEqual(self.room.left_edge,
                             [[2, 2],
                             [2, 3],
                             [2, 4],
                             [2, 5],
                             [2, 6]])

    def test_left_border(self):
        """
        XOOO
        XO O
        XO O
        XO O
        XOOO
        """
        self.assertListEqual(self.room.left_border,
                             [[1, 2],
                             [1, 3],
                             [1, 4],
                             [1, 5],
                             [1, 6]])

    def test_right_edge(self):
        """
        Check if the right edge matches expected results
        OOX
        O X
        O X
        O X
        OOX
        """
        self.assertListEqual(self.room.right_edge,
                             [[4, 2],
                             [4, 3],
                             [4, 4],
                             [4, 5],
                             [4, 6]])

    def test_right_border(self):
        """
        OOOX
        O OX
        O OX
        O OX
        OOOX
        """
        self.assertListEqual(self.room.right_border,
                             [[5, 2],
                             [5, 3],
                             [5, 4],
                             [5, 5],
                             [5, 6]])

    def tearDown(self):
        pass
