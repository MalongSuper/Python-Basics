# A directed graph uses arrows
# to indicate the direction of a relationship.
from graphviz import Digraph

g = Digraph("Directed Graph", format="png")

g.edge("A", "B")
g.edge("B", "C")
g.edge("A", "D")

g.view()
