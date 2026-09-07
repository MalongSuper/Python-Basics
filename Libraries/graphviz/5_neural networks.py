# Neural networks consist of: Input Layer; Hidden Layer(s); Output Layer
from graphviz import Digraph

nn = Digraph("Neural Network", format="png")
nn.attr(rankdir="LR", splines="line")
nn.attr("node", fixedsize="true", shape="circle")

# Input Layer
with nn.subgraph(name="cluster_input") as c:
    c.attr(color="white", label="Input Layer")
    c.attr("node", color="blue4")
    for node in ["x1", "x2", "x3", "x4"]:
        c.node(node)

# Hidden Layer
with nn.subgraph(name="cluster_hidden") as c:
    c.attr(color="white", label="Hidden Layer")
    c.attr("node", color="red2")
    for node in ["h1", "h2", "h3"]:
        c.node(node)

# Output Layer
with nn.subgraph(name="cluster_output") as c:
    c.attr(color="white", label="Output Layer")
    c.attr("node", color="seagreen2")
    c.node("O")

# Fully connect Input → Hidden
inputs = ["x1", "x2", "x3", "x4"]
hidden = ["h1", "h2", "h3"]

for x in inputs:
    for h in hidden:
        nn.edge(x, h)

# Fully connect Hidden → Output
for h in hidden:
    nn.edge(h, "O")

nn.view()
