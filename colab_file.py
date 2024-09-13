# -*- coding: utf-8 -*-
"""colab file.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HMRW9ZoO4LawisueKFK2TZlcDjBx175w
"""

# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Step 2: Load the dataset
# Assuming you have a CSV file named 'student_health_data.csv'
file_path = 'Impact_of_Mobile_Phone_on_Students_Health.csv'
df = pd.read_csv('C:/Users/pathi/Documents/New folder/Impact_of_Mobile_Phone_on_Students_Health(1).csv')


df.head()

# Data Understanding
print("Initial Dataset Overview:")
print(df.head())

print("Dataset Shape:", df.shape)

print("Data Types:\n", df.dtypes)

print(df.to_string())

# Data Exploration
print("\nDataset Information:")
print(df.info())

print("\nBasic Statistics Summary:")
print(df.describe(include='all'))

# Step 4: Handle Missing Values
imputer = SimpleImputer(strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Identify Data Problems
# Check for missing values
print("Missing Values:\n", df.isnull().sum())
print("\nMissing Values in Each Column:")

# Visualize missing values
plt.figure(figsize=(10, 5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Check for duplicate records
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate records: {duplicates}")

# Handle missing values (e.g., filling with median, mean, or mode)
df = df.fillna(df.median(numeric_only=True))

# Drop duplicate records
df = df.drop_duplicates()

# Assuming that 'df' is the DataFrame you intended to copy
Original_data = df.copy()

# Check the column names of the DataFrame
print(df.columns)

# Convert string columns to numerical representations
# First you need to identify columns with string values
for col in df_imputed.columns:
  if df_imputed[col].dtype == 'object':
    print(f"Column {col} contains string values.")

# Step 5: Convert Categorical to Numerical
label_encoders = {}
for column in df_imputed.select_dtypes(include=['object']).columns:
    if df_imputed[column].nunique() < 10:  # only encode categorical columns
        le = LabelEncoder()
        df_imputed[column] = le.fit_transform(df_imputed[column])
        label_encoders[column] = le

# Step 6: Normalize Numerical Columns
scaler = StandardScaler()
numerical_columns = df_imputed.select_dtypes(include=[np.number]).columns
df_imputed[numerical_columns] = scaler.fit_transform(df_imputed[numerical_columns])

# Step 6: Normalize Numerical Columns
from sklearn.preprocessing import StandardScaler

# Identify numerical columns in the dataset
numerical_columns = df_imputed.select_dtypes(include=[np.number]).columns

# Initialize StandardScaler
scaler = StandardScaler()

# Identify numerical columns in the dataset
numerical_columns = df_imputed.select_dtypes(include=[np.number]).columns

# Initialize StandardScaler
scaler = StandardScaler()

# Fit the scaler on numerical columns and transform
df_imputed[numerical_columns] = scaler.fit_transform(df_imputed[numerical_columns])

# Display the normalized dataset
print("\nNormalized Data (first few rows):")
print(df_imputed.head())

# Step 7: Visualize Data to Identify Outliers
plt.figure(figsize=(10, 8))
sns.boxplot(data=df_imputed)
plt.xticks(rotation=90)
plt.title("Outliers in the Dataset")
plt.show()

# Visualize the distribution of key variables
sns.countplot(x='Age', data=df) # Changed 'Age' to 'Gender' to match the title of the plot
plt.title('Gender Distribution')
plt.show()

sns.countplot(x='Daily usages', data=df)
plt.title('Mobile Operating System Distribution')
plt.show()

sns.countplot(x='Mobile phone use for education', data=df)
plt.title('Mobile Operating System Distribution')
plt.show()

imputedData = df  # Rename df to imputedData
sns.displot(imputedData["Helpful for studying"])

import matplotlib.pyplot as plt
import pandas as pd

# Load your data into the imputedData variable
imputedData = pd.read_csv('/content/Impact_of_Mobile_Phone_on_Students_Health.csv')

# Print the actual column names to inspect them
print(imputedData.columns)

# Access columns using their actual names (replace with actual names from the output above)
plt.figure(figsize=(6, 6))
plt.pie(imputedData['Age'].value_counts(),  # Replace 'Age' with the actual column name
        labels=imputedData['Age'].value_counts().index,  # Replace 'Age' with the actual column name
        autopct='%1.1f%%',
        startangle=90)
plt.title('Distribution of Age')  # Update the title accordingly
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Repeat for other categorical columns as needed
# For example:
plt.figure(figsize=(6, 6))

# Access the column using its actual name from the DataFrame
plt.pie(imputedData['Mobile phone use for education'].value_counts(),
        labels=imputedData['Mobile phone use for education'].value_counts().index,
        autopct='%1.1f%%',
        startangle=90)

# Update the title to reflect the actual column name
plt.title('Distribution of Mobile phone use for education')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
imputedData = pd.read_csv('/content/Impact_of_Mobile_Phone_on_Students_Health.csv')

# Columns to be converted to numeric
columns_to_convert = ['Age', 'Mobile phone use for education', 'Mobile phone activities']

# Convert columns to numeric, coercing errors to NaN
for col in columns_to_convert:
    imputedData[col] = pd.to_numeric(imputedData[col], errors='coerce')

# Plot boxplots for each column
plt.figure(figsize=(15, 12))  # Larger figure to accommodate multiple subplots

for i, col in enumerate(columns_to_convert, 1):
    plt.subplot(3, 1, i)  # Create subplots for each variable
    plt.boxplot(imputedData[col].dropna())
    plt.title(f'Boxplot of {col}')
    plt.ylabel(col)
    plt.grid(True)

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Step 8: Apply Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df_imputed['Cluster'] = kmeans.fit_predict(df_imputed[numerical_columns])

# Step 9: Evaluate Clustering Performance
print("\nCluster Centers:")
print(kmeans.cluster_centers_)
score = silhouette_score(df_imputed[numerical_columns], df_imputed['Cluster'])
print(f"\nSilhouette Score: {score}")

# Step 10: Visualize Clustering Results
sns.pairplot(df_imputed, hue='Cluster')
plt.show()

# Feature Scaling
scaler = StandardScaler()
numeric_cols = ['Daily usages']

# Convert 'Daily usages' to numeric values - assuming hours
# Use a regular expression to remove non-numeric characters from the beginning of the string
df['Daily usages'] = df['Daily usages'].str.split('-').str[0].str.replace(r'[^0-9.]', '', regex=True).str.strip().astype(float)

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Splitting the data into Training and Testing sets
X = df.drop(columns=['Names'])

# Check the available columns after one-hot encoding
print(df.columns)

# Check if 'Performance impact_Agree' exists
if 'Performance impact_Agree' in df.columns:
    y = df['Performance impact_Agree']  # Target variable
else:
    # Handle the case where the column doesn't exist
    # For example, print an error message and identify potential target variables
    print(f"Column 'Performance impact_Agree' not found! Available columns are: {df.columns}")
    # Choose a different target variable based on available columns
    y = df['Helpful for studying'] # Example: Replace with an actual target variable from df.columns

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Import the necessary module
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Impact_of_Mobile_Phone_on_Students_Health.csv')

# Display column names
print("Columns in the dataset:", df.columns)

# Identify target variable
if 'Performance impact_Agree' not in df.columns:
    print(f"Column 'Performance impact_Agree' not found! Available columns are: {df.columns}")
    y_col = 'Helpful for studying'  # Replace with an actual target variable from df.columns
else:
    y_col = 'Performance impact_Agree'

# Check for missing values in 'Daily usages' and y_col
print("Missing values in 'Daily usages':", df['Daily usages'].isnull().sum())
print("Missing values in target variable '{}':".format(y_col), df[y_col].isnull().sum())

# Convert target variable to numeric if it's categorical
if df[y_col].dtype == 'object':
    df[y_col] = df[y_col].map({'Agree': 1, 'Disagree': 0})

# Drop rows with missing values in either column
df = df.dropna(subset=['Daily usages', y_col])

# Plot boxplot
sns.boxplot(x='Daily usages', y=y_col, data=df)
plt.title('Daily Usages vs. Performance Impact')
plt.xlabel('Daily Usages')
plt.ylabel('Performance Impact')
plt.show()

# Step 8: Save the cleaned dataset
df_imputed.to_csv('Cleaned_Impact_of_Mobile_Phone_on_Students_Health.csv', index=False)
