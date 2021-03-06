#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.generator.level_generator
========================================

The generator creates and delivers Level instances
"""
from __future__ import unicode_literals, print_function, absolute_import

import random

import utils2d

from .level import Level
from .room import Room

tile_types = [
    'w',
    'h'
]


class TooManyRoomsForGrid(Exception):
    pass


class LevelGenerator():
    """
    Instantiate with the desired algorithm and then call generate()
    with valid size values

    valid algorithms are:
        'rooms'
    """

    def __init__(self, height=20, width=20, algorithm='rooms', seed=None):
        """
        Instantiate the class and set some basic parameters for generation

        :param `height`: The max Y value for grid tiles
        :param `width`: The max X value for grid tiles
        :param `algorithm`: The type of algoritm to use to construct
                            levels
        """

        self.seed = seed or random.randint(0, 1000000)
        random.seed(self.seed)
        self._algos = {
            'rooms': self.rooms_generator
        }
        self.height = height
        self.width = width
        self.algorithm = algorithm
        self.grid = self._init_grid(height, width)

    def generate(self, *args, **kwargs):
        """
        Generate the dungeon grid. See the docs for the different algorithms
        for parameter information
        """

        self._init_grid(self.height, self.width)
        self._algos[self.algorithm](*args, **kwargs)
        return Level(grid=self.grid, rooms=self.rooms)

    def rooms_generator(self, rooms=10):
        """
        Generate a grid containg a certain number of rooms of a certain size

        :param rooms: The number of rooms to fit in the grid
        """

        self.rooms = [self._create_room(i) for i in range(1, rooms + 1)]
        self._place_rooms()
        self._connect_rooms()

    def _place_rooms(self):
        """Randomly place rooms within a grid"""
        max_tries = 100000
        not_placed = []
        for room in self.rooms:
            counter = 0
            while room.pos == [0, 0]:
                if counter > max_tries:
                    break
                room.pos = self._place_room(room)
                counter += 1
            if counter > max_tries:
                not_placed.append(room.id)
            self._mark_room(room)
        while len([r for r in self.rooms if r.id in not_placed]):
            self.rooms.remove([r for r in self.rooms
                              if r.id in not_placed][0])

    def _connect_rooms(self):
        unconnected_rooms = self.rooms
        connected_rooms = [self._get_start_room()]

    def _get_start_room(self):
        key_func = lambda r: utils2d.distancesqr([0, 0],
                                                 utils2d.average(r.tiles))
        return sorted(self.rooms,
                      key=key_func)[0]

    def _mark_room(self, room):
        for y in range(room.pos[1], room.pos[1] + room.height):
            for x in range(room.pos[0], room.pos[0] + room.width):
                try:
                    self.grid[y][x] = room.id
                except IndexError:
                    raise

    def _place_room(self, room):
        """Find a position in the grid with enough
        empty tiles to hold the room"""
        pos = [random.randint(1, self.width - room.width - 1),
               random.randint(1, self.height - room.height - 1)]
        for y in range(pos[1], pos[1] + room.height):
            for x in range(pos[0], pos[0] + room.width):
                # if the tile value is not 0 there is a room there
                try:
                    if self.grid[y][x] != 0:
                        return [0, 0]
                except IndexError:
                    raise
        return pos

    def _create_room(self, id):
        """
        Creates a room that contains a position and an array of rows

        :param id: The id to set on the new room
        :returns new Room instance:
        """

        room = Room(id=id, grid=self.grid, generator=self)
        room.make(self.grid)
        return room

    def _init_grid(self, height, width):
        """Initializes self.grid with a 2d grid defined by height and width"""
        self.grid = [[0 for x in range(width)]
                     for y in range(height)]

    def _flood_rooms(self, flooded, dry):
        """
        Finds all rooms connected to the romms in the array and adds them
        to the array and removes them from dry
        """
        updated = []

        for room in flooded:
            for connected in self.get_connected_rooms(room):
                if connected not in updated and connected not in flooded:
                    updated.append(connected)

        if len(updated):
            for room in updated:
                if room in dry:
                    dry.remove(room)
                if room not in flooded:
                    flooded.append(room)
            self._flood_rooms(flooded, dry)

    def get_room(self, id):
        for room in self.rooms:
            if room.id == id:
                return room
        return None

    def get_connected_rooms(self, room):
        ret = []
        # Get adjoining rooms
        for r in room.neighbours:
            ret.append(r)
        # Traverse hallways to connected rooms
        return ret
