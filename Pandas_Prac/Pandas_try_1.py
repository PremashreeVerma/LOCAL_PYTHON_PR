import pandas as pd
s=pd.Series([1,2,3,4,5])
print(s)
print(s.dtype)
print()
print()
s.name="series"
print(s.name)
f=pd.Series(['a','b','c','d','e'])
print(f)
print(f[0:3])
print(f.iloc[3])
print(f.iloc[[3,4,1]])
print(f.dtype)
index=['1st','2nd','3rd','4th','5th']
s.index=index
print("pandas is successfully imported")
print(s)

