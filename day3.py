# Libraries
import pandas as pd

# UCI Heart disease dataset URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

# Correct column names for the heart dataset
columns = [
    'age','sex','cp','trestbps','chol','fbs','restecg',
    'thalach','exang','oldpeak','slope','ca','thal','target'
]

# Load dataset
df = pd.read_csv(url, names=columns)

print("Original Dataset:")
display(df)

# Replace missing values represented by '?'
df.replace("?", pd.NA, inplace=True)

print("\nMissing values replaced:")
display(df)

# Count missing values per column
mis_val = df.isna().sum()
print("\nMissing values per column:")
print(mis_val)

print("\nTotal missing values:", mis_val.sum())

# Convert numeric columns to proper numeric types
df['ca'] = pd.to_numeric(df['ca'], errors='coerce')
df['thal'] = pd.to_numeric(df['thal'], errors='coerce')

# Calculate means
mean_ca = df['ca'].mean()
mean_thal = df['thal'].mean()

print("\nMean of 'ca':", mean_ca)
print("Mean of 'thal':", mean_thal)

# Fill missing numeric values
df['ca'].fillna(mean_ca, inplace=True)
df['thal'].fillna(mean_thal, inplace=True)

print("\nAfter filling missing values:")
display(df)

# Count duplicate rows
dup_count = df.duplicated().sum()
print("\nDuplicate Rows:", dup_count)

# Remove duplicates
if dup_count > 0:
    print("\nDuplicated rows:")
    display(df[df.duplicated()])
    
    df_clean = df.drop_duplicates()
    print("\nAfter removing duplicates:")
    display(df_clean)
else:
    print("No duplicate rows found.")
