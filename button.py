from collections import defaultdict
from color import *

import sys, pygame
from pygame.locals import *
from label import Label
from widget import Widget


__author__ = 'richard'


class Button(Widget):
    def __init__(self, screen):
        self.buttons = {}
        self.screen = screen
        self.attributes = defaultdict(dict)
        self.render_queue = None
        self.label = Label(screen)

    def add_button(self,name,task_on_click,x1,y1,x2,y2):
        self.buttons[name] = (task_on_click,x1,x2,y1,y2)
        self.attributes[name]['x_left'] = x1
        self.attributes[name]['y_top'] = y1
        self.attributes[name]['width'] = x2 - x1
        self.attributes[name]['height'] = y2 - y1
        self.attributes[name]['color'] = red
        self.label.add_label(name,'',x1,y1,active=False)



    def add_attributes(self,name,type, value):
        self.attributes[name][type] = value
        if type == 'text':
            self.label.set_text(name,value)
            self.label.add_attribute(name,'active',True)
        #if we are chaing the position of the button, we need to update the position of the label as well
        if type=='x_left':
            self.label.add_attribute(name,'x',value)
        if type=='y_top':
            self.label.add_attribute(name,'y',value)
        if type=='text_size':
            self.label.add_attribute(name,'size',value)
        if type=='text_color':
            self.label.add_attribute(name,'color',value)

        self.render_queue.put(1)


    def set_render_queue(self, queue):
        self.label.set_render_queue(self.render_queue)
        super(Button,self).set_render_queue(queue)




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

        #render the labels in the buttons after we do the backgrounds
        self.label.__render__()



