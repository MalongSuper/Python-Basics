# Depth-First Search
from scipy.sparse.csgraph import depth_first_order, depth_first_tree
from scipy.sparse import csr_matrix
import numpy as np

graph = np.array([[0, 1, 1, 1, 0],
                  [1, 0, 1, 0, 0],
                  [1, 1, 0, 0, 1],
                  [1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0]])

# Convert to sparse matrix
sparse_matrix = csr_matrix(graph)

dfs_order = depth_first_order(csgraph=sparse_matrix, i_start=0,
                              directed=False)
print("DFS Order:", dfs_order[0])

dfs_tree = depth_first_tree(csgraph=sparse_matrix, i_start=0,
                            directed=False)
print("DFS Tree:\n", dfs_tree.toarray())
