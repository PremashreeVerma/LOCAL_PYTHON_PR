import pandas as pd
import numpy as np 

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],  
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'salary': [70000, 80000, 60000, 90000]
}
df=pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
print ("DataFrame from dictionary:")
print(df)
print (df.dtypes)

data_list = [
    ['Eve', 29, 'Phoenix', 75000], 
    ['Frank', 33, 'Philadelphia', 82000],
    ['Grace', 26, 'San Antonio', 68000],
    ['Hannah', 31, 'San Diego', 91000]
]
# df_list=pd.DataFrame(data_list, columns=['Name', 'Age', 'City', 'salary'])
df_list=pd.DataFrame(data_list)
print("\nDataFrame from list of lists:")
print(df_list)

df_list=pd.DataFrame(data_list, columns=['Name', 'Age', 'City', 'salary'])
print("\nDataFrame from list of lists with column name:")
print(df_list)
print (df_list.dtypes)