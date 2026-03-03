import socket
import threading
import json
import time

class Node:
    def __init__(self, port, name):
        self.host = '127.0.0.1'
        self.port = port
        self.name = name

    def start_transmitter(self):
        # Task: Set up a basic server that listens for connections
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        while True:
            conn, addr = server.accept()
            # Task: Enable asynchronous message handling using threading
            threading.Thread(target=self.receive_messages, args=(conn,), daemon=True).start()

    def receive_messages(self, conn):
        # Task: Implement clients that can exchange messages
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    event = json.loads(data)
                    print(f"[{self.name}] RECEIVED: {event['type']} from {event['sender']}")
            except:
                break

    def send_event(self, target_port, event_type):
        # Goal: Define Events for them to be sent in messages
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, target_port))
            payload = json.dumps({"type": event_type, "sender": self.name})
            client.send(payload.encode('utf-8'))
            client.close()
        except Exception as e:
            print(f"Connection failed from {self.name} to {target_port}")

if __name__ == "__main__":
    # Goal: Test with at least four nodes
    ports = [5000, 5001, 5002, 5003]
    names = ["Order-Node", "Payment-Node", "Email-Node", "Cancel-Node"]
    nodes = [Node(ports[i], names[i]) for i in range(4)]

    # Start all nodes as transmitters (servers)
    for n in nodes:
        threading.Thread(target=n.start_transmitter, daemon=True).start()
    
    time.sleep(1) # Brief pause for synchronization

    print("--- STARTING EVENT FLOW ---")
    # Simulation of required events
    nodes[0].send_event(5001, "OrderCreated")
    nodes[1].send_event(5002, "PaymentProcessed")
    nodes[2].send_event(5003, "EmailSent")
    nodes[0].send_event(5003, "OrderCancelled")
    
    time.sleep(2) # Allow time for asynchronous receipt
    print("--- SIMULATION COMPLETE ---")
