from socket import *
import sys
import select 

host ="192.168.0.132"
port =69 
s = socket(AF_INET,SOCK_DGRAM) 
s.bind((host,port)) 

addr = (host,port) 
buf=1024 

data,addr = s.recvfrom(buf) 
print("File Sudah Diterima:",data.strip()) 
f = open(data.strip(),'wb') 

data,addr = s.recvfrom(buf) 
try:
    while(data):
     f.write(data)
     s.settimeout(2)
     data,addr = s.recvfrom(buf) 
except timeout:
    f.close()
    s.close()
    print ("File Sudah Download")
