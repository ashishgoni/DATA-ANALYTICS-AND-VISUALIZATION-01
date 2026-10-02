
import numpy as np
import pandas as pd
arr = np.array([15, 25, 35, 45, 55])
print('Array:', arr)
print('Mean:', arr.mean())
print('Reshaped 2D:\n', arr.reshape(5,1))
print('Sliced (index 1 to 3):', arr[1:4])
data = {
    'Name': ['Arjun', 'Sneha', 'Rahul', 'Priya'],
    'Marks': [82, 76, 95, 68],
    'Branch': ['ISE', 'CSE', 'ECE', 'AIML']
}
df = pd.DataFrame(data)
print(df)
print('\nFirst 2 rows:\n', df.iloc[0:2])
print('\nMarks column:\n', df['Marks'])
print('\nRows where Marks > 70:\n', df[df['Marks'] > 70])