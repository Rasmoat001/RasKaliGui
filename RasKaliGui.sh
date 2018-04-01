#!/bin/bash
echo "Welcome To Kali Gui Installer"
echo "=======____Coded by Rasmoat____======="
echo "---------------------------------------------------------------"
echo "=======____T.me/Rasmaster____======="
echo "---------------------------------------------------------------"
echo "Telegeram @Rasmoat Twitter @Rasmoat97"

echo "facebook https://www.facebook.com/Rasmoat.yaya"
echo "------------------------------------------------------------------------------------------------"
echo Thanks For Your Showing Love @Rasmoat

echo @Rasmaster
echo --------------------------------------------------------------------------------------------------
echo .
echo --------------------------------------------------------------------------------------------------
echo =======================
echo --------------------------------------------------------------------------------------------------

echo "           Available Guis "
echo "1.Xfce Desktop Gui"
echo "2.Gnome Desktop Gui"
echo "3.Gnome Desktop Gui"
echo "4.Lxde Desktop Gui"
echo "----------------------------------------------------------------"

echo "Please Choose the Gui you want to install!"

echo "----------------------------------------------------------------"
echo .
echo Made By: Me :Rasmoat
echo .
set /p input= Type Number -
if %input%==1 goto  A
if %input%==2 goto  B
if %input%==3 goto  C
if %input%==4 goto  D
if %input%==5 goto  E
if %input%==6 goto  F
:A
echo "[+] Installing XFCE4, this will take a while"
apt-get --yes --force-yes install figlet
apt-get update
figlet Xfce Gui
apt-get dist-upgrade -y --force-yes
apt-get --yes --force-yes install kali-desktop-xfce xorg xrdp
echo "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini

:B
echo "[+] Installing Gnome, this will take a while!"
apt-get --yes --force-yes install figlet
apt-get update
figlet Gnome Gui
apt-get dist-upgrade -y --force-yes
apt-get --yes --force-yes install kde-plasma-desktop xorg xrdp
echo "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini

:C
echo "[+] Installing Kde, this will take a while!"
apt-get --yes --force-yes install figlet
apt-get update
figlet Kde Gui
apt-get dist-upgrade -y --force-yes
apt-get --yes --force-yes install kde-plasma-desktop xorg xrdp
echo "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini


:D
echo "[+] Installing Lxde, this will take a while!"
apt-get --yes --force-yes install figlet
apt-get update
figlet Lxde  Gui
apt-get dist-upgrade -y --force-yes
apt-get --yes --force-yes install lxde-core lxde kali-defaults kali-root-login desktop-base
echo "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini

:E
echo "[+] Installing Cinnamon, this will take a while!"
apt-get --yes --force-yes install figlet
apt-get update
figlet Lxde  Gui
apt-get dist-upgrade -y --force-yes
apt-get --yes --force-yes install kali-defaults kali-root-login desktop-base cinnamon
echo "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini

:F
echo "[+] Installing Mate, this will take a while!"
apt-get --yes --force-yes install figlet
apt-get update
figlet Lxde  Gui
apt-get dist-upgrade -y --force-yes#
echo "deb http://repo.mate-desktop.org/debian wheezy main" >> /etc/apt/sources.list && apt-get update
apt-get --yes --quiet --allow-unauthenticated install mate-archive-keyring
apt-get --yes --force-yes install kali-defaults kali-root-login desktop-base mate-desktop-environment-extra
echo "[+] Configuring XRDP to listen on port 3390 (but not starting the service)..."
sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini
