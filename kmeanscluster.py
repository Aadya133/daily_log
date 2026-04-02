import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#loading the dataset
df=pd.read_csv("income.csv")

#information of database
print(df.head())
print(df.describe())

#checking for null values
print(df.isna().sum())

#Plot of age and income
plt.scatter(df['Age'], df['Income'])
plt.show()

# Clustering
km=KMeans(n_clusters=3)
y_predict=km.fit_predict(df[['Age','Income']])
print(y_predict)

#Adding a new cluster column to dataframe
df['Cluster']=y_predict
print(df.head())

#Dataframe for each cluster
df1=df[df.Cluster==0]
df2=df[df.Cluster==1]
df3=df[df.Cluster==2]

#Plotting Each cluster dataframe
plt.scatter(df1.Age,df1['Income'],color='green')
plt.scatter(df2.Age,df2['Income'],color='orange')
plt.scatter(df3.Age,df3['Income'],color='blue')
plt.show()
#Graph issue solving - scaling

#-----------Scaling------------ 
ss=StandardScaler()
scaled_data=ss.fit_transform(df[['Age','Income']])
scaled_df=pd.DataFrame(scaled_data,columns=['Age','Income'])
print(scaled_df.head())

#fiting scaled data
km=KMeans(n_clusters=3)
y_predict=km.fit_predict(scaled_df[['Age','Income']])
print(y_predict)

#Cluster column
scaled_df['Cluster']=y_predict
print(df.head())

#Dataframe
df1=scaled_df[scaled_df.Cluster==0]
df2=scaled_df[scaled_df.Cluster==1]
df3=scaled_df[scaled_df.Cluster==2]

#Plotting Each cluster of scaled dataframe
plt.scatter(df1.Age,df1['Income'],color='green')
plt.scatter(df2.Age,df2['Income'],color='orange')
plt.scatter(df3.Age,df3['Income'],color='blue')
plt.show()