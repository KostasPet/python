sudo apt-get update
sudo apt-get install oracle-java8-jdk
mkdir /home/pi/.jagex_cache_32
mkdir /home/pi/.jagex_cache_32/runescape
mkdir /home/pi/.jagex
mkdir /home/pi/.jagex/runescape
mkdir /home/pi/.jagex/runescape/bin
mkdir /home/pi/.jagex/runescape/images
cd /home/pi/.jagex/runescape/bin
wget https://github.com/MrHDR/RaspberryPi/raw/master/Rsinstall/jagexappletviewer.jar
cd /home/pi/.jagex/runescape/images
wget https://raw.githubusercontent.com/MrHDR/RaspberryPi/master/Rsinstall/jagexappletviewer.png
wget https://raw.githubusercontent.com/MrHDR/RaspberryPi/master/Rsinstall/jagexappletvieweros.png
cd /home/pi/Desktop
wget https://github.com/MrHDR/RaspberryPi/raw/master/Rsinstall/Rs3.desktop
wget https://github.com/MrHDR/RaspberryPi/raw/master/Rsinstall/OSRS.desktop
