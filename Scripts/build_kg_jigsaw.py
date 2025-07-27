import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

core_family = "Jigsaw"  # Ransomware family name to visualize

# Load the relations data
relations_df = pd.read_csv('D:/AIRS WebApp/data/processed/relations.csv')

# Case-insensitive matching for robustness
relations_df['Source_low'] = relations_df['Source'].str.lower()
relations_df['Target_low'] = relations_df['Target'].str.lower()
core_family_lower = core_family.lower()

# Find all variants of 'Jigsaw'
family_nodes = set()
if core_family_lower in relations_df['Source_low'].values:
    family_nodes.update(relations_df.loc[relations_df['Source_low'] == core_family_lower, 'Source'])
if core_family_lower in relations_df['Target_low'].values:
    family_nodes.update(relations_df.loc[relations_df['Target_low'] == core_family_lower, 'Target'])

if not family_nodes:
    print(f'No node matching "{core_family}" found in relations.csv.')
    exit()

# Build the directed graph and collect direct neighbors (1-hop)
G = nx.DiGraph()
for _, row in relations_df.iterrows():
    G.add_edge(row['Source'], row['Target'], label=row['Relation'])

all_neighbors = set()
for fam in family_nodes:
    all_neighbors |= set(G.successors(fam))
    all_neighbors |= set(G.predecessors(fam))

sub_nodes = list(family_nodes | all_neighbors)
subG = G.subgraph(sub_nodes).copy()

if subG.number_of_edges() == 0:
    print(f'"{core_family}" is in your data, but has no direct connections.')
    exit()

# Node coloring for clarity
node_colors = []
for n in subG.nodes:
    if n in family_nodes:
        node_colors.append('orange')  # Highlight the main ransomware family node
    elif any(relations_df.loc[relations_df['Target'] == n, 'Relation'].str.contains('Threat').any() for _ in [0]):
        node_colors.append('red')     # Threat/event nodes
    elif any(relations_df.loc[relations_df['Target'] == n, 'Relation'].str.contains('Address|IPaddress', case=False).any() for _ in [0]):
        node_colors.append('deepskyblue')  # Address/IP nodes
    else:
        node_colors.append('lightgray')    # Other nodes

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(subG, seed=100, k=0.5)
nx.draw_networkx_nodes(subG, pos, node_color=node_colors, node_size=1800, alpha=0.9)
nx.draw_networkx_labels(subG, pos, font_size=12, font_weight='bold', font_family='Arial')
nx.draw_networkx_edges(subG, pos, arrows=True, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2)
edge_labels = nx.get_edge_attributes(subG, 'label')
nx.draw_networkx_edge_labels(
    subG, pos, edge_labels=edge_labels, font_color='mediumvioletred',
    font_size=10, bbox=dict(facecolor='white', edgecolor='none', pad=1.5)
)
plt.title(f'Knowledge Graph: Direct Connections of "{core_family}"', fontsize=18, fontweight='bold', color='navy')
plt.axis('off')
plt.tight_layout()
plt.show()
