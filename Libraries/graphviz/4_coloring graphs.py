# Nodes and edges can be customized with colors, shapes, and styles.
from graphviz import Digraph

g = Digraph(format="png")

g.node("Server", color="red", style="filled")
g.node("Database", color="lightblue", style="filled")
g.node("Client", color="lightgreen", style="filled")

g.edge("Client", "Server")
g.edge("Server", "Database")

g.view()
