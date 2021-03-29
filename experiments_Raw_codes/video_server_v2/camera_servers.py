import socket, cv2, pickle, struct
import imutils # pip3 install imutils
import threading
import cv2


class camera_server:
    def __init__(self, publisher_camera_ip='127.0.0.1', publisher_camera_port=9997, socket_server_host_ip=None, socket_server_port=9996):
        
        self.frame=None

        # make client of publisher camera
        self.video_stream_thread = threading.Thread(target=self.start_video_stream, args=(publisher_camera_ip,publisher_camera_port))
        
        # socket_server
        if socket_server_host_ip == None:  # if user enters the ip for socket server
            self.socket_server_host_ip=socket.gethostbyname(socket.gethostname())
        else: 
            self.socket_server_host_ip = socket_server_host_ip

        self.socket_server_port = socket_server_port # if user enters the port for socket server
        self.make_sock_server(self.socket_server_host_ip,self.socket_server_port)  # start socket server        
        self.sock_server_thread= threading.Thread(target=self.start_sock_server)
        
        #websocket_server
        self.publisher_camera_ip=publisher_camera_ip
        self.publisher_camera_port=publisher_camera_port
        
        self.websock_server_thread=threading.Thread(target=self.websocket_server, args=())

        # start servers in thread
        self.video_stream_thread.start()
        self.sock_server_thread.start()
        #self.websock_server_thread.start()

    def start_video_stream(self,publisher_camera_ip, port):       # start streaming from camera , publisher_camera_ip= ip of camera , port= at which it is publishing
        
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        client_socket.connect((publisher_camera_ip,port))
        print("connected to publishing camera @", publisher_camera_ip,"  port: ", port)
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            while len(data) < payload_size:
                packet = client_socket.recv(4*1024) 
                if not packet: break
                data+=packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q",packed_msg_size)[0]
            
            while len(data) < msg_size:
                data += client_socket.recv(4*1024)
            frame_data = data[:msg_size]
            data  = data[msg_size:]
            self.frame = pickle.loads(frame_data)
            header="RECEIVING VIDEO FROM " + str(publisher_camera_ip) + ' : ' + str( port)
            cv2.imshow(header,self.frame)
            #print("receiving data from publisher camera")
            key = cv2.waitKey(1) & 0xFF
            #print(data)
            if key  == ord('q'):
                break
        client_socket.close()
        print("closing connection with publishing camera @", publisher_camera_ip,"  port: ", port)

    
    def websocket_server(self):         # start websocket server to serve camera stream to clients (UI display) using websockets
        pass
    
    def make_sock_server(self,sock_server_host_ip, ss_port):  # make socket server to serve camera stream  to clients (AI_node) using sockets
        
        self.sock_sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        """  code block for reusable address of port for serving  """
        # Get the old state of the SO_REUSEADDR option
        old_state = self.sock_sever.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) 

        # Enable the SO_REUSEADDR option
        self.sock_sever.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        new_state = self.sock_sever.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )
        #print ("New sock state:",new_state)
        """ code block ended """
        
        #print('HOST IP:',self.sock_server_host_ip)
        #print('port number: ', self.port)
        
        socket_address = (sock_server_host_ip,ss_port)
        self.sock_sever.bind(socket_address)
        self.sock_sever.listen()
        print("socket server established and Listening for clients at ",socket_address)

    def sock_server_frame_distributor(self, addr,client_sock):  # distribute video frames to client
        try:
            print('CLIENT {} CONNECTED!'.format(addr))
            if client_sock:
                while True:
                    a = pickle.dumps(self.frame)
                    message = struct.pack("Q",len(a))+a
                    client_sock.sendall(message)
                    
        except Exception :
            print(f"CLINET {addr} DISCONNECTED")
            pass

    def start_sock_server(self):    # function to run socket server handler
        print("starting socket server at ",self.socket_server_host_ip, "  port : ",self.socket_server_port)
        while True:
            client_sock,addr = self.sock_sever.accept()
            print("got client at address : ",addr)     
            thread = threading.Thread(target=self.sock_server_frame_distributor, args=(addr,client_sock))
            thread.start()
            print("TOTAL CLIENTS ",threading.activeCount() - 2) # edited here because one thread is already started before


if __name__ == '__main__':
    j= camera_server()
