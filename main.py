'''
Created on Jul 24, 2012

@author: Admin
'''


from fullscreenwrapper2 import *
import android

import datetime
import os
import pathhelpers
import sys
import time

droid = android.Android()


# Main Screen Class
class MainScreen(Layout):
    def __init__(self):
        #initialize your class data attributes
        
        #load & set your xml
        super(MainScreen,self).__init__(pathhelpers.read_layout_xml("main.xml"),"Odoo")

    def on_show(self):
        #initialize your layout views on screen_show
        self.views.logo.src = pathhelpers.get_drawable_pathname("logo.png")
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.close_out))
    def close_out(self,view,event ):
        FullScreenWrapper2App.close_layout()
        
    
        
    def on_close(self):
        pass

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
    
