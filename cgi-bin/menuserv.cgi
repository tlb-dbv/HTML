#!/usr/bin/python
#-*- coding utf8 -*-

var=raw_input()
acao=var.split("=")[0]

import os

print("content-type: text/html")
print("")

if acao == "DNSI":
    os.system("date >> /var/www/html/cgi-bin/serv.log")
    os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 start &>> /var/www/html/cgi-bin/serv.log")
    print("<h1>Iniciou</h1>")
elif acao == "DNSP":
    os.system("date >> /var/www/html/cgi-bin/serv.log")
    os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 stop &>> /var/www/html/cgi-bin/serv.log")
    print("<h1>Parou</h1>")
elif acao == "DNSR":
    os.system("date >> /var/www/html/cgi-bin/serv.log")
    os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 restart &>> /var/www/html/cgi-bin/serv.log ")
    print("<h1>Reiniciou</h1>")
elif acao == "NAGI":
    os.system("date >> /var/www/html/cgi-bin/serv.log")
    os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 start& >> /var/www/html/cgi-bin/serv.log")
    print("<h1>Iniciou</h1>")
elif acao == "NAGP":
    os.system("date >> /var/www/html/cgi-bin/serv.log")
    os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 stop &>> /var/www/html/cgi-bin/serv.log")
    print("<h1>Parou</h1>")
elif acao == "NAGR":
    os.system("date >> /var/www/html/cgi-bin/serv.log")
    os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 restart &>> /var/www/html/cgi-bin/serv.log ")
    print("<h1>Reiniciou</h1>")
elif acao == "FIRI":
	os.system("sudo /usr/lib/cgi-bin/regras.sh")
	print("<h1>Iniciou</h1>")
elif acao == "FIRP":
	os.system("sudo /usr/lib/cgi-bin/panico.sh")
	print("<h1>Parou</h1>")
elif acao == "FIRR":
	os.system("sudo /usr/lib/cgi-bin/panico.sh")
	os.system("sudo /usr/lib/cgi-bin/regras.sh")
	print("<h1>Reiniciou</h1>")
elif acao == "VOLT":
	f = open("menu.html", "r")
	pagina = f.read()
	f.close()
	print(pagina)
