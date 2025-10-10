# PANDAS -- Pandas is one of the most widely used libraries in python for Data manipulation and Analysis.
#           It provides data structures and functions needed to manipulate structured data.

# In pandas, there are two primary data structures:
# 1. Series: A one-dimensional labeled array capable of holding any data type.
# 2. DataFrame: A two-dimensional labeled data structure with rows and columns similar to an Excel sheet.

import pandas as pd

data = {
    'Name': ['pandu', 'Bob', 'bhAAi', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['AP', 'Mumbai', 'Bangalore', 'chennai']
}
df = pd.DataFrame(data)
print(df)

# Accessing a specific column
print(df['Name'])
# Accessing a specific row by index
print(df.iloc[1])   # iloc is used for index-based access
# Accessing a specific row by label
print(df.loc[1])    # loc is used for label-based access    

# Adding a new column
df['Country'] = ['India', 'India', 'India', 'India']
print(df)

# Deleting a column
df.drop('Country', axis=1, inplace=True)
print(df)

# Filtering data
print(df[df['Age'] > 25])

# Sorting data
print(df.sort_values(by='Age'))

# Descriptive statistics
print(df.describe())

# Handling missing data
df.loc[4] = [None, None, None]  # Adding a row with missing values
print(df)
print(df.isnull())  # Checking for null values
print(df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'}))  # Filling missing values
print(df.dropna())  # Dropping rows with missing values

# Reading from a CSV file
# df = pd.read_csv('file.csv')
# print(df)

