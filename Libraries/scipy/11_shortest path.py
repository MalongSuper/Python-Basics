# Shortest Path
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
import numpy as np

graph = np.array([[0, 4, 5, 0, 0, 0],
                  [4, 0, 11, 9, 7, 0],
                  [5, 11, 0, 0, 3, 0],
                  [0, 9, 0, 0, 13, 2],
                  [0, 7, 3, 13, 0, 6],
                  [0, 0, 0, 2, 6, 0]])

# Convert to sparse matrix
sparse_matrix = csr_matrix(graph)

# Finding the shortest path
dist_matrix, predecessors = shortest_path(csgraph=sparse_matrix,
                                          directed=False,
                                          return_predecessors=True)
print("Distance Matrix:\n", dist_matrix)
print("Predecessor Matrix:\n", predecessors)
