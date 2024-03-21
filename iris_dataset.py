import pandas as pd
import joblib

# Assuming the correct column names
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Load the dataset with proper column names
iris_data = pd.read_csv('iris.data.csv', names=column_names)

# Check the first few rows to verify
print(iris_data.head())

print(iris_data.head())
print(iris_data.info())

X = iris_data.drop('species', axis=1)  # Features
y = iris_data['species']  # Target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

# Initialize the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

# Predict on the testing data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a file named "iris_model.pkl"
joblib.dump(model, 'iris_model.pkl')