import networkx as nx
import matplotlib.pyplot as plt

# Create a graph to represent the network
network = nx.Graph()

# Add nodes representing devices
network.add_nodes_from(range(1, 6))

# Add edges representing connections
network.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# Visualize the network
pos = nx.spring_layout(network)  # Layout for visualization
nx.draw(network, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title("Ad-hoc Network Environment")
plt.show()
