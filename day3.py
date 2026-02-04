#libraries
import pandas as pd

#UCI Heart disease dataset url
url="https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

#defining column header
columns=[
    'id','sepallength','sepalwidth',
    'petalength','petalwidth','species'
]

#load the dataset
df=pd.read_csv(path,names=columns)

display(df)

#replace the missing values
df.replace("?",pd.NA, inplace=True)

#print the dataset
display(df)

#count missing values
mis_val=df.isna().sum()
print("Missing values in each column ")
print(mis_val)

#total missing values
print("\nTotal missing values  :",mis_val.sum())

#conversion
df['ca']=pd.to_numeric(df['ca'])
df['thal']=pd.to_numeric(df['thal'])

#mean
mean_ca=df['ca'].mean()
mean_thal=df['thal'].mean()
print("Mean ca: ",mean_ca)
print("Mean thal : ", mean_thal)

#replace na
df['ca'].fillna(mean_ca,inplace=True)
df['thal'].fillna(mean_thal,inplace=True)

#display
display(df)

#duplicate rows
dup_count=df.duplicated().sum()
print("Duplicate Rows ",dup_count)

#delete duplicate rows
if(dup_count>0):
  print("Duplicated rows :")
  display(df[df.duplicated()])
  df_clean=df.drop_duplicates()
  print("After deleting duplicate rows")
  display(df)
else:
  print("No duplicate rows")



