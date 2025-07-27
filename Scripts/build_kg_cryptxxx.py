import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the relations data
relations_df = pd.read_csv('D:/AIRS WebApp/data/processed/relations.csv')

# Build the directed graph
G = nx.DiGraph()
for _, row in relations_df.iterrows():
    G.add_edge(row['Source'], row['Target'], label=row['Relation'])

core_family = "CryptXXX"

# Get all nodes directly connected to CryptXXX
neighbors = list(G.successors(core_family)) + list(G.predecessors(core_family))
sub_nodes = list(set([core_family] + neighbors))
subG = G.subgraph(sub_nodes).copy()

# Assign node colors by type
node_colors = []
for n in subG.nodes:
    if n == core_family:
        node_colors.append('orange')  # Highlight main ransomware
    elif any(relations_df.loc[relations_df['Target'] == n, 'Relation'].str.contains('Threat').any() for _ in [0]):
        node_colors.append('red')  # Threat type node
    elif any(relations_df.loc[relations_df['Target'] == n, 'Relation'].str.contains('Address|IPaddress', case=False).any() for _ in [0]):
        node_colors.append('deepskyblue')  # Addresses or IPs
    else:
        node_colors.append('lightgray')  # Other node types

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(subG, seed=31, k=0.5)
nx.draw_networkx_nodes(subG, pos, node_color=node_colors, node_size=1800, alpha=0.88)
nx.draw_networkx_labels(subG, pos, font_size=12, font_weight='bold', font_family='Arial')
nx.draw_networkx_edges(subG, pos, arrows=True, arrowstyle='-|>', arrowsize=19, edge_color='gray', width=2)
edge_labels = nx.get_edge_attributes(subG, 'label')
nx.draw_networkx_edge_labels(
    subG, pos, edge_labels=edge_labels, font_color='mediumvioletred',
    font_size=10, bbox=dict(facecolor='white', edgecolor='none', pad=1.5)
)
plt.title(f'Knowledge Graph: Direct Connections of "CryptXXX"', fontsize=16, fontweight='bold', color='navy')
plt.axis('off')
plt.tight_layout()
plt.show()
