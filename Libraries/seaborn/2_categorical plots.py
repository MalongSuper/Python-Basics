# Categorical plots compare groups and categories
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_cat = pd.DataFrame({"Department":
                       np.random.choice(["IT", "HR", "Sales"], 100),
                       "Salary": np.random.randint(2000,
                                                   6000, 100),
                       "Level": np.random.choice(["Boss", "Leader", "Employee"], 100)})

# Bar Plot shows average values across categories.
sns.barplot(data=df_cat, x="Department", y="Salary")
plt.show()

# Box Plot shows distribution and outliers.
sns.boxplot(data=df_cat, x="Department", y="Salary")
plt.show()

# Violin Plot combines a box plot with a distribution plot.
sns.violinplot(data=df_cat, x="Department", y="Salary")
plt.show()

# Strip Plot displays individual observations.
sns.stripplot(data=df_cat, x="Department", y="Salary")
plt.show()

# Swarm Plot is similar to strip plots but prevents overlap.
sns.swarmplot(data=df_cat, x="Department", y="Salary")
plt.show()

# Point Plot displays category averages as points.
sns.pointplot(data=df_cat, x="Department", y="Salary", hue='Level')
plt.show()


