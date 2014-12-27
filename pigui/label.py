from collections import defaultdict
import pygame
from color import *
__author__ = 'richard'

from widget import Widget

class Label(Widget):
    def __init__(self, screen):
        self.labels = {}
        self.screen = screen
        self.attributes = defaultdict(dict)
        self.render_queue = None


    def add_label(self, name, value,x,y,active=True):
        self.labels[name] = value
        self.attributes[name]['color'] = black
        self.attributes[name]['x'] = x
        self.attributes[name]['y'] = y
        self.attributes[name]['active'] = active
        self.attributes[name]['size'] = 34

    def add_attribute(self,name,type,value):
        
        if name not in self.attributes.keys():
            print "Missing Label, no label named %s" %(name)
        self.attributes[name][type] = value
        self.render_queue.put(1)


    def set_text(self, name ,value):
        self.labels[name] = value

    def get_text(self,name):
        return self.labels[name]

    def get_attribute(self,name,type):
        return self.attributes[name][type]


    def __render__(self):
        for key in self.labels:
            if self.attributes[key]['active'] == True:
                title_font=pygame.font.Font(None,self.attributes[key]['size'])
                label=title_font.render(self.labels[key], 1, (self.attributes[key]['color']))
                self.screen.blit(label,(self.attributes[key]['x'],self.attributes[key]['y']))
