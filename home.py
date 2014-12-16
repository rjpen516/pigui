__author__ = 'richard'

from canvas import Canvas
from label import Label
from button import Button
from color import *


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



        self.label.add_label('xvalue_label', 'X:',0,100)
        self.label.add_label('xvalue_value', '', 20,100)

        self.label.add_label('yvalue_label', 'Y:',0,150)
        self.label.add_label('yvalue_value', '', 20,150)
        

        self.button.add_button('test2',self.move_down,200,200,225,225)
        self.button.add_attributes('test2','color',blue)

        self.button.add_button('update_value',self.update_xy_value,0,100,40,150)
        self.button.add_attributes('update_value','color',green)


        global output_label
        output_label = self.label

        self.update_xy_value()



    def update_xy_value(self):
        self.label.add_attribute('xvalue_value','text',self.label.get_attribute('welcome_undertext','x'))
        self.label.add_attribute('yvalue_value','text',self.label.get_attribute('welcome_undertext','y'))

    def move_down(self):
        self.label.add_attribute('welcome_undertext','y',self.label.get_attribute('welcome_undertext','y')+5)
        self.update_xy_value()
        self.label.__render__()






