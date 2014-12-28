from collections import defaultdict

__author__ = 'richard'

from button import Button
from label import Label

from color import *
from widget import Widget
from canvas import Canvas
import pygame


class ListView(Widget):
    def __init__(self, screen, list, x1, y1, x2, y2, onselectaction, size=20):
        super(ListView, self).__init__()
        self.canvas = ListViewCanvas('list_view_picker', screen, list, x1, y1, x2, y2, self, size)
        self.active = False
        print "Creating ListView with left top (%d,%d) to (%d,%d)" % (x1, y1, x2, y2)
        self.onselect = onselectaction


    def __setup__(self):
        self.runner.add_canvas('list_view_picker', self.canvas)

    def set_active(self, active):
        self.canvas.set_active(active)
        self.active = active

    def set_runner(self, runner):
        super(ListView, self).set_runner(runner)
        self.canvas.set_runner(runner)

    def set_render_queue(self, queue):
        super(ListView, self, ).set_render_queue(queue)
        self.canvas.set_render_queue(queue)

    def __render__(self):
        if not self.active:
            return

        if self.runner.current_canvas != 'list_view_picker':
            self.runner.change_canvas('list_view_picker')


class ListViewCanvas(Canvas):
    def __init__(self, name, screen, list, x1, y1, x2, y2, widget, size=20):
        super(ListViewCanvas, self).__init__(name)
        self.list = list

        self.widget = widget

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.config = {}
        self.config['color'] = black
        self.config['text_size'] = size

        self.active = False

        self.first_element_seen = 0
        # this guy will determine how many elements we draw unto the screen, the font size is 20
        self.elements_on_screen = (y2 - y1) / self.config['text_size']
        self.selected = 0
        self.selected_window = 0

    def __setup__(self, screen):
        # create scroll system

        self.button = Button(screen)
        self.label = Label(screen)

        self.button.set_render_queue(self.render_queue)
        self.label.set_runner(self.runner)

        self.register_widgets(self.button)
        self.register_widgets(self.label)

        self.button.add_button('scroll_up', self.scroll_up, self.x2 - 20, self.y1, self.x2, self.y2 / 2)
        self.button.add_button('scroll_down', self.scroll_down, self.x2 - 20, self.y1 + (self.y2 - self.y1) / 2,
                               self.x2, self.y2)
        self.button.add_button('go_back', self.back, self.x1, self.y2 - 15, self.x1 + (self.x2 - self.x1) / 2, self.y2)
        self.button.add_button('select', self.select, self.x1 + (self.x2 - self.x1) / 2, self.y2 - 15, self.x2 - 20,
                               self.y2)

        self.button.add_attributes('scroll_up', 'color', green)
        self.button.add_attributes('scroll_down', 'color', blue)
        self.button.add_attributes('go_back', 'color', red)
        self.button.add_attributes('select', 'color', green)

        self.button.add_attributes('scroll_up', 'text_size', self.config['text_size'])
        self.button.add_attributes('scroll_down', 'text_size', self.config['text_size'])

        #setup the possible label slots onto the screen
        for i in range(0, self.elements_on_screen - 1):
            self.label.add_label(str(i), '', self.x1, self.y1 + self.config['text_size'] * i)
            self.label.add_attribute(str(i), 'size', self.config['text_size'])
            if i == self.selected:
                self.label.add_attribute(str(i), 'color', red)

    def set_active(self, active):
        self.active = active
        self.render_queue.put(1)

    def select(self):
        self.back()
        self.widget.onselect(self.selected)

    def update_labels(self):
        i = 0
        for item in self.list[max(self.selected - self.elements_on_screen, 0):]:
            self.label.set_text(str(i), item)
            i += 1

    def scroll_up(self):
        self.selected -= 1

        if(self.selected_window < self.selected):
            #we need to move everything down
            self.selected_windows += 1

        if(self.selected < 0):
            self.selected = 0

        self.label.add_attribute(str(self.selected + 1), 'color', black)
        self.label.add_attribute(str(self.selected), 'color', red)

    def scroll_down(self):
        self.selected += 1
        self.selected_window += 1

        # do a check to see if we have anymore to show, if not do nothing

        if (self.selected_window > self.elements_on_screen):
            #we need to move everything up
            self.selected_window -= 1
            pass


        if(self.selected > len(self.list)):
            self.selected -= 1

        self.label.add_attribute(str(self.selected_window - 1), 'color', black)
        self.label.add_attribute(str(self.selected_window), 'color', red)

    def back(self):
        self.active = False
        self.widget.active = False
        self.runner.back_canvas()

    def __render__(self):
        if not self.active:
            return

        self.update_labels()

        self.button.__render__()
        self.label.__render__()

        # draw the boarder around the guy
        width = self.x2 - self.x1
        higth = self.y2 - self.y1
        #print "Rendering the box from (%d,%d) to with width: %d, heigth %d" %(self.x1,self.y1,width,higth)
        pygame.draw.rect(self.screen, self.config['color'], (self.x1, self.y1, width, higth), 1)


    def add_attribute(self, name, type, value):
        self.attributes[name][type] = value

    def set_render_queue(self, queue):
        super(ListViewCanvas, self).set_render_queue(queue)

        # self.button.set_render_queue(queue)
        #self.label.set_render_queue(queue)

    def set_runner(self, runner):
        super(ListViewCanvas, self).set_runner(runner)

    #self.button.set_runner(runner)
    #self.label.set_runner(runner)


    def set_list(self, list):
        self.list = list

        
