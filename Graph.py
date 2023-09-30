import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
 
G.add_edge('A','B')
G.add_edge('A','C')
G.add_edge('B','C')
G.add_edge('C','D')
G.add_edge('C','E')
 
# drawing in planar layout
nx.draw_planar(G, with_labels = True)
plt.show()

'''
count = 0
def create_tree():
    n = int(input("Enter the number of nodes: "))
    G = nx.Graph()
    node_names = [input(f"Enter the name of node {i+1}: ") for i in range(n)]
    for i in range(n-1):
        count = int(input(f"Enter the number of parents for{node_names[i+1]}"))
        while count>0:
            parent = input(f"Enter the parent node {count} for node {node_names[i+1]}: ")
            cost = int(input(f"Enter the cost from {parent} to node {node_names[i+1]}: "))
            G.add_edge(parent, node_names[i+1], cost=cost)
            count= count-1
    
    return G

def visualize_tree(G):
    pos = nx.spring_layout(G)  # Positions all nodes
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", font_color="black")
    edge_labels = nx.get_edge_attributes(G, 'cost')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    plt.show()

graph = create_tree()

visualize_tree(graph)
'''

