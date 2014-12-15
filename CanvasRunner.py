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


os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()


class CanvasRunner(object):
    def __init__(self):
        self.canvas = {}
        self.default_canvas = ''
        self.canvas_stack = []
        self.current_canvas = ''

        self.size = width, height = 480, 320
        self.screen = pygame.display.set_mode(self.size)

    def add_canvas(self,name,canvas_obj):
        self.canvas[name] = canvas_obj

        self.canvas[name].set_screen(self.screen)

        self.canvas[name].__setup__(self.screen)

        if len(self.canvas.keys()) == 1:
            self.canvas_stack.append(canvas_obj)
            self.default_canvas = name
            self.current_canvas = name

    def set_default_canvas(self, name):
        self.default_canvas = name


    def __render__(self):
        self.screen.fill(white)
        self.canvas[self.current_canvas].__render__()
        pygame.display.flip()

    def main(self):
        self.__render__()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.canvas[self.current_canvas].on_click(pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            self.__render__()


