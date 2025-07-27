import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read edges (relations) from your processed file
relations_df = pd.read_csv('D:/AIRS WebApp/data/processed/relations.csv')

# Build the graph: Directed or undirected depending on your needs
G = nx.DiGraph()  # Graph with direction (source -> target)

for _, row in relations_df.iterrows():
    source = row['Source']
    target = row['Target']
    relation = row['Relation']
    G.add_edge(source, target, label=relation)

print(f"Your graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Draw a small preview to avoid clutter (e.g. 20 nodes only)
sub_nodes = list(G.nodes)[:20]
subG = G.subgraph(sub_nodes)

plt.figure(figsize=(14,10))
pos = nx.spring_layout(subG)
nx.draw(subG, pos, with_labels=True, node_size=500, font_size=8, arrowsize=20)
edge_labels = nx.get_edge_attributes(subG, 'label')
nx.draw_networkx_edge_labels(subG, pos, edge_labels=edge_labels, font_size=7)
plt.title("Sample Subgraph Preview")
plt.show()
