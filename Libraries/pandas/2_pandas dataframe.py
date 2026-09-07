# Python Pandas DataFrame
import pandas as pd
import numpy as np

# Creating a DataFrame
# From a Dictionary of Lists
data = {"Name": ["Alice", "Bob", "Charlie"],
        "Major": ["CS", "IT", "AI"],
        "GPA": [3.8, 3.5, 3.9]}
df = pd.DataFrame(data)
print(df)

# From a List of Dictionaries
data = [{"Name": "Alice", "Major": "CS", "GPA": 3.8},
        {"Name": "Bob", "Major": "IT", "GPA": 3.5},
        {"Name": "Charlie", "Major": "AI", "GPA": 3.9}]
df = pd.DataFrame(data)
print(df)

# From a List of Lists
data = [["Alice", "CS", 3.8],
        ["Bob", "IT", 3.5],
        ["Charlie", "AI", 3.9]]
df = pd.DataFrame(data, columns=["Name", "Major", "GPA"])
print(df)

# From NumPy Arrays
data = np.array([[85, 90],
                [88, 92],
                [95, 97]])
df = pd.DataFrame(data, columns=["Math", "Science"])
print(df)

# The columns= parameter allows to specify column names.
data = [["Alice", "CS"], ["Bob", "IT"]]
df = pd.DataFrame(data, columns=["Name", "Major"])
print(df)

# Suppose some column names exist while others do not.
# If a requested column does not exist, Pandas creates the column, and all values become NaN.
# If columns= is omitted, Pandas automatically uses the keys of the input data.
data = {"Name": ["Alice", "Bob"],
        "Major": ["CS", "IT"]}
df = pd.DataFrame(data, columns=["Name", "Major", "GPA"])
print(df)

# Naming the Index (By default, indexes are: 0, 1, 2, 3, ...)
data = {"Name": ["Alice", "Bob", "Charlie"],
        "Major": ["CS", "IT", "AI"],
        "GPA": [3.8, 3.5, 3.9]}
df = pd.DataFrame(data, index=["a", "b", "c"])
print(df)

# Displaying DataFrame Information
print("Index Labels:", df.index)
print("Column Names:", df.columns)
print("Convert to Python Lists:", df.columns.tolist())
print("Convert to Dictionary:", df.to_dict())

# Set a Column as the Index
data = {"Name": ["Alice", "Bob", "Charlie"],
        "Major": ["CS", "IT", "AI"],
        "GPA": [3.8, 3.5, 3.9]}
df = pd.DataFrame(data, index=["a", "b", "c"])
df = df.set_index("Name")
print(df)
# Restore Default Index
df = df.reset_index()
print(df)

# Common info
print("Number of Rows:", len(df))
print("Number of Columns:", len(df.columns))
print("Shape of DataFrame:", df.shape)
print("Total Number of Elements:", df.size)

# Retrieve a Column
data = {"Name": ["Alice", "Bob"],
        "Major": ["CS", "IT"]}
df = pd.DataFrame(data)
print(df["Major"])

# Rename Columns
df = df.rename(columns={"Major": "AI"})
print(df)

# DataFrame Information
df.info()

# Statistical Summary
print(df.describe())
print(df.describe(include="all"))  # Include Non-Numerical Columns

# First Rows
print(df.head())  # Default df.head(5)
# Last Rows
print(df.tail())  # Default df.tail(5)

# Indexing and Slicing
data = {"Name": ["Alice", "Bob", "James", "Matt", "Cindy"],
        "Age": [18, 19, 19, 18, 18],
        "Major": ["CS", "IT", "AI", "IT", "AI"]}
df = pd.DataFrame(data)

# Integer-Based Indexing
print("Second row, third column:", df.iloc[1, 2])
# Slicing with iloc
print("Rows 0 and 1; Columns 0 and 1:\n", df.iloc[0:2, 0:2])

# Label-Based Indexing
df = df.set_index("Name")
print(df.loc["Bob", "Major"])
# Slicing with loc
print(df.loc[["Alice", "James"], ["Major"]])

# Filtering a DataFrame
data = {"Name": ["Alice", "Bob", "Charlie", "David"],
        "Major": ["CS", "IT", "CS", "AI"],
        "GPA": [3.8, 3.2, 3.9, 3.5]}
df = pd.DataFrame(data)
print(df)

# Comparative Conditions
print(df[df["GPA"] >= 3.7])

# Logical Conditions
print(df[(df["Major"] == "CS") & (df["GPA"] >= 3.8)])
print(df[(df["Major"] == "AI") | (df["Major"] == "IT")])
print(df[~(df["Major"] == "IT")])

# Subset-Based Conditions
print(df[df["Major"].isin(["CS", "AI"])])

# Boolean conditions
print((df["GPA"] > 3.5).any())
print((df["GPA"] > 3.5).all())

# String Conditions
print(df[df["Name"].str.contains("a")])
print(df[df["Name"].str.startswith("A")])
print(df[df["Name"].str.endswith("d")])

# Sorting a DataFrame
print("Sort by Values:\n", df.sort_values("GPA"))
print("Sort by Values (Descending):\n", df.sort_values("GPA", ascending=False))
print("Sorting by Multiple Columns:\n", df.sort_values(["Major", "GPA"]))
print("Sort by Index:\n", df.sort_index())

# Modifying a DataFrame
df["Status"] = "Active"
print("Adding a Column:\n", df)
df.loc[len(df)] = ["Eve", "DS", 3.7, "Active"]
print("Adding a Row:\n", df)
df = df.drop(columns=["Status"])
print("Removing Columns:\n", df)
df = df.drop(index=1)
print("Removing Rows:\n", df)

# Removes a column and returns it as a Series.
major_column = df.pop("Major")
print("Removes a column:\n", major_column)

# All rows receive the same value.
df["GPA"] = 4.0
print("Updating an Entire Column:\n", df)

# Suppose we only want to update CS students.
data = {"Name": ["Alice", "Bob", "Charlie", "David"],
        "Major": ["CS", "IT", "CS", "AI"],
        "GPA": [3.8, 3.2, 3.9, 3.5]}
df = pd.DataFrame(data)
# Only matching rows are modified.
df.loc[df["Major"] == "CS", "GPA"] = 4.0
print("Updating Selected Rows:\n", df)

# Creating a New DataFrame with Filtering
honor_students = df[df["GPA"] >= 3.8]
print(honor_students)

# Data Types in DataFrame
print(type(df))
print(df.dtypes)
print(df.select_dtypes(include=["number"]))
print(df.select_dtypes(include=["object"]))

# Statistical Methods
data = {"A": [1, 2, 3], "B": [4, 5, 6]}
df = pd.DataFrame(data)
print(df + 10)

# Arithmetic Operations
print("Add:\n", df["A"].add(df["B"]))
print("\nSubtract:\n", df["A"].sub(df["B"]))
print("\nMultiply:\n", df["A"].mul(df["B"]))
print("\nDivide:\n", df["A"].div(df["B"]))

# Descriptive Statistics
print("Sum:\n", df.sum())
print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Mode:\n", df.mode())
print("Quantile:\n", df.quantile(0.5))
print("Max:\n", df.max())
print("Min:\n", df.min())
print("Variance:\n", df.var())
print("Standard Deviation:\n", df.std())

# Largest values and smallest values
print("Largest values:\n",df.nlargest(2, "A"))
print("Smallest values:\n",df.nsmallest(2, "A"))

# Counting Values
print("Count Non-Null Values:\n", df.count())
# For a Series
print("Count Unique Values:\n", df["A"].value_counts())

# Applying Functions
print(df["A"].apply(lambda x: x * 2))
