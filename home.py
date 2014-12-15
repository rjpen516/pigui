__author__ = 'richard'

from canvas import Canvas
from label import Label
from button import Button
from color import *



def exit_task():
    print "Hello World"




class Home(Canvas):
    def __setup__(self, screen):
        button = Button(screen)
        label = Label(screen)

        self.register_widgets(button)
        self.register_widgets(label)

        
        button.add_button('exit',exit_task,50,50,100,100)
        button.add_attributes('exit','color',red)
        button.add_attributes('exit','text','EXIT')
        button.add_button('test2',exit_task,200,200,225,225)
        button.add_attributes('test2','color',blue)


        label.add_label('example','Example Label',50,30)
        label.add_label('example2','Fuck You',225,30,active=False)


