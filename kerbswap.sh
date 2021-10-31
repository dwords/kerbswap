#!/bin/bash 

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Please run Kerswap as root!."
    exit
fi
echo "Kerbswap - Updating made easy."
echo "Updating your kernel!."


 curl "https://raw.githubusercontent.com/dwords/remote-resources/main/mainline/ubuntu-mainline-kernel.sh --output ubuntu-mainline-kernel.sh"

sudo install ubuntu-mainline-kernel.sh /usr/local/bin

sudo ubuntu-mainline-kernel.sh –i

clear

echo "Kernel updated!."
echo "Your system will reboot in (5) minutes, please save any files!..."
sleep 300
reboot 



