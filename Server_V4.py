import threading
import socket

class ServerThread(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")

                with client_socket:
                    while True:
                        try:
                            data = client_socket.recv(1024)
                            if not data:
                                break
                            received_data = data.decode().split(',')
                            float_list = [float(item) for item in received_data]
                            #print("Received:", float_list)
                            throttle = float_list[0]
                            #print("Throttle:", throttle)
                            braking = float_list[1]
                            #print("Braking:", braking)
                            steering = float_list[2]
                            #print("Steering:", steering)
                        except Exception as e:
                            print("Error:", e)
                            break

if __name__ == "__main__":
    host = '192.168.0.170'
    port = 2203
    server_thread = ServerThread(host, port)
    server_thread.start()
    print("Throttle:", server_thread.throttle)
    print("Braking:", server_thread.braking)
    print("Steering:", server_thread.steering)