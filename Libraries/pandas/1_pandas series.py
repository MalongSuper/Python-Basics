# Python Pandas Series
import pandas as pd

data = ["Alice", "Bob", "Charlie"]
s = pd.Series(data)
print(s)


# Creating a Series from a List
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)

# Giving the Series a Name
data = [10, 20, 30, 40]
s = pd.Series(data, name="Scores")
print(s)

# Custom Index Labels
data = [85, 90, 95]
s = pd.Series(data, index=["Alice", "Bob", "Charlie"])
print(s)

# Creating a Series from a Dictionary
data = {"Alice": 85, "Bob": 90, "Charlie": 95}
s = pd.Series(data)
print(s)

# Renaming a Series
data = [100, 90, 80]
s = pd.Series(data, index=["A", "B", "C"])
s = s.rename(index={"A": "Alice"})
print(s)

# Changing the Series name
s.name = "Exam Scores"
print(s)

# Series Size and Shape
data = [10, 20, 30, 40]
s = pd.Series(data)
print("Number of Rows:", len(s))
print("Total Number of Elements:", s.size)
print("Shape of a Series:", s.shape)

# Traversing Through a Series
data = [85, 90, 95]
s = pd.Series(data, index=["Alice", "Bob", "Charlie"])
for key, value in s.items():
    print(key, value)

# Filtering a Series
data = [60, 75, 90, 55, 88]
s = pd.Series(data)
print(s[s >= 80])

# Insertion and Deletion
data = [10, 20, 30]
s = pd.Series(data)
s[3] = 40
print("Insert a new value:\n", s)

s = s.drop(1)
print("Delete a value:\n", s)

# Keys and Values
data = [85, 90, 95]
s = pd.Series(data, index=["Alice", "Bob", "Charlie"])
print("Retrieve Index Labels:", s.keys())
print("Retrieve Values:", s.values)
print("Retrieve Value from Key:", s["Bob"])
print("Retrieve Key from Value:", s[s == 95].index)

# Indexing and Slicing
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print("Position-Based Indexing:", s.iloc[2])
print("Access Index Label by Position:", s.index[2])
print("Slicing:", s.iloc[1:4])

# Unique Values
data = [10, 20, 20, 30, 30, 30]
s = pd.Series(data)
print("Unique:", s.unique())

# Sorting a Series
data = [50, 20, 80, 10]
s = pd.Series(data)
print("Sort by Values:\n", s.sort_values())
print("Sort by Index:\n", s.sort_index())

# Converting a Series to a DataFrame
data = [100, 90, 80]
s = pd.Series(data, name="Scores")
df = s.to_frame()
print(df)

# From Series to DataFrame and Back
data = {"Name": ["Alice", "Bob", "Charlie"],
        "Score": [85, 90, 95]}
df = pd.DataFrame(data)
print(df)

# Retrieving a single column from a DataFrame produces a Series.
scores = df["Score"]
print(type(scores))
print(scores)
