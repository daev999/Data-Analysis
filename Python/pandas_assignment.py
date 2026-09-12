import random
import numpy as np
import pandas as pd

# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=["A", "B", "C","D"])
print("Original DataFrame:")
print(df)

# # Set the index to be the first column
df.set_index('A', inplace=True)
print("DataFrame with new index:")
print(df)

# 2. Create a Pandas DataFrame with columns 'A', 'B', 'C' and index 'X', 'Y', 'Z'. Fill the DataFrame with random integers and access the element at row
# 'Y' and column 'B'.
df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=["A", "B", "C"], index=["X", "Y", "Z"])
print("Original DataFrame")
print(df)

# Access the element at row 'Y' and column 'B'.
element = df.at["Y", "B"]
print(f"Element at row 'Y' and column 'B':{element}")

# Assignment 2: DataFrame Operations

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Add a new column that is the product of the first two columns.
# 2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. Compute the row-wise and column-wise sum.

# Assignment 3: Data Cleaning

# 1. Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers. Introduce some NaN values. Fill the NaN values with the mean
# of the respective columns.
# 2. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Introduce some NaN values. Drop the rows with any NaN
# values.