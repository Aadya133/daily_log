import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("student_clustering.csv")

print(df.head())
print(df.describe())

print(df.isna().sum())
