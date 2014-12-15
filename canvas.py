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
    def __init__(self,name):
        self.name = name
        self.objects = []

    def __setup__(self):
        #preform any setup modules here (like init buttons)
        pass

    def set_screen(self,screen):
        self.screen = screen


    def register_widgets(self, widget):
        self.objects.append(widget)

    def on_click(self,x,y):
        for object in self.objects:
            if isinstance(object,Button):
                object.on_click(x,y)
        #after we run the user code, we need to update the screen, so lets render it up
        self.__render__()

    def __render__(self):
        for object in self.objects:
            object.__render__()


