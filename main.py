#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main
====

This is the main application module
"""
from __future__ import unicode_literals, print_function, absolute_import

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence


class MyGame(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.environ = self.loader.loadModel("assets/testing/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        self.taskMgr.add(self.spin_camera, "spin_camera")

        self.make_panda()

        self.make_panda_pace()

    def make_panda(self):
        self.panda = Actor("assets/testing/panda-model",
                           {"walk": "assets/testing/panda-walk4"})
        self.panda.setScale(0.005, 0.005, 0.005)
        self.panda.reparentTo(self.render)

        self.panda.loop("walk")

    def make_panda_pace(self):
        pos_interval1 = self.panda.posInterval(13,
                                               Point3(0, -10, 0),
                                               startPos=Point3(0, 10, 0))
        pos_interval2 = self.panda.posInterval(13,
                                               Point3(0, 10, 0),
                                               startPos=Point3(0, -10, 0))
        rot_interval1 = self.panda.hprInterval(3,
                                               Point3(180, 0, 0),
                                               startHpr=Point3(0, 0, 0))
        rot_interval2 = self.panda.hprInterval(3,
                                               Point3(0, 0, 0),
                                               startHpr=Point3(180, 0, 0))

        self.panda_pace = Sequence(pos_interval1,
                                   rot_interval1,
                                   pos_interval2,
                                   rot_interval2)
        self.panda_pace.loop()

    def spin_camera(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180)
        self.camera.setPos(20 * sin(angleRadians),
                           -20.0 * cos(angleRadians),
                           3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


if __name__ == "__main__":
    app = MyGame()
    app.run()
