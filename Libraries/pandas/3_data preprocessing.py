# The process of preparing data for analysis
# is known as data preprocessing.
import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"],
        "GPA": [3.8, None, 3.9]}
df = pd.DataFrame(data)
print(df)

# Detect Missing Values -> isna() or isnull()
print(df.isna())

# Fill in the missing value with mean
df["GPA"] = df["GPA"].fillna(df["GPA"].mean())
print(df)

# Dropping Missing Values
print(df.dropna())

# Retrieve Unique Values
data = {"Major": ["CS", "IT", "CS", "AI", "IT"]}
df = pd.DataFrame(data)
print(df["Major"].unique())

# Count Unique Values
print(df["Major"].nunique())

# Detect Duplicates: returns True
print(df.duplicated())

# Remove Duplicates: By default, the first occurrence is kept.
print(df.drop_duplicates())

# Replacing Values
data = {"Major": ["CS", "IT", "AI"]}
df = pd.DataFrame(data)
df = df.replace({"CS": "Computer Science"})
print(df)

# Mapping Values
data = {"Major": ["CS", "IT", "AI"]}
df = pd.DataFrame(data)
encoding = {"CS": 0, "IT": 1, "AI": 2}
df["Major_Code"] = df["Major"].map(encoding)
print(df)

# One-Hot Encoding
data = {"Major": ["CS", "IT", "AI"]}
df = pd.DataFrame(data)
encoded = pd.get_dummies(df)
print(encoded)

# Merging: Combines DataFrames based on one or more common columns.
students = pd.DataFrame({"ID": [1, 2, 3],
                         "Name": ["Alice", "Bob", "Charlie"]})
scores = pd.DataFrame({"ID": [1, 2, 3],
                       "GPA": [3.8, 3.5, 3.9]})
result = students.merge(scores, on="ID")
print(result)

# Joining: Combines DataFrames using their indexes.
df1 = pd.DataFrame({"Name": ["Alice", "Bob"]}, index=[1, 2])
df2 = pd.DataFrame({"GPA": [3.8, 3.5]}, index=[1, 2])
print(df1.join(df2))

# Aggregation: Groups data and calculates statistical summaries.
data = {"Major": ["CS", "CS", "IT"],
        "GPA": [3.8, 3.6, 3.5]}
df = pd.DataFrame(data)
print(df.groupby("Major")["GPA"].mean())

# Concatenation: Combines DataFrames vertically or horizontally.
df1 = pd.DataFrame({"A": [1, 2]})
df2 = pd.DataFrame({"A": [3, 4]})
result = pd.concat([df1, df2])
print(result)

# Segmentation: Segmentation divides continuous numerical values
# into ranges (bins).
scores = [55, 68, 75, 88, 95]
grades = pd.cut(scores, bins=[0, 60, 70, 80, 100],
                labels=["F", "D", "C", "A"])
print(grades)
