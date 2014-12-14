__author__ = 'richard'
import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from pprint import pprint
from collections import defaultdict
from color import *
from button import Button
from label import Label


import glob
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()


def exit_task():
    label.add_label('example2','Fuck You Jerermy',200,30)
    refresh_menu_screen()


def refresh_menu_screen():
#set up the fixed items on the menu
    screen.fill(white) #change the colours if needed

    button.__render__()
    label.__render__()

    pygame.display.flip()




def main():


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.on_click(pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

	pygame.display.update()


#################### EVERTHING HAS NOW BEEN DEFINED ###########################
#define colours



#set size of the screen
size = width, height = 480, 320
screen = pygame.display.set_mode(size)
button = Button(screen)
label = Label(screen)

button.add_button('exit',exit_task,50,50,100,100)
button.add_attributes('exit','color',red)
button.add_attributes('exit','text','EXIT')
button.add_button('test2',exit_task,200,200,225,225)
button.add_attributes('test2','color',blue)


label.add_label('example','Example Label',50,30)


refresh_menu_screen()  #refresh the menu interface
main() #check for key presses and start emergency exit


