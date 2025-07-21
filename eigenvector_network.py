import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (river system example)
G = nx.DiGraph()

edges = [
    ('Source1', 'Junction1'),
    ('Source2', 'Junction1'),
    ('Junction1', 'Junction2'),
    ('Tributary1', 'Junction2'),
    ('Junction2', 'MainRiver'),
    ('MainRiver', 'Outflow'),
    ('Tributary2', 'MainRiver')
]

G.add_edges_from(edges)

# Use eigenvector_centrality (not the numpy version)
ec = nx.eigenvector_centrality(G, max_iter=1000, tol=1e-06)

# Display results
print("Eigenvector Centrality:")
for node, value in ec.items():
    print(f"{node}: {value:.4f}")

# Visualize the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
node_size = [5000 * ec[n] for n in G.nodes()]
nx.draw(G, pos, with_labels=True, node_size=node_size, node_color='blue', edge_color='green', arrows=True)
plt.title("River Network Eigenvector Centrality (Disconnected Graph Supported)")
plt.show()
