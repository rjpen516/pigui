__author__ = 'richard'
import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from pprint import pprint
from collections import defaultdict
from pigui.color import *
from pigui.button import Button
from pigui.label import Label
from pigui.CanvasRunner import CanvasRunner
from home import Home


program = CanvasRunner()


home = Home('homescreen')
program.add_canvas('homescreen',home)
program.main()
