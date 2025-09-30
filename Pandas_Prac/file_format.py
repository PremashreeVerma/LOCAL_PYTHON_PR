import pandas as pd
data= {"Name":['Ram','Shyam','Puja'],
       "Age":['12','15','13'],
       "City":['Delhi','Mumbai','Kolkata']
       }
df=pd.DataFrame(data)
print(df)

# df.to_csv("pandas_output.csv",index=False)
# df.to_excel("pandas_output.xlsx",index=False)
df.to_json("pandas_output.json",index=False)
