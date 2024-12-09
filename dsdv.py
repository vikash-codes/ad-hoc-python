import networkx as nx
import pandas as pd

class DSDV:
    def __init__(self, graph):
        self.graph = graph
        self.routing_table = pd.DataFrame(columns=['Destination', 'Next Hop', 'Distance', 'Sequence Number'])

    def initialize_routing_table(self, node):
        for dest in self.graph.nodes:
            if dest == node:
                self.routing_table = self.routing_table._append({'Destination': dest, 'Next Hop': None, 'Distance': 0, 'Sequence Number': 0}, ignore_index=True)
            elif dest in self.graph.neighbors(node):
                self.routing_table = self.routing_table._append({'Destination': dest, 'Next Hop': dest, 'Distance': 1, 'Sequence Number': 0}, ignore_index=True)
            else:
                self.routing_table = self.routing_table._append({'Destination': dest, 'Next Hop': None, 'Distance': float('inf'), 'Sequence Number': 0}, ignore_index=True)

    def print_routing_table(self):
        print(self.routing_table)

# Create a sample graph for testing
network = nx.Graph()
network.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# DSDV Example
dsdv = DSDV(network)
dsdv.initialize_routing_table(1)
dsdv.print_routing_table()
