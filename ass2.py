import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
file_path = r'C:\Users\bilal\Downloads\diabetes_modified.csv'
if os.path.exists(file_path):
    print("File found.")
else:
    print("File not found. Please check the file path.")
data = pd.read_csv(file_path)

# Columns where zero values don't make sense
cols_to_check = ['Pregnancies','Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction' , 'Age', 'Outcome']

# Replace zero values with NaN in the specified columns
data[cols_to_check] = data[cols_to_check].replace({0: np.nan})

# Fill NaN values with the median of each column
data[cols_to_check] = data[cols_to_check].fillna(data[cols_to_check].median())

# Separating the features and the target variable
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Fold Cross-Validation
kf = KFold(n_splits=10, shuffle=True, random_state=42)

# KNN Classifier
knn = KNeighborsClassifier()
knn_scores = cross_val_score(knn, X_scaled, y, cv=kf)

# Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=42)
dt_scores = cross_val_score(dt, X_scaled, y, cv=kf)

# Display the results
print(f"KNN Scores: {knn_scores}")
print(f"KNN Mean Score: {knn_scores.mean()}")

print(f"Decision Tree Scores: {dt_scores}")
print(f"Decision Tree Mean Score: {dt_scores.mean()}")
