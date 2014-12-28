from Clickable import Clickable

__author__ = 'richard'

import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from pprint import pprint
from collections import defaultdict
from color import *
from button import Button
from label import Label


class Canvas(object):
    def __init__(self, name):
        self.name = name
        self.objects = []
        self.render_queue = None
        self.runner = None

    def __setup__(self):
        # preform any setup modules here (like init buttons)
        pass

    def set_screen(self, screen):
        self.screen = screen

    def set_render_queue(self, queue):
        self.render_queue = queue

    def set_runner(self, runner):
        self.runner = runner


    def register_widgets(self, widget):
        self.objects.append(widget)
        widget.set_render_queue(self.render_queue)
        widget.set_runner(self.runner)
        widget.__setup__()

    def on_click(self, x, y):
        print "Click on (%d,%d)" %(x,y)
        for object in self.objects:
            if isinstance(object, Clickable):
                object.on_click(x, y)
        # after we run the user code, we need to update the screen, so lets render it up
        self.__render__()

    def __render__(self):
        for object in self.objects:
            object.__render__()


