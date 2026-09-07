# Statistical plots summarize data and reveal mathematical relationships.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({"x": np.arange(100),
                   "y": np.random.randint(0, 100, 100)})

df_cat = pd.DataFrame({"Department":
                       np.random.choice(["IT", "HR", "Sales"], 100),
                       "Salary": np.random.randint(2000,
                                                   6000, 100),
                       "Level": np.random.choice(["Boss", "Leader", "Employee"], 100)})

# Regression Plot is a scatter plot with a regression line.
sns.regplot(data=df, x="x", y="y")
plt.show()

# LM Plot is an enhanced regression plot.
df_cat.insert(loc=3, column='PR_Score', value=np.random.randint(1, 100, 100))

sns.lmplot(data=df_cat, x="PR_Score", y="Salary", hue='Level', col='Department')
plt.show()

# Heatmap is one of Seaborn's most famous visualizations.
matrix = np.random.rand(5, 5)
sns.heatmap(matrix, annot=True, cmap="coolwarm")
plt.show()

# Catplot is a flexible interface for categorical visualizations.
# Add Gender column
df_cat.insert(loc=2, column='Gender',
              value=np.random.choice(["Male", "Female"], 100))

# Add Experience Level (Low, Medium, High)
df_cat.insert(loc=3, column='Experience',
              value=np.random.choice(["Low", "Medium", "High"], 100))

sns.catplot(data=df_cat, x="Experience", y="Salary", kind="point",
            hue='Gender', col='Department')

