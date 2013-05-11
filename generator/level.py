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


class LevelGenerator():
    """
    Instantiate with the desired algorithm and then call generate()
    with valid size values

    valid algorithms are:
        'rooms'
    """

    def __init__(self, height=20, width=20, algorithm='rooms'):
        """
        Instantiate the class and set some basic parameters for generation

        :param `height`: The max Y value for grid tiles
        :param `width`: The max X value for grid tiles
        :param `algorithm`: The type of algoritm to use to construct
                            levels
        """

        self._algos = {
            'rooms': self.rooms_generator
        }
        self.height = height
        self.width = width
        self.algorithm = algorithm
        self.grid = self._make_grid(height, width)

    def generate(self, *args, **kwargs):
        """
        Generate the dungeon grid. See the docs for the different algorithms
        for parameter information
        """

        self._algos[self.algorithm](*args, **kwargs)

    def rooms_generator(self, rooms=10):
        """
        Generate a grid containg a certain number of rooms of a certain size

        :param rooms: The number of rooms to fit in the grid
        """

        self.rooms = [self._create_room(i) for i in range(rooms)]

    def _create_room(self, id):
        """
        Creates a room that contains a position and an array of rows

        :param id: The id to set on the new room
        :returns new Room instance:
        """

        room = Room(id)
        room.make(self.grid)
        return room

    def _make_grid(self, height, width):
        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(0)
            grid.append(row)
        return grid
