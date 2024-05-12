import socket

def main():
    host = '192.168.0.170'  # Change this to your desired host or use an empty string to listen on all available interfaces
    port = 2203         # Change this to your desired port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

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
                        print("Received:", float_list)
                        print("Received:", float_list)
                        throttle = float_list[0]
                        print("Throttle:", throttle)
                        braking = float_list[1]
                        print("Braking:", braking)
                        steering = float_list[2]
                        print("Steering:", steering)
                    except Exception as e:
                        print("Error:", e)
                        break

if __name__ == "__main__":
    main()
