#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.generator.level
==============================

This generator has methods to generate levels according to the constructor
rules
"""
from __future__ import unicode_literals, print_function, absolute_import

import random
import unittest

from .room import Room


class Level:

    def __init__(self, grid=None, rooms=None):
        """This is a level, with a ready grid"""
        self.grid = grid or []
        self.rooms = rooms or []
        for room in self.rooms:
            room.level = self

    @property
    def width(self):
        return len(self.grid[0])

    @property
    def height(self):
        return len(self.grid)

    def __repr__(self):
        s = "Width: %s, Height: %s, Rooms: %s\n" % (self.width,
                                                    self.height,
                                                    len(self.rooms))
        s += self.grid_repr(self.grid)
        return s

    def get_room(self, id):
        for room in self.rooms:
            if room.id == id:
                return room
        return None

    @classmethod
    def grid_repr(cls, grid):
        s = '   ' + ''.join([str(i).ljust(20)
                            for i in range(0, len(grid[0]), 10)]) + '\n'
        s += '   ' + ' '.join(['%s' % (i % 10)
                               for i in range(0, len(grid[0]) + 1)]) + '\n'
        rowcount = 0
        for row in grid:
            s += str(rowcount).rjust(2) + ' '
            for tile in row:
                s += str(tile).rjust(2, b'0') if tile != 0 else '  '
            s += '\n'
            rowcount += 1
        return s
