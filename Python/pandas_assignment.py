import random
import numpy as np
import pandas as pd

# Assignment 1:
# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers
# df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=["A", "B", "C","D"])
# print("Original DataFrame:")
# print(df)

# Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. Fill the DataFrame with random integers and access the element at row
# 'Y' and column 'B'.
# df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=["A", "B", "C"], index=["X", "Y", "Z"])
# print("Original DataFrame")
# print(df)

# Access the element at row 'Y' and column 'B'.
# element = df.at["Y", "B"]
# print(f"Element at row 'Y' and column 'B':{element}")

# Assignment 2: DataFrame Operations
# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Add a new column that is the product of the first two columns.
# df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)))
# print("Original DataFrame:")
# print(df)

# Add a new column that is the product of the first two columns.
# df["new_col"] = df[0].mul(df[1])
# print("Original DataFrame:")
# print(df)

# 2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. 
# - Compute the row-wise and column-wise sum.
# df = pd.DataFrame(np.random.randint(1, 100, size=(4, 3)))

# Compute sums
# column_sums = np.sum(df, axis=0)   # one total per column
# row_sums = np.sum(df, axis=1)      # one total per row

# print("Column sums:", column_sums)
# print("Row sums:", row_sums)

# Assignment 3: Data Cleaning

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Introduce some NaN values. Fill the NaN values with the mean
# of the respective columns.
df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)))
print("Original Dataframe")

# Introduce some NaN values. 
df.loc[0, 0] = np.nan
df.loc[1, 1] = np.nan

# Fill the NaN values with the mean
df[0] = df[0].fillna(df[0].mean())
df[1] = df[1].fillna(df[1].mean())

print("\nUpdated Dataframe") 
print(df)

# 2. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Introduce some NaN values. Drop the rows with any NaN
# values.