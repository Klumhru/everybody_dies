#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.generator.room
=============================

The Room class contains a grid of position references, an id and
a position reference
"""
from __future__ import unicode_literals, print_function, absolute_import

import unittest
from random import randint


class Room:

    def __init__(self, id=None, grid=None):
        """Creates a room and sets defaults"""

        self.id = id or 0
        self.pos = [0, 0]
        self.grid = grid or []

    def make(self, grid):
        """Create the room within the given grid

        :param grid: The grid to use as limits

        :return the new room:
        """

        self.width = randint(3, 5)
        self.height = randint(3, 5)

    def __repr__(self):
        return "<Room(%(id)s), pos(%(pos)s) W: %(width)s, H: %(height)s>" % \
            self.__dict__

    def get_connected_rooms(self):
        # Get adjoining rooms

        # Traverse hallways to connected rooms
        pass

    @property
    def top_border(self):
        return [[p[0], p[1] - 1] for p in self.top_edge]

    @property
    def top_edge(self):
        return [[x, self.pos[1]]
                for x in range(self.pos[0], self.pos[0] + self.width)]

    @property
    def bottom_border(self):
        return [[p[0], p[1] + 1] for p in self.bottom_edge]

    @property
    def bottom_edge(self):
        return [[x, self.pos[1] + self.height - 1]
                for x in range(self.pos[0], self.pos[0] + self.width)]

    @property
    def left_border(self):
        return [[p[0] - 1, p[1]] for p in self.left_edge]

    @property
    def left_edge(self):
        return [[self.pos[0], y]
                for y in range(self.pos[1], self.pos[1] + self.height)]

    @property
    def right_border(self):
        return [[p[0] + 1, p[1]] for p in self.right_edge]

    @property
    def right_edge(self):
        return [[self.pos[0] + self.width - 1, y]
                for y in range(self.pos[1], self.pos[1] + self.height)]
