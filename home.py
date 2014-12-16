__author__ = 'richard'

from canvas import Canvas
from label import Label
from button import Button
from color import *
from move_label import MoveLabel

from home2 import Home2



editor_up = False




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


        self.button.add_button('show_editor',self.make_moving_form_visable,0,self.runner.size[1]-20,78,self.runner.size[1])
        self.button.add_attributes('show_editor','text','Show Edit')
        self.button.add_attributes('show_editor','text_size',20)

        self.move_label = MoveLabel(screen,'welcome_undertext',self.label, visable=False)
        self.register_widgets(self.move_label)




    def make_moving_form_visable(self):
        global editor_up

        self.move_label.add_attribute('visable', not editor_up)
        editor_up = not editor_up
        self.button.add_attribute('show_editor','text','Hide Move')




