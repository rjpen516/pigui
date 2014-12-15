from collections import defaultdict
from color import *

import sys, pygame
from pygame.locals import *

__author__ = 'richard'


class Button(object):
    def __init__(self, screen):
        self.buttons = {}
        self.screen = screen
        self.attributes = defaultdict(dict)
        self.render_queue = None

    def add_button(self,name,task_on_click,x1,y1,x2,y2):
        self.buttons[name] = (task_on_click,x1,x2,y1,y2)
        self.attributes[name]['x_left'] = x1
        self.attributes[name]['y_top'] = y1
        self.attributes[name]['width'] = x2 - x1
        self.attributes[name]['height'] = y2 - y1
        self.attributes[name]['color'] = red

    def add_attributes(self,name,type, value):
        self.attributes[name][type] = value

    def set_render_queue(self, queue):
        self.render_queue = queue


    def on_click(self,x,y):
        for button in self.buttons:
            #pprint(button)
            value = self.buttons[button]
            #print "I have X: %s <= %s <= %s  Y: %s <= %s <= %s" % (value[1],str(x),value[2],value[3],str(y),value[4])
            if value[1] <= x <= value[2] and value[3] <= y <= value[4]:
                value[0]()
                print "Button Press on %s at (%s,%s)" % (button,x,y)

    def __render__(self):
        for key in self.buttons:
            data = self.attributes[key]
            pygame.draw.rect(self.screen,data['color'],(data['x_left'],
                                              data['y_top'],
                                              data['width'],
                                              data['height']))


