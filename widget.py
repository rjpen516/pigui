from collections import defaultdict

__author__ = 'richard'



class Widget(object):
    def __init__(self):
        self.attributes = defaultdict(dict)

    def __setup__(self):
        pass

    def __render__(self):
        pass

    def add_attribute(self,name,type,value):
        self.attributes[name][type] = value

    def set_render_queue(self,queue):
        print "Superclass Widget"
        self.render_queue = queue

    def set_runner(self, runner):
        self.runner = runner