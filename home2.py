__author__ = 'richard'

from canvas import Canvas
from label import Label
from button import Button
from color import *



output_label = None

has_shown = True

def exit_task():
    print "Hello World"
    global has_shown

    output_label.add_attribute('example2','active',has_shown)

    has_shown = not has_shown





class Home2(Canvas):
    def __setup__(self, screen):
        button = Button(screen)
        label = Label(screen)

        self.register_widgets(button)
        self.register_widgets(label)

        
        button.add_button('exit',exit_task,50,50,100,100)
        button.add_attributes('exit','color',red)
        button.add_attributes('exit','text','Hid Text')


        button.add_button('test2',self.back_task,200,200,225,225)
        button.add_attributes('test2','color',blue)
        button.add_attributes('test2','text','Back')


        label.add_label('example','Hello World',50,30)
        label.add_label('example2','I love world',225,30,active=False)


        global output_label
        output_label = label

    def back_task(self):
        self.runner.back_canvas()



