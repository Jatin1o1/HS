# This code will run on the publisher camera, it will send video to broadcast server
# Lets import the libraries
import imutils # pip3 install imutils
import socket, cv2, pickle, struct

import cv2
from mqtt_pub import Mqtt_publish


class Video_Publisher:
	def __init__(self, ip=socket.gethostbyname(socket.gethostname()), port=7777):
		self.host_ip= ip
		self.port=port
		

	def make_server(self):
		self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		# Get the old state of the SO_REUSEADDR option
		old_state = self.server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) 

		# Enable the SO_REUSEADDR option
		self.server_socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
		new_state = self.server_socket.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )
		#print ("New sock state:",new_state)
				
		print('HOST IP:',self.host_ip)

		
		while True:
			socket_address = (self.host_ip,self.port)
			result_of_check = self.server_socket.connect_ex(socket_address)  # check weather port is open(0) or not(1) , if not increase port number by 1

			if result_of_check == 1:  # port is closed
				self.port += 1  # increase binding port number by 1
			else:
				break

		socket_address = (self.host_ip,self.port)
		print("socket_address is ", socket_address)
		self.server_socket.bind(socket_address)
		self.server_socket.listen()
		Mqtt_publish("video_publishers", ("camera publishing at address:"+ str(socket_address) )) 

	
	def Start_stream(self):
		self.make_server() 

		while True:
			self.video_stream()

	
	def video_stream(self):
		print("startiing video stream")
		client_socket,addr = self.server_socket.accept()
		camera = True
		if camera == True:
			vid = cv2.VideoCapture(0)
		else:
			vid = cv2.VideoCapture('videos/video1.mp4')
		try:
			print('CLIENT {} CONNECTED!'.format(addr))
			if client_socket:
				while(vid.isOpened()):
					img,frame = vid.read()

					frame  = imutils.resize(frame,width=320)
					a = pickle.dumps(frame)
					message = struct.pack("Q",len(a))+a
					client_socket.sendall(message)
					cv2.imshow("TRANSMITTING TO broadcast SERVER",frame)
					key = cv2.waitKey(1) & 0xFF
					if key ==ord('q'):
						client_socket.close()
						break

		except:
			print(f"broadcast SERVER {addr} DISCONNECTED")
			pass
	

j= Video_Publisher()
j.Start_stream()