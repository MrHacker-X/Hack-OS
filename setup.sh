#created by MrHacker-X; give me credit if you're using any part of this script.
#bin/bash
clear
bash main/banner.sh
pkg install tor -y
rm -rf /data/data/com.termux/files/usr/etc/tor
rm /data/data/com.termux/files/usr/etc/tor
mkdir /data/data/com.termux/files/usr/etc/tor
cp torrc /data/data/com.termux/files/usr/etc/tor
clear
bash main/banner.sh
echo
echo
cd main;chmod +x *;cd ..;cd core;chmod +x *;cd ..;cd pass;chmod +x *
termux-setup-storage
cd $HOME
pkg install python -y
pkg install python2 -y
pkg install wget -y
pip install lolcat
pip install --upgrade pip
pip3 install requests --upgrade
pip3 install requests[socks]
pip3 install stem
pip3 install instagram-py
cd $HOME
wget -O ~/instapy-config.json "https://git.io/v5DGy"
cd $HOME/Hack-OS
bash main/done.sh
