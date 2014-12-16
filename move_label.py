from Clickable import Clickable
from widget import Widget

__author__ = 'richard'


from canvas import Canvas
from label import Label
from button import Button
from color import *



class MoveLabel(Widget,Clickable):
    def __init__(self,screen,label_name,widget):
        self.screen = screen
        self.widget_name = label_name
        self.widget = widget

        self.button = Button(screen)
        self.label = Label(screen)


    def __setup__(self):
        self.label.add_label('xvalue_label', 'X:',0,100)
        self.label.add_label('xvalue_value', '', 20,100)

        self.label.add_label('yvalue_label', 'Y:',0,150)
        self.label.add_label('yvalue_value', '', 20,150)


        self.button.add_button('up',self.move_up,200,200,225,225)
        self.button.add_attributes('up','text','^')
        self.button.add_attributes('up','color',green)
        self.button.add_attributes('up','text_size',15)


        self.button.add_button('down',self.move_down,200,225,225,250)
        self.button.add_attributes('down','text','V')
        self.button.add_attributes('down','color',green)
        self.button.add_attributes('down','text_size',15)

        self.button.add_button('left',self.move_left,175,225,200,250)
        self.button.add_attributes('left','text','<')
        self.button.add_attributes('left','color',green)
        self.button.add_attributes('left','text_size',15)

        self.button.add_button('right',self.move_right,225,225,250,250)
        self.button.add_attributes('right','text','>')
        self.button.add_attributes('right','color',green)
        self.button.add_attributes('right','text_size',15)


        self.button.add_button('update_value',self.update_xy_value,0,100,40,200)
        self.button.add_attributes('update_value','color',white)


    def on_click(self,x,y):
        self.button.on_click(x,y)

    def set_render_queue(self, queue):
        print "MoveLabel Widget"
        self.button.set_render_queue(queue)
        self.label.set_render_queue(queue)
        super(MoveLabel,self).set_render_queue(queue)


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
        self.label.add_attribute('welcome_undertext','x',self.label.get_attribute('welcome_undertext','x')-5)
        self.update_xy_value()
        self.label.__render__()

    def move_right(self):
        self.label.add_attribute('welcome_undertext','x',self.label.get_attribute('welcome_undertext','x')+5)
        self.update_xy_value()
        self.label.__render__()

    def __render__(self):
        self.button.__render__()
        self.label.__render__()
        self.widget.__render__()