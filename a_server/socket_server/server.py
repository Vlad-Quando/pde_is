from django.conf import settings

from socket import *
import json
import time
import random
import threading
from datetime import datetime
import os

from .server_commands.server_frames import *


# Server data
HOST = "213.189.221.17"
PORT = 6000
ADDRESS = (HOST, PORT)

# Socket class
class TCPServer:

    def __init__(self):

        self.socket = socket(AF_INET, SOCK_STREAM) # Creating socket
        
        self.socket.bind(ADDRESS) # Binding socket to the address

        self.socket.listen(1) # Starting socket
        print(f"Socket server is listening on {HOST}:{PORT}")

        self.connections = [] # List of all connected clients/all connections
    

    def send_command3(self, connection: socket) -> str:

        packet = QUERY_PARAMS_COMMAND # Creating a packet retrieving device data
        packet["time"] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)
        packet["deviceID"] = random.randint(100_000, 999_999) # Putting a random device ID
        json_packet = json.dumps(packet) # Serializing a packet to JSON

        connection.sendall(json_packet.encode()) # Sending a command to a client

        return json_packet
    
    
    def send_command2(self, connection: socket) -> str:

        packet = PARAM_SETTING_COMMAND
        packet["deviceID"] = random.randint(100_000, 999_999) # Putting a random device ID
        packet["supressMode"] = random.randint(1, 6) # Putting a supress mode value
        packet["time"] = int(datetime.now().timestamp() * 1_000_000_000) # Putting a current time (nanosecs)
        json_packet = json.dumps(packet) # Serializing a packet to JSON

        connection.sendall(json_packet.encode()) # Sending a command to a client

        return json_packet
    

    def recieve_command3_response(self, connection: socket, address) -> str:

        try:
            message = connection.recv(1024) # Recieving a message (JSON)
                
            try:
                json_message = json.loads(message.decode()) # Deserializing a message to a python dict
                print(f"RECIEVED from {address}:", end='\n') # Printing recieved message
                uav = json_message.get('uav', None)

                for k in json_message:
                    if k != "uav":
                        print(f"{k}: {json_message[k]}")
                print()
                
                if uav is not None:
                    print("UAV:")
                    for k in uav:
                        print(f"{k}: {uav[k]}")
                
                print("\n" + "-" * 30 + "\n")

                return json_message

            except Exception as exception:
                print(f"JSON parsing error: {exception}")
                return "Command3 Response: Error"

        except Exception as exception:
            print(f"An error occured on {address}: {exception}")
            return "Command3 Response: Error"


    def recieve_command2_response(self, connection: socket, address) -> str:

        try:
            message = connection.recv(1024) # Recieving a message (JSON)
                
            try:
                json_message = json.loads(message.decode()) # Deserializing a message to a python dict
                print(f"RECIEVED from {address}:", end='\n') # Printing recieved message
                params = json_message.get('params', None)

                for k in json_message:
                    if k != "params":
                        print(f"{k}: {json_message[k]}")
                print()
                
                if params is not None:
                    print("PARAMS:", params)

                print("\n" + "-" * 20 + "\n")

                return json_message

            except Exception as exception:
                print(f"JSON parsing error: {exception}")
                return "Command2 Response: Error"

        except Exception as exception:
            print(f"An error occured on {address}: {exception}")
            return "Command2 Response: Error"
    

    def recieve_commission_response(self, connection: socket, address) -> str:
        try:
            message = connection.recv(1024) # Recieving a message (JSON)
                
            try:
                json_message = json.loads(message.decode()) # Deserializing a message to a python dict
                print(f"RECIEVED from {address}:", end='\n') # Printing recieved message
                
                for k in json_message:
                    print(f"{k}: {json_message[k]}")
                print()

                return json_message

            except Exception as exception:
                print(f"JSON parsing error: {exception}")
                return "Commition: Error (Parsing)"

        except Exception as exception:
            print(f"An error occured on {address}: {exception}")
            return "Commition: Error (Connection)"


    # Client handling
    def handle_client(self, connection: socket, address):
        
        self.connections.append(connection) # Adding a client to the client's list

        log_dir = os.path.join(settings.BASE_DIR, "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = os.path.join(log_dir, current_time + ".json")
        print("LOG_FILE_NAME:", log_filename)

        # Server loop: sending 2 and 3 commands and recieving their responses every 3 secs
        
        with open(log_filename, 'w') as log:
            loop_time = 0
            
            while True:

                data = self.send_command3(connection)
                log_data = {"type": "SENT", "command": json.loads(data)}
                log.write(json.dumps(log_data) + "\n")

                data = self.recieve_commission_response(connection, address)
                log_data = {"type": "RECIEVED", "command": data}
                log.write(json.dumps(log_data) + "\n")

                data = self.recieve_command3_response(connection, address)
                log_data = {"type": "RECIEVED", "command": data}
                log.write(json.dumps(log_data) + "\n")

                time.sleep(1)

                data = self.send_command2(connection)
                log_data = {"type": "SENT", "command": json.loads(data)}
                log.write(json.dumps(log_data) + "\n")

                data = self.recieve_commission_response(connection, address)
                log_data = {"type": "RECIEVED", "command": data}
                log.write(json.dumps(log_data) + "\n")

                data = self.recieve_command2_response(connection, address)
                log_data = {"type": "RECIEVED", "command": data}
                log.write(json.dumps(log_data) + "\n")

                time.sleep(2)
                loop_time += 1

                if loop_time == 2:
                    break
                

    # Server code
    def server(self):
        
        # Server loop
        while True:

            connection, address = self.socket.accept() # Establishing a connection

            # self.handle_client(connection, address)

            client_thread = threading.Thread(target=self.handle_client, args=[connection, address]) # Creating a thread for a new client
            client_thread.start() # Starting the thread
    
    # Shutting the server down
    def close_server(self):

        for connection in self.connections: # Closing all connections
            connection.close()

        print("Server closed.")


def main():
    server = TCPServer()
    
    try:
        server.server()
    except KeyboardInterrupt:
        print("Shutting down the server.")
        server.close_server()
        