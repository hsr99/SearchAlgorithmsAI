from dsplot.graph import Graph

graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)
graph.plot()