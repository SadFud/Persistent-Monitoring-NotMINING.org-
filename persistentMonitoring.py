# -*- coding: utf-8 -*-
import urllib
import psutil
import os
import time
import sys
from termcolor import colored

os.system("bash ./update.sh")

contenido=""
try:
	bl = open("blacklist.txt", "r")
	contenido = bl.readlines()
	print colored('[+] Blacklist leida correctamente', 'green')
except Exception as e:
	print colored('[+] Error al leer la blacklist', 'red')

while True:
	cpu = psutil.cpu_percent()
	time.sleep( 1 )
	if cpu > 40.0:

			cpu = psutil.cpu_percent()
			os.system('netstat > net.html')
			scan = "net.html"
			lines = urllib.urlopen(scan).read()
			search = lines.find('coinhive')
			search1 = lines.find('rs-solution.de')
			search2 = lines.find('ns3033653.ip-164')
			search3 = lines.find('104.25.6.31')
			search4 = lines.find('104.24.104.76')
			search5 = lines.find('104.18.55.211')
			search6 = lines.find('104.27.185.32')
			search7 = lines.find('ns546545.ip-158-6')
			search8 = lines.find('beta00.cortacoin')
			search9 = lines.find('mail.aba.ae')
			search10 = lines.find('104.31.93.36')
			search11 = lines.find('104.31.92.36')

			if search != -1:
				print colored('[/!\] Mining with Coinhive', 'red')

			elif search1 != -1:
				print colored('[/!\] Mining with gustaver.ddns.net', 'red')

			elif search2 != -1:
				print colored('[/!\] Mining with pon.ewtuyytdf45.com', 'red')

			elif search3 != -1:
				print colored('[/!\] Mining with crypto-loot.com', 'red')

			elif search4 != -1:
				print colored('[/!\] Mining with mepirtedic.com', 'red')

			elif search5 != -1:
				print colored('[/!\] Mining with aster18cdn.nl', 'red')

			elif search6 != -1:
				print colored('[/!\] Mining with cdn.whysoserius.club', 'red')

			elif search7 != -1:
				print colored('[/!\] Mining with gtg02.bestsecurepractice.com', 'red')

			elif search8 != -1:
				print colored('[/!\] Mining with beta00.cortacoin.com', 'red')

			elif search9 != -1:
				print colored('[/!\] Mining with "mail.aba.ae" used by: freecontent.*, hashing.win, webassembly.stream, coinimp.com...', 'red')

			elif search10 != -1:
				print colored('[/!\] Mining with crypto-loot.com', 'red')

			elif search11 != -1:
				print colored('[/!\]Mining with crypta-loot.com', 'red')
			else:
				for web in contenido:
					test = str(web.strip())
					if (lines.find(test) != -1):
						print colored('[/!\] Mining with ' + test, 'red')


			time.sleep( 10 )
