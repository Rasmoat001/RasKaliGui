#!/bin/bash
echo "                                   [------------------------------------]"
echo "                                      Welcome To Kali Gui Installer"
echo "                                   [------------------------------------]"
echo "                                   =======____Coded by Rasmoat____======"
echo "                                   =======____Keep_Wondering___======="
echo "                                      Telegeram @Rasmoat Twitter @Rasmoat97"
echo "                             =======____facebook fb.me/Rasmoat.yaya_____======="
echo "------------------------------------------------------------------------------------------------"
echo "Thanks For Your Showing Love @Rasmoat"

echo "@Rasmaster"
echo --------------------------------------------------------------------------------------------------
echo .
echo --------------------------------------------------------------------------------------------------
echo =======================
echo --------------------------------------------------------------------------------------------------

echo "   Available Guis "
echo "1. Xfce Desktop Gui"
echo "2. Gnome Desktop Gui"
echo "3. Gnome Desktop Gui"
echo "4. Lxde Desktop Gui"
echo "5. Cinnamon Desktop Gui"
echo "6. Mate Desktop Gui"
echo "0. Exit Installer"
echo "----------------------------------------------------------------"

echo "Please Choose the Gui you want to install!"

echo "----------------------------------------------------------------"
echo .
echo Made By: Me :Rasmoat
echo .
echo "Type Number -:"

read input
if [ $input == 1 ]; then
goto  A
fi
if [ $input == 2 ]; then
goto  B
fi
if [ $input == 3 ]; then
goto C
fi
if [ $input == 4 ]; then
goto D
fi
if [ $input == 5 ]; then
goto E
fi
if [ $input == 6 ]; then
goto F
fi
if [ $input == 0 ]; then
exit 0
fi

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
fi
