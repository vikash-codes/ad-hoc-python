import random

# Server and client configuration
class Device:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

class Server(Device):
    def __init__(self, name, ip_address, capacity, signal_range):
        super().__init__(name, ip_address)
        self.capacity = capacity
        self.signal_range = signal_range
        self.used_capacity = 0

class Client(Device):
    def __init__(self, name, ip_address, max_threshold):
        super().__init__(name, ip_address)
        self.max_threshold = max_threshold
        self.used_bandwidth = 0

# Initialize devices
server = Server("Server-1", "192.168.1.1", capacity=1000, signal_range=400)
clients = [
    Client(f"Client-{i+1}", f"192.168.1.{i+2}", max_threshold=200)
    for i in range(4)
]

# Device Configurator
class DeviceConfigurator:
    def __init__(self, server, clients):
        self.server = server
        self.clients = clients
        self.time_intervals = [20, 40, 60, 80, 100]

    def process_requests(self):
        print("Processing requests...")
        print(f"{'Time':<10}{'Client':<15}{'IP Address':<15}{'Status':<10}{'Used Bandwidth':<15}{'Server Used Capacity'}")
        for time in self.time_intervals:
            for client in self.clients:
                status = self.handle_request(client)
                print(f"{time:<10}{client.name:<15}{client.ip_address:<15}{status:<10}{client.used_bandwidth:<15}{self.server.used_capacity}")

    def handle_request(self, client):
        request = 50  # Each client request 50MBps
        if (
            self.server.used_capacity + request <= self.server.capacity
            and client.used_bandwidth + request <= client.max_threshold
        ):
            # Allocate bandwidth
            self.server.used_capacity += request
            client.used_bandwidth += request
            return "Success"
        else:
            return "Fail"

# Run simulation
configurator = DeviceConfigurator(server, clients)
configurator.process_requests()





import networkx as nx
import matplotlib.pyplot as plt

# Visualization function
def visualize_network(server, clients, time, configurator):
    # Create a graph
    graph = nx.Graph()

    # Add server and clients as nodes
    graph.add_node(server.name, color="red", size=700)
    for client in clients:
        graph.add_node(client.name, color="blue", size=500)

    # Add edges between server and clients
    for client in clients:
        graph.add_edge(server.name, client.name, weight=client.used_bandwidth)

    # Get node colors and sizes
    node_colors = [graph.nodes[node]["color"] for node in graph.nodes]
    node_sizes = [graph.nodes[node]["size"] for node in graph.nodes]

    # Get edge labels for bandwidth
    edge_labels = nx.get_edge_attributes(graph, "weight")

    # Plot the graph
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    nx.draw(
        graph, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, edge_color="gray"
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="green")

    plt.title(f"Server-Client Network at Time {time}s\nServer Used Capacity: {server.used_capacity} MBps")
    plt.show()

# Process requests with visualization
class DeviceConfiguratorWithVisualization(DeviceConfigurator):
    def process_requests_with_visualization(self):
        print("Processing requests with visualization...")
        for time in self.time_intervals:
            for client in self.clients:
                self.handle_request(client)
            visualize_network(self.server, self.clients, time, self)

# Run simulation with visualization
configurator_with_visualization = DeviceConfiguratorWithVisualization(server, clients)
configurator_with_visualization.process_requests_with_visualization()
