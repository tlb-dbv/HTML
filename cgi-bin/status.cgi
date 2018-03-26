#!/usr/bin/python
#-*- coding: utf8-*-
import os

var=raw_input()
stat=var.split("=")[0]

print("content-type: text/html")
print("")

if stat == "dns":
	os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 status |grep Active > dns.txt")
	f = open("dns.txt", "r")
	pagina = f.read()
	f.close()
	print(pagina)
elif stat == "nag":
	os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 status |grep Active > nag.txt")
	f = open("nag.txt", "r")
	pagina = f.read()
	f.close()
	print(pagina)
elif stat == "fir":
	os.system("sudo /var/www/html/cgi-bin/stf.sh")
	f = open("fir.txt", "r")
	pagina = f.read()
	f.close()
	print(pagina)
elif stat == "VOLT":
    f = open("menu.html", "r")
    pagina = f.read()
    f.close()
    print(pagina)
