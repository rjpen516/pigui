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
    print "I should exit"


def refresh_menu_screen():
#set up the fixed items on the menu
    screen.fill(white) #change the colours if needed

    #make an example label
    #title_font=pygame.font.Font(None,34)
    #label=title_font.render("Example Label", 1, (blue))
    #screen.blit(label,(5, 15))

    button.__render__()
    label.__render__()


	#play=pygame.image.load("play.tiff")
	# draw the main elements on the screen
	#screen.blit(play,(20,80))
	#screen.blit(pause,(80,80))
	#pygame.draw.rect(screen, red, (8, 70, 304, 108),1)
	#pygame.draw.line(screen, red, (8,142),(310,142),1)
	#pygame.draw.rect(screen, cream, (10, 143, 300, 33),0)
	#screen.blit(refresh,(270,70))
	#screen.blit(previous,(10,180))
	#screen.blit(next,(70,180))
    #    screen.blit(vol_down,(130,180))
	#screen.blit(vol_up,(190,180))
	#screen.blit(mute,(250,180))
    #    screen.blit(exit,(270,5))
	#screen.blit(radio,(2,1))
    #pygame.draw.rect(screen, green, (0,0,width,height),3)

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


