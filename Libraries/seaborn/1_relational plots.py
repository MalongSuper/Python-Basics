# Relational plots help us understand relationships
# between numerical variables.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({"x": np.arange(100),
                   "y": np.random.randint(0, 100, 100)})

# Scatter Plot displays individual observations
sns.scatterplot(data=df, x="x", y="y")
plt.show()

# Line Plot displays trends and changes over time
sns.lineplot(data=df, x="x", y="y")
plt.show()
