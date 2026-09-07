# An undirected graph represents relationships without direction.
from graphviz import Graph

g = Graph("Undirected Graph", format="png")

g.edge("Alice", "Bob")
g.edge("Bob", "Charlie")
g.edge("Alice", "David")

g.view()
