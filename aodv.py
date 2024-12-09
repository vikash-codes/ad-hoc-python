import networkx as nx
from queue import Queue

class AODV:
    def __init__(self, graph):
        self.graph = graph
        self.routes = {}  # Stores discovered routes

    def route_request(self, src, dest):
        # Simulate RREQ broadcast
        visited = set()
        queue = Queue()
        queue.put((src, [src]))

        while not queue.empty():
            current, path = queue.get()
            if current in visited:
                continue
            visited.add(current)

            if current == dest:
                self.routes[(src, dest)] = path
                return path  # Route found

            for neighbor in self.graph.neighbors(current):
                queue.put((neighbor, path + [neighbor]))

        return None  # Route not found

# Create a sample graph for testing
network = nx.Graph()
network.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# AODV Example
aodv = AODV(network)
route = aodv.route_request(1, 4)
print("Discovered Route:", route)
