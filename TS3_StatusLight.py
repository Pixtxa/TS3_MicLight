#Pixtxa added the following Lines
import socket
import sys
host = "192.168.3.14" #IP of MagicHome LED-Stripe-Controller

#Original sample-code is following
from ts3plugin import ts3plugin

import ts3defines, pytson, ts3client
import os
from configparser import ConfigParser

from PythonQt.QtGui import QDialog, QHBoxLayout, QVBoxLayout, QTreeView, QSortFilterProxyModel, QPushButton, QToolButton, QSpacerItem, QSizePolicy, QSpinBox, QLabel, QLineEdit, QIcon
from PythonQt.QtCore import Qt, QAbstractItemModel, QModelIndex

#Pixtxa deleted some lines. It also work's without them.

class eventlog(ts3plugin):
    requestAutoload = True
    name = "eventlog"
    version = "1.0.0"
    apiVersion = 21
    author = "Thomas \"PLuS\" Pathmann"
    description = "This plugin shows all available events in a log. Might be helpfull for plugin deveolopers."
    offersConfigure = False
    commandKeyword = ""
    infoTitle = None
    menuItems = [(ts3defines.PluginMenuType.PLUGIN_MENU_TYPE_GLOBAL, 0, "Eventlog", os.path.join("ressources", "octicons", "list-unordered.svg.png"))]
    hotkeys = []

    def __init__(self):
        self.log = None
        self.cfg = ConfigParser()

        #set default values
        self.cfg.add_section("general")
        self.cfg.set("general", "maximumEvents", "100")
        self.cfg.set("general", "height", "200")
        self.cfg.set("general", "width", "350")

        cfgpath = pytson.getConfigPath("eventlog.conf")
        if os.path.isfile(cfgpath):
            self.cfg.read(cfgpath)

    def stop(self):
        with open(pytson.getConfigPath("eventlog.conf"), "w") as f:
            self.cfg.write(f)

    def showLog(self, parent):
        if not self.log:
            self.log = EventlogDialog(self.cfg["general"], parent)

        self.log.show()
        self.log.raise_()
        self.log.activateWindow()

    def onMenuItemEvent(self, schid, atype, menuItemID, selectedItemID):
        if menuItemID == 0:
            self.showLog(None)

    def menuCreated(self):
        pass #just here to not be triggered in __getattr__

    def callback(self, name, *args):
        #Pixtxa added the following code here:
        global r,g,b,w,speaking,muted                                                     #Variables from the last call are deleted, so I used global ones
        changed = False                                                                   #Init tracking variable
        if name == "onTalkStatusChangeEvent":                                             #Track how many people are speaking
            changed = True                                                                  #Send data to the controller at end of function
            if args[1] == 1:                                                                #If someone starts speaking
                speaking +=1                                                                  #one more person is speaking,
            else:                                                                           #if someone stops speaking
                speaking -=1                                                                  #one person less is speaking
                if speaking < 0:                                                           #if negative amount of people are speaking (usually if Script was started while someone was speaking)
                    speaking = 0                                                              #reset counter, because it makes no sense
        if name == "onClientSelfVariableUpdateEvent" and args[1] == 4:                    #Track if you are speaking
            changed = True                                                                  #Send data to the controller at end of function
            if args[3] == "1":                                                              #If you started speaking
                g = 255                                                                       #Set green channel on
                speaking -=1                                                                  #remove that yourself are speaking in your channel
            else:                                                                          #If you stopped speaking
                g = 0                                                                         #Set green channel off
                speaking +=1                                                                  #add the removed you that was speaking in your channel
        if speaking > 0:                                                                  #if someone is speaking, that is not you
            b = 255                                                                         #set blue channel on
        else:                                                                             #if the others aren't speaking
            b = 0                                                                           #set blue channel on
        if name == "onClientSelfVariableUpdateEvent" and (args[1] == 5 or args[1] == 6):  #Track if you muted your mic or speakers
            changed = True                                                                  #Send data to the controller at end of function                
            if args[3] == "1":                                                              #If you muted yourself
                muted +=1                                                                     #add that mic or speaker is muted
                if muted > 2:                                                                 #limit amount of mutable devices (shouldn't be possible to get the variable to that value, but better be safe)
                    muted = 2                                                                   #Mic + Speakers = 2
            else:                                                                           #If you unmuted yourself
                muted -=1                                                                     #remove that mic or speaker is muted
                if muted < 0:                                                                 #if negative amount of devices is muted (usually if Script was started while you were muted)
                    muted = 0                                                                   #reset counter, because it makes no sense
            if muted > 0 :                                                                  #If mic or speakers are muted
                r = 255                                                                       #Set red channel on 
            else:                                                                           #If no Device is muted
                r = 0                                                                         #Set red channel off
        if changed:                                                                       #If there may be a change
            if (r>0 or g>0 or b>0):                                                         #If one rgb-channel is on
                w=0                                                                           #Set white channel off
            else:                                                                           #If all rgb-channels are off
                w=255                                                                         #Set white channel on
            Check = (0x4F+r+g+b+w)%256                                                      #calculate checksum
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           #start connection
            s.settimeout(0.25)                                                              #use Timeout, so TeamSpeak wouldn't crash if stripe is offline
            s.connect((host, 5577)) #Verbindung zum Stripe                                  #connect to stripe
            s.send((chr(0x31)+chr(r)+chr(g)+chr(b)+chr(w)+chr(0x0f)+chr(0x0f)+chr(Check)).encode('mbcs')) #send data to stripe
            s.close() #Verbindungsende                                                      #end connection to stripe
        #And here follows the remaining samplecode
        if self.log:
            self.log.callback(name, *args)

    def __getattr__(self, name):
        return (lambda *args: self.callback(name, *args))
