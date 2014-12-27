from pigui.clickable_label import ClickableLabel

__author__ = 'richard'

from pigui.canvas import Canvas
from pigui.label import Label
from pigui.button import Button
from pigui.color import *
from pigui.move_label import MoveLabel

from settings import Settings
import sys
import os

editor_up = False

current_label = None


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


        #self.button.add_button('show_editor',self.make_moving_form_visable,0,self.runner.size[1]-20,78,self.runner.size[1])
        #self.button.add_attributes('show_editor','text','Show Edit')
        #self.button.add_attributes('show_editor','text_size',20)

        #self.move_label = MoveLabel(screen,'welcome_undertext',self.label, visable=False)
        #self.register_widgets(self.move_label)

        self.button.add_button('kill_app',self.kill_app,0,self.runner.size[1]-20,40,self.runner.size[1])
        self.button.add_attributes('kill_app', 'text', 'Exit')
        self.button.add_attributes('kill_app', 'text_size',20)

	self.button.add_button('restart_app',self.restart_pi,40,self.runner.size[1]-20,100,self.runner.size[1])
	self.button.add_attributes('restart_app','text','Restart')
	self.button.add_attributes('restart_app','color',green)
	self.button.add_attributes('restart_app','text_color',white)
	self.button.add_attributes('restart_app','text_size',20)

        self.button.add_button('settings',self.open_settings,40,150,140,200)
        self.button.add_attributes('settings','text','Settings')
	self.button.add_attributes('settings','color', blue)
	self.button.add_attributes('settings','text_color',white)

	global current_label
	current_label = 'welcome_undertext'
	
	


    def make_moving_form_visable(self):
        global editor_up

        self.move_label.add_attribute('visable', not editor_up)
        editor_up = not editor_up
        self.button.add_attribute('show_editor','text','Hide Move')



    def change_button_click(self,name):
        self.move_label.set_select_label(name)

    def kill_app(self):
        print "The App Killed Sucesfully"
        sys.exit()
	
	
    def open_settings(self):
        settings = Settings('settings')
	self.runner.add_canvas('settings',settings)	
	self.runner.change_canvas('settings')

    def restart_pi(self):
	self.label.add_label('restart','Restarting your Pi, Please wait',40,self.runner.size[1]/2)
	self.label.add_attribute('restart','size',60)
        os.system('shutdown -r now')
