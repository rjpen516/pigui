__author__ = 'richard'

from canvas import Canvas
from label import Label
from button import Button
from color import *
from move_label import MoveLabel

from home2 import Home2








class Home(Canvas):
    def __setup__(self, screen):
        self.button = Button(screen)
        self.label = Label(screen)


        self.register_widgets(self.button)
        self.register_widgets(self.label)


        self.label.add_label('welcome', 'Welcome to Hacking Pi',125,5)
        self.label.add_attribute('welcome','size',34)

        self.label.add_label('welcome_undertext','Your Source to a touchscreen hacking',125,30)
        self.label.add_attribute('welcome_undertext','size',15)
        self.label.add_attribute('welcome_undertext','color',red)

        self.move_label = MoveLabel(screen,'welcome_undertext',self.label)
        self.register_widgets(self.move_label)






