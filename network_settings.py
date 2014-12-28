import pprint
from pigui.button import Button
from pigui.canvas import Canvas
from pigui.color import *
from pigui.label import Label

import netifaces



__author__ = 'richard'



class NetworkSettings(Canvas):
    def __init__(self, name,interface):
        super(NetworkSettings,self).__init__(name)
        self.interface = interface

    def __setup__(self, screen):

        self.button = Button(screen)
        self.label = Label(screen)


        self.register_widgets(self.button)
        self.register_widgets(self.label)

        self.label.add_label('welcome', 'Network Settings', 125, 5)
        self.label.add_attribute('welcome', 'size', 34)

        self.label.add_label('welcome_undertext', 'For interface: ' + self.interface, 125, 30)
        self.label.add_attribute('welcome_undertext', 'size', 15)

        self.button.add_button('back', self.runner.back_canvas, 0, 0, 30, 30)
        self.button.add_attributes('back', 'text', '<<')
        self.button.add_attributes('back', 'color', cream)
        self.button.add_attributes('back', 'text_size', 20)

        self.get_information()


    def get_information(self):
        interfaces = netifaces.interfaces()

        pprint.pprint(interfaces)