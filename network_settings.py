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


        self.button.add_button('dhcp_release',self.dhcp_release, self.runner.size[0]-90,0,self.runner.size[0],30)
        self.button.add_attributes('dhcp_release','text','DHCP Release')
        self.button.add_attributes('dhcp_release','color',red)
        self.button.add_attributes('dhcp_release','text_size',10)


        #information labels
        self.label.add_label('ip_addr_label','IP Address:',30,60)
        self.label.add_attribute('ip_addr_label','size',20)
        self.label.add_label('ip_addr', '',115,60)
        self.label.add_attribute('ip_addr','size',20)


        self.label.add_label('mac_addr_label','MAC: ',30,75)
        self.label.add_attribute('mac_addr_label','size',20)
        self.label.add_label('mac_addr','',115,75)
        self.label.add_attribute('mac_addr','size',20)



        self.get_information()

    def dhcp_release(self):
        pass


    def get_information(self):
        pprint.pprint(netifaces.ifaddresses(self.interface))

        info = netifaces.ifaddresses(self.interface)
        #get the ip addr
        if 2 in info:
            self.label.set_text('ip_addr',info[2][0]['addr'] + ' bc:' + info[2][0]['broadcast'] + ' nm:' + info[2][0]['netmask'])
        else:
            self.label.set_text('ip_addr','0.0.0.0')

        #get mac_address
        if 17 in info:
           self.label.set_text('mac_addr',info[17][0]['addr'])

