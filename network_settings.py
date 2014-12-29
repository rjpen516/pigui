import pprint
import time
from pigui.button import Button
from pigui.canvas import Canvas
from pigui.color import *
from pigui.label import Label

import netifaces

import threading



__author__ = 'richard'



class NetworkSettings(Canvas):
    def __init__(self, name,interface):
        super(NetworkSettings,self).__init__(name)
        self.interface = interface
        self.t = None

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


        self.button.add_button('dhcp_release',self.dhcp_release, self.runner.size[0]-70,0,self.runner.size[0],25)
        self.button.add_attributes('dhcp_release','text','DHCP Release')
        self.button.add_attributes('dhcp_release','color',red)
        self.button.add_attributes('dhcp_release','text_size',15)

        self.button.add_button('dhcp_renew',self.dhcp_release, self.runner.size[0]-70,26,self.runner.size[0],50)
        self.button.add_attributes('dhcp_renew','text','DHCP Renew')
        self.button.add_attributes('dhcp_renew','color',green)
        self.button.add_attributes('dhcp_renew','text_size',15)


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

    def refresh_status(self,seconds):

        if self.t != None:
            return

        self.t = threading.Thread(target=self.refresh_worker,args=(seconds,))
        self.t.start()





    def refresh_worker(self,seconds):
        time_to_sleep = seconds*2

        for i in range(0,time_to_sleep):
            self.get_information()
            time.sleep(.5)




    def dhcp_release(self):

        self.refresh_status(15)


    def get_information(self):

        try:

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

        except:
            print "Error, clearning values"
            self.label.set_text('ip_addr','')
            self.label.set_text('mac_addr','Interface Error')

