#!/usr/bin/python
#-*- coding utf8 -*-

var=raw_input()
clic=var.split("=")[0]

if clic == "exc":
	os.system("sudo crone.sh")
elif clic == "stat":
	os.system("sudo cronl.sh")
	print("content-type: text/html")
	print("")
	f = open("cron.txt", "r")
	stats = f.read()
	f.close()
	print(stats)
elif clic == "tare":
	os.system("sudo crona.sh")
