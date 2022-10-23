import pandas as pd

df=pd.read_csv('total_stars.csv')
print(df.columns)

df.drop(df.columns[[0,6,7,8,9,10,11]],axis=1,inplace=True)
print(df.columns)

df.to_csv('cleaned.csv')