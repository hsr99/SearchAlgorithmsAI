import networkx as nx
import matplotlib.pyplot as plt
from Graph import *
def beam_search_dest(G, source, destination, beamwidth=5):
  paths=[]
  queue = [(source, 0, [])]
  visited = set()

  while queue:
    node, score, path = queue.pop(0)
    visited.add(node)

    if node == destination:
      return path

    neighbors = []
    for neighbor in G[node]:
      neighbors.append((neighbor, score + 1, path + [node]))

    neighbors.sort(key=lambda x: x[1], reverse=True)
    neighbors = neighbors[:beamwidth]

    for neighbor, score, path in neighbors:
      if neighbor not in visited:
        queue.append((neighbor, score, path))

  return None


path = beam_search_dest(G, 0, 4)




