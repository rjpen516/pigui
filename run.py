__author__ = 'richard'
import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
import glob
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
pygame.init()


#define function that checks for mouse location
def on_click():
	click_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
	#check to see if exit has been pressed
	if 270 <= click_pos[0] <= 320 and 10 <= click_pos[1] <=50:
		print "You pressed exit"
		button(0)


#define action on pressing buttons
def button(number):
	print "You pressed button ",number
	if number == 0:    #specific script when exiting
		pass
        #do something with the screen or handle a task


def refresh_menu_screen():
#set up the fixed items on the menu
	screen.fill(white) #change the colours if needed
	font=pygame.font.Font(None,24)
	title_font=pygame.font.Font(None,34)
	label=title_font.render("MPC RADIO", 1, (blue))
	label2=font.render("Streaming Internet Radio", 1, (red))
	screen.blit(label,(105, 15))
	screen.blit(label2,(88, 45))
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
	pygame.draw.rect(screen, green, (0,0,width,height),3)

	pygame.display.flip()

def main():
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                #print "screen pressed" #for debugging purposes
                                #pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                #print pos #for checking
                                #pygame.draw.circle(screen, white, pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
                                on_click()

	pygame.display.update()


#################### EVERTHING HAS NOW BEEN DEFINED ###########################

#set size of the screen
size = width, height = 480, 320
screen = pygame.display.set_mode(size)

#define colours
blue = 26, 0, 255
cream = 254, 255, 25
black = 0, 0, 0
white = 255, 255, 255
yellow = 255, 255, 0
red = 255, 0, 0
green = 0, 255, 0
refresh_menu_screen()  #refresh the menu interface
main() #check for key presses and start emergency exit


