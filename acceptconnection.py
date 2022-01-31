import socket
import sys
import threading
from _thread import *



def server(conn):	
	while 1:
		data2U = conn.recv(1024).decode("utf-8")
		if "#!END!#" in data2U:
			break
		print(data2U)

		
		#f = conn.makefile(mode='rw')#
		#m = f.readline()#
		
		
		
		#f.write(m)#
		#f.flush()#
		
		#conn, addr = s.accept()#
	conn.close()
	s.close()

def client(conn):	
	while 1:
		datasend=input()

		if "#!END!#" in datasend:
			break
		conn.sendall(bytes(datasend+'\n', 'utf-8'))
		#f = conn.makefile(mode='rw')#
		#m = f.readline()#
		
		
		
		#f.write(m)#
		#f.flush()#
		
		#conn, addr = s.accept()#
	conn.close()
	s.close()
if __name__=="__main__":
	HOST = '192.168.1.5'	# finding correct ip using ifconfig/ipconfig
	PORT = 8888	# Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ('Socket created')
	try :
		
		s.bind((HOST,PORT))
		print ('Socket bind complete')
	except socket.error as msg:
		
		print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]) 
		sys.exit()
	try :
		s.listen(10)
		print ('Socket now listening')
	except socket.error as msg:
		
		print('Listening failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]) 
		sys.exit()
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	#display client information
	print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	t1=threading.Thread(target=client, args=(conn,))
	t1.start()
	t2=threading.Thread(target=server, args=(conn,))
	
	t2.start()
#	client(conn)
#	server(conn)
	
