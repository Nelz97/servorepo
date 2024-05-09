import threading
import socket

class Server(threading.Thread):
    def __init__(self):
        super().__init__()
        self.rcv_msg = None
        self.TCP_IP = '192.168.1.121'  # Replace with your server's IP address
        self.TCP_PORT = 2206  # Choose the same port number as used in the client script
        self.BUFFER_SIZE = 1024
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.TCP_IP, self.TCP_PORT))
        self.server_socket.listen(1)  # Listen for incoming connections
        print("Server started. Waiting for connections...")

    def run(self):
        try:
            conn, addr = self.server_socket.accept()  # Accept a connection
            print("Connection address:", addr)

            while True:
                self.rcv_msg = conn.recv(self.BUFFER_SIZE).decode('utf-8').rstrip() # Receive data from the client
                if not self.rcv_msg:
                    break
                print("Received data:", self.rcv_msg)  # Decode bytes to string
        except Exception as e:
            print("Error:", e)
        finally:
            conn.close()  # Close the connection
            self.server_socket.close()     # Close the socket

if __name__ == "__main__":
    svr = Server()
    svr.start()
    """def commmander():
            if svr.rcv_msg is not None:
                cmdVelData = svr.rcv_msg.split(',')
                print(type(cmdVelData))
                throttle = cmdVelData[0]
                print("Throttle:", throttle)
                braking = cmdVelData[1]
                print("Braking:", braking)
                steering = cmdVelData[2]
                print("Steering:", steering)
                while svr.rcv_msg is not None:
                    commmander()"""
    while True:
        if svr.rcv_msg is not None:
                cmdVelData = svr.rcv_msg.split(',')
                print(cmdVelData)
                throttle = cmdVelData[0]
                print("Throttle:", throttle)
                braking = cmdVelData[1]
                print("Braking:", braking)
                steering = cmdVelData[2]
                print("Steering:", steering)
                while svr.rcv_msg is not None:
                    #commmander()
        #commmander()
        break  # Exit the loop after processing the message once
