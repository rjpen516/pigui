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
        

        self.button.add_button('up',self.move_up,200,200,225,225)
        self.button.add_attributes('up','text','^')
        self.button.add_attributes('up','color',green)
        self.button.add_attributes('up','text_size',15)


        self.button.add_button('down',self.move_up,225,225,250,250)
        self.button.add_attributes('down','text','^')
        self.button.add_attributes('down','color',green)
        self.button.add_attributes('down','text_size',15)

        self.button.add_button('left',self.move_left,175,225,200,250)
        self.button.add_attributes('left','text','<')
        self.button.add_attributes('left','color',green)
        self.button.add_attributes('left','text_size',15)

        self.button.add_button('left',self.move_right,250,225,275,250)
        self.button.add_attributes('left','text','>')
        self.button.add_attributes('left','color',green)
        self.button.add_attributes('left','text_size',15)


        self.button.add_button('update_value',self.update_xy_value,0,100,40,200)
        self.button.add_attributes('update_value','color',white)



        self.update_xy_value()



    def update_xy_value(self):
        self.label.set_text('xvalue_value',str(self.label.get_attribute('welcome_undertext','x')))
        self.label.set_text('yvalue_value',str(self.label.get_attribute('welcome_undertext','y')))

    def move_down(self):
        self.label.add_attribute('welcome_undertext','y',self.label.get_attribute('welcome_undertext','y')+5)
        self.update_xy_value()
        self.label.__render__()

    def move_up(self):
        self.label.add_attribute('welcome_undertext','y',self.label.get_attribute('welcome_undertext','y')-5)
        self.update_xy_value()
        self.label.__render__()

    def move_left(self):
        self.label.add_attribute('welcome_undertext','y',self.label.get_attribute('welcome_undertext','x')-5)
        self.update_xy_value()
        self.label.__render__()

    def move_right(self):
        self.label.add_attribute('welcome_undertext','y',self.label.get_attribute('welcome_undertext','x')+5)
        self.update_xy_value()
        self.label.__render__()





