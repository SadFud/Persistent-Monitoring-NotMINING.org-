#!/bin/bash
wget "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt" -O /tmp/nm1;
sed '/^#/ d' /tmp/nm1 | cut -d' ' -f2 > /tmp/nm2
sed '/^\s*$/d' /tmp/nm2 > blacklist.txt
rm /tmp/nm1
rm /tmp/nm2
clear
echo "[+] Blacklist actualizada"
