# A Graph is one of the most important data structures in Computer Science.
# A graph consists of:
# Vertices (Nodes) — Objects and Edges — Connections between objects
from scipy.sparse.csgraph import csgraph_from_dense
import numpy as np


# Undirected Graph
undirected_graph = np.array([[0, 1, 1, 0],
                             [1, 0, 1, 1],
                             [1, 1, 0, 1],
                             [0, 1, 1, 0]])
# Directed Graph
directed_graph = np.array([[0, 1, 1, 0],
                           [0, 0, 1, 1],
                           [0, 0, 0, 1],
                           [0, 0, 0, 1]])

# Represent the graphs as sparse matrices
undirected_sparse = csgraph_from_dense(undirected_graph)
print(undirected_sparse)

directed_sparse = csgraph_from_dense(directed_graph)
print(directed_sparse)

# Unweighted Graphs
unweighted_graph = np.array([[0, 1, 1, 0],
                            [0, 1, 1, 1],
                             [1, 0, 0, 0],
                            [0, 1, 0, 0]])

# Represent the graph as sparse matrices
unweighted_sparse = csgraph_from_dense(unweighted_graph)
print(unweighted_sparse)


# Weighted Graph
weighted_graph = np.array([[0, 4, 3, 0],
                        [0, 5, 6, 2],
                        [3, 0, 0, 0],
                        [0, 4, 0, 0]])

# Represent the graph as sparse matrices
weighted_sparse = csgraph_from_dense(weighted_graph)
print(weighted_sparse)
