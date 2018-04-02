import sys
import argparse
import os
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep

print "                                   [------------------------------------]"
print "                                      Welcome To Kali Gui Installer"
print "                                   [------------------------------------]"
print "                                   =======____Coded by Rasmoat____======"
print "                                   =======____Keep_Wondering___======="
print "                                      Telegeram @Rasmoat Twitter @Rasmoat97"
print "                             =======____facebook fb.me/Rasmoat.yaya_____======="
print "------------------------------------------------------------------------------------------------"
print "Thanks For Your Showing Love @Rasmoat"

print "@Rasmaster"
print "--------------------------------------------------------------------------------------------------"
print ""
print "--------------------------------------------------------------------------------------------------"
print "======================="
print "--------------------------------------------------------------------------------------------------"

print "   Available Guis "
print "1. Xfce Desktop Gui"
print "2. Gnome Desktop Gui"
print "3. Kde Desktop Gui"
print "4. Lxde Desktop Gui"
print "5. Cinnamon Desktop Gui"
print "6. Mate Desktop Gui"
print "0. Exit Installer"
print "======================="

print "----------------------------------------------------------------"

print "Please Choose the Gui you want to install!"

print "----------------------------------------------------------------"
print ""
print "Made By::Rasmoat"
print ""

input = raw_input("Type Number :-: ")
clearScr()
if choice == "1":
    Xfce()
elif choice == "2":
    Gnome()
elif choice == "3":
    Kde()
elif choice == "4":
    Lxde()
elif choice == "5":
    Cinnamon()
elif choice == "6":
    Mate()
elif choice == "0":
    print "Good Bye :("
    sys.exit()
else:
            print "You have Entered an Incorrect Number,Please Select A Good Choice!"

def Xfce():
    print""
print "[+] Installing XFCE4, this will take a while"
os.system ("apt-get --yes --force-yes install figlet")
os.system("apt-get update")
os.system ("figlet Xfce Gui")
os.system ("apt-get dist-upgrade -y --force-yes")
os.system ("apt-get --yes --force-yes install kali-desktop-xfce xorg xrdp")
print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")

def Gnome():
    print ""
print "[+] Installing Gnome, this will take a while!"
os.system ("apt-get --yes --force-yes install figlet")
os.system("apt-get update")
os.system ("figlet Gnome Gui")
os.system ("apt-get dist-upgrade -y --force-yes")
os.system ("apt-get --yes --force-yes install kde-plasma-desktop xorg xrdp")
print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")

def Kde():
    print ""
print "[+] Installing Kde, this will take a while!"
os.system ("apt-get --yes --force-yes install figlet")
os.system("apt-get update")
os.system ("figlet Kde Gui")
os.system ("apt-get dist-upgrade -y --force-yes")
os.system ("apt-get --yes --force-yes install kde-plasma-desktop xorg xrdp")
print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")


def Lxde():
    print ""
print "[+] Installing Lxde, this will take a while!"
os.system ("apt-get --yes --force-yes install figlet")
os.system("apt-get update")
os.system ("figlet Lxde  Gui")
os.system ("apt-get dist-upgrade -y --force-yes")
os.system ("apt-get --yes --force-yes install lxde-core lxde kali-defaults kali-root-login desktop-base")
print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")

def Cinnamon():
    print ""
print "[+] Installing Cinnamon, this will take a while!"
os.system ("apt-get --yes --force-yes install figlet")
os.system("apt-get update")
os.system ("figlet Lxde  Gui")
os.system ("apt-get dist-upgrade -y --force-yes")
os.system ("apt-get --yes --force-yes install kali-defaults kali-root-login desktop-base cinnamon")
print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")

def Mate():
    print ""
print "[+] Installing Mate, this will take a while!"
os.system ("apt-get --yes --force-yes install figlet")
os.system("apt-get update")
os.system ("figlet Lxde  Gui")
os.system ("apt-get dist-upgrade -y --force-yes")
print "deb http://repo.mate-desktop.org/debian wheezy main" >> /etc/apt/sources.list && os.system("apt-get update")
os.system ("apt-get --yes --quiet --allow-unauthenticated install mate-archive-keyring")
os.system ("apt-get --yes --force-yes install kali-defaults kali-root-login desktop-base mate-desktop-environment-extra")
print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
