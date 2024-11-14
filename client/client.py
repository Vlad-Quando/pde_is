from socket import *
import json
import time
from datetime import datetime
import random

from client_frames import *

# Connection data
HOST = "192.168.43.61"
PORT = 6000
ADDRESS = (HOST, PORT)

# Socket class
class TCPClient:

    def __init__(self):
        
        self.socket = socket(AF_INET, SOCK_STREAM) # Creating a connection

        while True:

            try:
                self.socket.connect(ADDRESS) # Establishing a connection
                print("Connection successfully established.")
                break

            except ConnectionRefusedError as e:
                print("ERROR:", e)
                time.sleep(5)
                continue
    

    def recieve_command(self):
        message = self.socket.recv(1024) # Recieving a message

        try:
            json_message = json.loads(message.decode())
            print(json_message)
            print()
            
            packet_type = json_message.get("packetType", None)

            return packet_type

        except Exception as exception:
            print(f"An error occured while handling a recieved message: {exception}")

    
    # Handling a connection
    def handle_connection(self):

        # Client loop
        while True:
            packet_type = self.recieve_command()

            if packet_type is not None:
                if packet_type == 3:
                    commit_packet = DATA_RECEPTION_COMMITION
                    commit_packet["result"] = random.randint(1, 3)
                    commit_packet["time"] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)

                    json_commit_packet = json.dumps(commit_packet)
                    self.socket.sendall(json_commit_packet.encode())

                    packet = DETECTION_DATA_FRAME
                    packet["signalType"] = random.randint(1, 10)
                    packet["time"] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)

                    json_packet = json.dumps(packet)
                    self.socket.sendall(json_packet.encode())

                elif packet_type == 2:
                    commit_packet = DATA_RECEPTION_COMMITION
                    commit_packet["result"] = random.randint(1, 3)
                    commit_packet["time"] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)

                    json_commit_packet = json.dumps(commit_packet)
                    self.socket.sendall(json_commit_packet.encode())

                    packet = PARAMS_DATA_COMMAND
                    packet["deviceStatus"] = random.randint(1, 3)
                    packet["time"] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)

                    json_packet = json.dumps(packet)
                    self.socket.sendall(json_packet.encode())

    
    def close_connection(self):
        self.socket.close() # Closing connection


def main():

    client = TCPClient()

    try:
        client.handle_connection()

    except KeyboardInterrupt:
        print("Closing connection.")
        client.close_connection()


if __name__ == "__main__":
    main()