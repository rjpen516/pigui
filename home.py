__author__ = 'richard'

from canvas import Canvas
from label import Label
from button import Button
from color import *


from home2 import Home2

output_label = None

has_shown = True

def show_text_task():
    print "Hello World"
    global has_shown

    output_label.add_attribute('example2','active',has_shown)

    has_shown = not has_shown







class Home(Canvas):
    def __setup__(self, screen):
        button = Button(screen)
        label = Label(screen)

        self.register_widgets(button)
        self.register_widgets(label)


        label.add_label('welcome', 'Welcome to Hacking Pi',125,5)
        label.add_attribute('welcome','size',34)

        label.add_label('welcome_undertext','Your Source to a touchscreen hack',125,15)
        label.add_attribute('welcome_undertext','size',15)
        label.add_attribute('welcome_undertext','color',red)



        
        button.add_button('exit',show_text_task,50,50,100,100)
        button.add_attributes('exit','color',red)
        button.add_attributes('exit','text','EXIT')
        button.add_button('test2',self.new_canvas_task,200,200,225,225)
        button.add_attributes('test2','color',blue)




        global output_label
        output_label = label

    def new_canvas_task(self):
        home2 = Home2('home2')
        self.runner.add_canvas('home2',home2)
        self.runner.change_canvas('home2')





