# Connected Components
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
import numpy as np

connected_graph = np.array([[0, 0, 1, 0, 0],
                            [0, 0, 0, 1, 1],
                            [1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]])

# Convert to sparse matrix
sparse_matrix = coo_matrix(connected_graph)

# Weakly connected components
weak_components, labels = connected_components(csgraph=sparse_matrix,
                                               directed=True, connection='weak')
print("Num of Weak Components:", weak_components)
print("Labels:", labels)

# Strongly connected components
strong_components, labels = connected_components(csgraph=sparse_matrix,
                                                 directed=True, connection='strong')
print("Num of Strong Components:", strong_components)
print("Labels:", labels)
