#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
everybody_dies.test_generate
============================

Simply runs generate
"""
from __future__ import unicode_literals, print_function, absolute_import

import sys

from generator.level_generator import LevelGenerator


if __name__ == '__main__':

    gen = LevelGenerator(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
    level = gen.generate(rooms=int(sys.argv[4]))
    print(level)
