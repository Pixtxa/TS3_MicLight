#Pixtxa added the following Lines
import socket
import sys
host = "192.168.3.14" #IP of MagicHome LED-Stripe-Controller

#Colors
rsend = 0
gsend = 255
bsend = 0
wsend = 0

ridle = 0
gidle = 0
bidle = 0
widle = 255

rmute = 255
gmute = 0
bmute = 0
wmute = 0



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
        global muted
        if name == "onClientSelfVariableUpdateEvent":
            if args[1] == 4:
                if args[3] == "1": #If speaking, set light color to send
                    muted = 0
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    s.connect((host, 5577))
                    Check = (0x4F+rsend+gsend+bsend+wsend)%256
                    s.send((chr(0x31)+chr(rsend)+chr(gsend)+chr(bsend)+chr(wsend)+chr(0x0f)+chr(0x0f)+chr(Check)).encode('mbcs'))
                    s.close()
                elif muted == 0: #If not speaking and not muted, set light color to idle
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    s.connect((host, 5577))
                    Check = (0x4F+ridle+gidle+bidle+widle)%256
                    s.send((chr(0x31)+chr(ridle)+chr(gidle)+chr(bidle)+chr(widle)+chr(0x0f)+chr(0x0f)+chr(Check)).encode('mbcs'))
                    s.close()
            if args[1] == 5:
                if args[3] == "1": #If speaking, set light color to mute
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    s.connect((host, 5577))
                    Check = (0x4F+rmute+gmute+bmute+wmute)%256
                    s.send((chr(0x31)+chr(rmute)+chr(gmute)+chr(bmute)+chr(wmute)+chr(0x0f)+chr(0x0f)+chr(Check)).encode('mbcs'))
                    s.close()
                    muted = 1
                else: #If not muted, set light color to idle
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    s.connect((host, 5577))
                    Check = (0x4F+ridle+gidle+bidle+widle)%256
                    s.send((chr(0x31)+chr(ridle)+chr(gidle)+chr(bidle)+chr(widle)+chr(0x0f)+chr(0x0f)+chr(Check)).encode('mbcs'))
                    s.close()
                    muted = 0
        #And here follows the remaining samplecode
        if self.log:
            self.log.callback(name, *args)

    def __getattr__(self, name):
        return (lambda *args: self.callback(name, *args))
