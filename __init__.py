from kivy.uix.boxlayout import BoxLayout
from kivy.event import EventDispatcher

class Control(BoxLayout,EventDispatcher):
    def __init__(self,*args,**kwargs):
        self.register_event_type('on_test')
        super(Control,self).__init__(**kwargs)
    def get(self,a):
        self.dispatch('on_test',a)
    def on_test(self,a):
        pass

