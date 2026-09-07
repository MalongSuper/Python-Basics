# Distribution plots help us understand how data is spread.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({"x": np.arange(100),
                   "y": np.random.randint(0, 100, 100)})

# Histogram shows frequency distributions.
sns.histplot(df["y"], bins=15)
plt.show()

# KDE Plot displays a smooth probability density curve.
sns.kdeplot(df["y"], fill=True)
plt.show()

# Rug Plot displays every observation as a small tick mark.
# Draw Histogram with KDE line alongside rugplot
sns.histplot(df["y"], kde=True, stat="density", linewidth=1)
sns.rugplot(df["y"], color='red')
plt.show()

# Joint Plot combines multiple visualizations into one figure.
sns.jointplot(data=df, x="x", y="y", kind="scatter")
plt.show()
