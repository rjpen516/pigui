from Clickable import Clickable
from button import Button
from label import Label
from color import *


__author__ = 'richard'


class ClickableLabelButton(Button):
    def on_click(self, x, y):
        for button in self.buttons:
            value = self.buttons[button]
            if value[1] <= x <= value[2] and value[3] <= y <= value[4]:
                value[0](button)
                print "Button Press on %s at (%s,%s) and sending button name" % (button, x, y)


class ClickableLabel(Label, Clickable):
    def __init__(self, screen):
        super(ClickableLabel, self).__init__(screen)
        self.button = ClickableLabelButton(screen)

    def add_label(self, name, value, x, y, task, active=True):
        super(ClickableLabel, self).add_label(name, value, x, y, active)
        # create new button that will span the value
        self.add_attribute(name, 'base_x', x)
        self.add_attribute(name, 'base_y', y)
        self.button.add_button(name, task, x, y,
                               self.get_attribute(name, 'size') * len(value) + x,
                               self.get_attribute(name, 'size') + y)
        self.button.add_attribute(name, 'color', white)

    def add_attribute(self, name, type, value):
        if type == 'button_color':
            self.button.add_attribute(name, 'color', value)
            return

        super(ClickableLabel, self).add_attribute(name, type, value)
        # if the size changes, we need to update the button
        if type == 'size' or type == 'x' or type == 'y':
            self.button.set_button_placement(name,
                                             self.get_attribute(name, 'x'),
                                             self.get_attribute(name, 'y'),
                                             self.get_attribute(name, 'x') + self.get_attribute(name, 'size') * len(
                                                 self.get_text(name)),
                                             self.get_attribute(name, 'y') + self.get_attribute(name, 'size'))

        self.render_queue.put(1)


    def set_text(self, name, value):
        super(ClickableLabel, self).set_text(name, value)
        # update that button to span the new text area
        self.button.set_button_placement(name,
                                         self.get_attribute(name, 'x'),
                                         self.get_attribute(name, 'y'),
                                         self.get_attribute(name, 'x') + self.get_attribute(name, 'size') * len(
                                             self.get_text(name)),
                                         self.get_attribute(name, 'y') + self.get_attribute(name, 'size'))

    def set_render_queue(self, queue):
        super(ClickableLabel, self).set_render_queue(queue)
        self.button.set_render_queue(queue)


    def set_runner(self, runner):
        super(ClickableLabel, self).set_runner(runner)
        self.button.set_runner(runner)

    def __render__(self):
        self.button.__render__()
        super(ClickableLabel, self).__render__()


    def on_click(self, x, y):
        self.button.on_click(x, y)
