# 76. Weather Prediction Decision Tree (Graphviz)
from graphviz import Digraph

# Make the node square
tree = Digraph(name="weather_tree", format="png")
tree.node_attr.update(shape="box")

# Outlook
tree.node("Outlook", fontcolor="white",
          color="blue", style="filled")
tree.node("Sunny", fontcolor="white",
          color="lightblue", style="filled")
tree.node("Overcast", fontcolor="white",
          color="lightblue", style="filled")
tree.node("Rainy", fontcolor="white",
          color="lightblue", style="filled")

tree.edge("Outlook", "Sunny")
tree.edge("Outlook", "Overcast")
tree.edge("Outlook", "Rainy")

# Windy
tree.node("Windy", fontcolor="white",
          color="blue", style="filled")
tree.node("FALSE", fontcolor="white",
          color="lightblue", style="filled")
tree.node("TRUE", fontcolor="white",
          color="lightblue", style="filled")

tree.edge("Sunny", "Windy")
tree.edge("Windy", "FALSE")
tree.edge("Windy", "TRUE")

# Temperature
tree.node("Temperature", fontcolor="white",
          color="blue", style="filled")
tree.node("Cool", fontcolor="white",
          color="lightblue", style="filled")
tree.node("Mild", fontcolor="white",
          color="lightblue", style="filled")
tree.node("Hot", fontcolor="white",
          color="lightblue", style="filled")

tree.edge("Rainy", "Temperature")
tree.edge("Temperature", "Cool")
tree.edge("Temperature", "Mild")
tree.edge("Temperature", "Hot")

# Hours Played (output node)
tree.node("46.5", fontcolor="white",
          color="orange", style="filled")
tree.node("47.7", fontcolor="white",
          color="orange", style="filled")
tree.node("26.5", fontcolor="white",
          color="orange", style="filled")
tree.node("38", fontcolor="white",
          color="orange", style="filled")
tree.node("27.5", fontcolor="white",
          color="orange", style="filled")
tree.node("41.5", fontcolor="white",
          color="orange", style="filled")


tree.edge("Overcast", "46.5")
tree.edge("FALSE", "47.7")
tree.edge("TRUE", "26.5")
tree.edge("Cool", "38")
tree.edge("Hot", "27.5")
tree.edge("Mild", "41.5")

# View the tree
tree.view()
