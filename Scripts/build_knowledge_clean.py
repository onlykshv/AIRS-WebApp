import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

relations_df = pd.read_csv('D:/AIRS WebApp/data/processed/relations.csv')

# Calculate degrees and select top 10 nodes for a focused graph
all_nodes = list(set(relations_df['Source'].tolist() + relations_df['Target'].tolist()))
G = nx.DiGraph()
for _, row in relations_df.iterrows():
    G.add_edge(row['Source'], row['Target'], label=row['Relation'])

# Get top 10 nodes by degree
top_n = 10
node_degrees = dict(G.degree())
selected_nodes = sorted(node_degrees, key=node_degrees.get, reverse=True)[:top_n]

# Create subgraph and include edges only between selected nodes
subG = G.subgraph(selected_nodes).copy()
# Set up layout
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(subG, seed=42)
# Draw nodes and labels
nx.draw_networkx_nodes(subG, pos, node_color='skyblue', node_size=1600)
nx.draw_networkx_edges(subG, pos, arrowstyle='-|>', arrowsize=20, edge_color='darkgray')
nx.draw_networkx_labels(subG, pos, font_size=10, font_family='Arial', font_weight='bold')
# Draw edge labels in red
edge_labels = nx.get_edge_attributes(subG, 'label')
nx.draw_networkx_edge_labels(subG, pos, edge_labels=edge_labels, font_color='red', font_size=8)
plt.title('Clean and Clear Subgraph of Ransomware Knowledge Graph')
plt.axis('off')
plt.show()
