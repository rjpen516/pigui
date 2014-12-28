from pigui.clickable_label import ClickableLabel

__author__ = 'richard'

from pigui.canvas import Canvas
from pigui.label import Label
from pigui.button import Button
from pigui.color import *
from pigui.move_label import MoveLabel
from pigui.clickable_label import ClickableLabel
from pigui.listview import ListView
import sys
import os
import netifaces


class Settings(Canvas):
    def __setup__(self, screen):
        self.interface_list = []

        self.button = Button(screen)
        self.listview = ListView(screen, self.interface_list, 20, 20, self.runner.size[0] - 20,
                                 self.runner.size[1] - 20, self.on_wifi_select)
        self.label = Label(screen)
        self.clicklabel = ClickableLabel(screen)

        self.register_widgets(self.button)
        self.register_widgets(self.label)
        self.register_widgets(self.clicklabel)
        self.register_widgets(self.listview)

        self.label.add_label('title', 'General Settings', 125, 5)
        self.label.add_attribute('title', 'size', 34)

        self.label.add_label('title_undertext', 'General Settings for the Hacking Pi', 125, 30)
        self.label.add_attribute('title_undertext', 'size', 15)
        self.label.add_attribute('title_undertext', 'color', blue)

        self.button.add_button('network_settings', self.open_wifi_settings, 40, 150, 170, 200)
        self.button.add_attributes('network_settings', 'text', 'Net Setting')
        self.button.add_attributes('network_settings', 'color', blue)
        self.button.add_attributes('network_settings', 'text_color', white)

        self.button.add_button('back', self.back, 0, 0, 30, 30)
        self.button.add_attributes('back', 'text', '<<')
        self.button.add_attributes('back', 'color', cream)
        self.button.add_attributes('back', 'text_size', 20)

        self.clicklabel.add_label('wlan_ip_address', '', 40, 200, self.update_ip)
        self.clicklabel.add_attribute('wlan_ip_address', 'size', 20)
        self.clicklabel.add_attribute('wlan_ip_address', 'color', black)
        # self.clicklabel.add_attribute('ip_address','button_color',green)

        self.clicklabel.add_label('eth_ip_address', '', 40, 220, self.update_ip)
        self.clicklabel.add_attribute('eth_ip_address', 'size', 20)
        self.clicklabel.add_attribute('eth_ip_address', 'color', black)

        self.update_ip()

        self.button.add_button('shutdown', self.shutdown_pi, self.runner.size[0] - 60, self.runner.size[1] - 20,
                               self.runner.size[0], self.runner.size[1])
        self.button.add_attributes('shutdown', 'text', 'shutdown')
        self.button.add_attributes('shutdown', 'color', red)
        self.button.add_attributes('shutdown', 'text_size', 20)
        self.setup_interface()

    def on_wifi_select(self, index):
        print "I got the following index %d" % (index)

    def open_wifi_settings(self):
        self.listview.set_active(True)

    def open_settings(self):
        pass

    def back(self):
        self.runner.back_canvas()

    def setup_interface(self):
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            self.interface_list.append(interface)

    def update_ip(self):
        interfaces = netifaces.interfaces()
        if 'wlan0' not in interfaces:
            self.clicklabel.set_text('wlan_ip_address', 'no interface')
        else:
            addr = netifaces.ifaddresses('wlan0')
            if addr == None or 2 not in addr.keys() or addr[2][0]['addr'] == '':
                self.clicklabel.set_text('wlan_ip_address', 'wlan0:0.0.0.0')
            else:
                self.clicklabel.set_text('wlan_ip_address', 'wlan0:' + addr[2][0]['addr'])

        if 'eth0' not in interfaces:
            self.clicklabel.set_text('eth_ip_address', 'no interface')
        else:
            addr = netifaces.ifaddresses('eth0')
            if addr == None or 2 not in addr.keys() or addr[2][0]['addr'] == '':
                self.clicklabel.set_text('eth_ip_address', 'eth0:0.0.0.0')
            else:
                self.clicklabel.set_text('eth_ip_address', 'eth0:' + addr[2][0]['addr'])


    def shutdown_pi(self):
        self.label.add_label('shutdown', 'Shutting Down', 40, self.runner.size[1] / 2)
        self.label.add_attribute('shutdown', 'size', 40)
        os.system('shutdown -h now')
