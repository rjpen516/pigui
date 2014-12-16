__author__ = 'richard'



class Widget(object):
    def __init__(self):
        pass

    def __setup__(self):
        pass

    def __render__(self):
        pass

    def set_render_queue(self,queue):
        print "Superclass Widget"
        self.render_queue = queue

    def set_runner(self, runner):
        self.runner = runner