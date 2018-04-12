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

print "   Available Guis! "
print "1. Xfce Desktop Gui"
print "2. Gnome Desktop Gui"
print "3. Kde Desktop Gui"
print "4. Lxde Desktop Gui"
print "5. Cinnamon Desktop Gui"
print "6. Mate Desktop Gui"
print "7. Update Script! "
print "0. Exit Installer"
print "======================="

print "----------------------------------------------------------------"

print "Please Choose the Gui you want to install!"

print "----------------------------------------------------------------"
print ""
print "Made By::Rasmoat!"
print ""
choice = raw_input("Type Number :-: ")

if choice == "1":
    print "[+] Installing XFCE4, this will take a while"
    os.system (" apt-get --yes --force-yes install figlet")
    os.system(" apt-get update")
    os.system (" figlet Xfce Gui")
    os.system (" apt-get dist-upgrade -y --force-yes")
    os.system (" apt-get --yes --force-yes install kali-desktop-xfce xorg xrdp")
    print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
    os.system (" sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
    print (" Xfce Gui Succesfully Installed!")
    sys.exit()
elif choice == "2":
    print "[+] Installing Gnome, this will take a while!"
    os.system (" apt-get --yes --force-yes install figlet")
    os.system(" apt-get update")
    os.system (" figlet Gnome Gui")
    os.system (" apt-get dist-upgrade -y --force-yes")
    os.system (" apt-get --yes --force-yes install kde-plasma-desktop xorg xrdp")
    print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
    os.system (" sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
    print ("Gnome Gui Installed Succesfully!")
    sys.exit()
elif choice == "3":
    print "[+] Installing Kde, this will take a while!"
    os.system (" apt-get --yes --force-yes install figlet")
    os.system(" apt-get update")
    os.system (" figlet Kde Gui")
    os.system (" apt-get dist-upgrade -y --force-yes")
    os.system (" apt-get --yes --force-yes install kde-plasma-desktop xorg xrdp")
    print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
    os.system (" sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
    print (" Kde Gui Installed Succesfully!")
    sys.exit()
elif choice == "4":
    print "[+] Installing Lxde, this will take a while!"
    os.system (" apt-get --yes --force-yes install figlet")
    os.system(" apt-get update")
    os.system (" figlet Lxde  Gui")
    os.system (" apt-get dist-upgrade -y --force-yes")
    os.system (" apt-get --yes --force-yes install lxde-core lxde kali-defaults kali-root-login desktop-base")
    print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
    os.system (" sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
    print (" Lxde Gui Installed Succesfully!")
    sys.exit()
elif choice == "5":
    print "[+] Installing Cinnamon, this will take a while!"
    os.system (" apt-get --yes --force-yes install figlet")
    os.system(" apt-get update")
    os.system (" figlet Cinnamon  Gui")
    os.system (" apt-get dist-upgrade -y --force-yes")
    os.system (" apt-get --yes --force-yes install kali-defaults kali-root-login desktop-base cinnamon")
    print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
    os.system (" sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
    print (" Cinnamon Gui Succesfully Installed!")
    sys.exit()
elif choice == "6":
    print "[+] Installing Mate, this will take a while!"
    os.system ("apt-get --yes --force-yes install figlet")
    os.system("apt-get update")
    os.system ("figlet Mate  Gui")
    os.system ("apt-get dist-upgrade -y --force-yes")
    os.system (" echo 'deb http://repo.mate-desktop.org/debian wheezy main' >> /etc/apt/sources.list ")
    os.system("apt-get update")
    os.system ("apt-get --yes --quiet --allow-unauthenticated install mate-archive-keyring")
    os.system ("apt-get --yes --force-yes install kali-defaults kali-root-login desktop-base mate-desktop-environment-extra")
    print "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
    os.system ("sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
    print ( " Mate Gui Succesfully Installed!")
    sys.exit()
elif choice == "0":
    print "Good Bye :("
    sys.exit()
elif choice == "7":
    print "[+] Updating Script, Please Wait!"
    os.system(" git clone https://github.com/Rasmoat001/RasKaliGui.git")
    print "[+] Script Updated Succesfully!, Open Script Again!"
    print "=============------------------==================="
    sys.exit()
else:
    print "You have Entered an Incorrect Number,Please Restart Program and Select A Good Choice!"
    sys.exit()
#def Xfce():
#def Gnome():
#def Kde():
#def Lxde():
#def Cinnamon():
#def Mate():
