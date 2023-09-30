import igraph as ig
from igraph import *
import matplotlib.pyplot as plt

def breadth_first_search(graph, start_vertex):
    queue = []
    visited = set()

    queue.append(start_vertex)
    visited.add(start_vertex)
    traversal_edge=[]
    while queue:
        traverse=Graph()
        current_vertex = queue.pop(0)
        #print(current_vertex)
        try:
            neighbors = graph[current_vertex]
        except KeyError:
            pass
        for neighbor in neighbors:
            # names=[0]
            if neighbor not in visited:
                # names+=[neighbor]
                traversal_edge+=[(current_vertex,neighbor)]
                print(traversal_edge)
                traverse=ig.Graph(edges=traversal_edge)
                # traverse.vs['name']=names
                queue.append(neighbor)
                visited.add(neighbor)
                traverse.layout(layout='auto')
                # visual_style = {} 
                # visual_style["vertex_label"] = traverse.vs["name"]
                fig, ax = plt.subplots()
                ig.plot(traverse, target=ax)
                plt.show()


#graph creation
vertex=[0,1,2,3,4]
edges = [(0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (3, 4), (2, 4)]
g=Graph()
g= ig.Graph(edges=edges)
g.vs['name']=vertex

el=g.get_edgelist()
edge_dict={}
for edge in edges:
    parent,child = edge
    if parent not in edge_dict:
        edge_dict[parent] = []
    edge_dict[parent].append(child)

print(edge_dict)
start_vertex = 0

print("Breadth-First Search starting from vertex", start_vertex)
breadth_first_search(edge_dict, start_vertex)


# #plotting
# g.layout(layout='auto')
# visual_style = {} #visual attributes of the graph
# visual_style["vertex_label"] = g.vs["name"]
# fig, ax = plt.subplots()
# ig.plot(g, target=ax,**visual_style)
# plt.show()


