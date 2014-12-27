__author__ = 'richard'


class Clickable(object):
    def __init__(self):
        pass

    def on_click(self,x,y):
        print "Click on (%d,%d)" %(x,y)