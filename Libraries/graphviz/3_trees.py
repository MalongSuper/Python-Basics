# A tree is a special graph structure
# where each child has exactly one parent
from graphviz import Digraph

tree = Digraph(format="png")

tree.edge("Root", "A")
tree.edge("Root", "B")

tree.edge("A", "A1")
tree.edge("A", "A2")

tree.edge("B", "B1")
tree.edge("B", "B2")

tree.view()
