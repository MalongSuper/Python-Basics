# Breadth-First Search
from scipy.sparse.csgraph import breadth_first_order, breadth_first_tree
from scipy.sparse import csr_matrix
import numpy as np

graph = np.array([[0, 1, 1, 1, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 0, 1],
                  [1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0]])

# Convert to sparse matrix
sparse_matrix = csr_matrix(graph)

bfs_order = breadth_first_order(csgraph=sparse_matrix, i_start=0,
                               directed=False)
print("BFS Order:", bfs_order[0])

bfs_tree = breadth_first_tree(csgraph=sparse_matrix, i_start=0,
                              directed=False)
print("BFS Tree:\n", bfs_tree.toarray())
