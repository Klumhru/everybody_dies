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
