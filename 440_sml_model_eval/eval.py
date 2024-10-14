# define dependencies
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('exampledataset1.csv')

# Split the dataset into features (x) and target (y)
x = df.drop('Target', axis=1)
y = df['Target']

# Split the data into traingin and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Init the lgistic regression model
model = LogisticRegression()

# Train the model
model.fit(x_train, y_train)

# Make Predictions on the testing set
y_pred = model.predict(x_test)

# Evaluate the model's Performance
accuracy = accuracy_score(y_test, y_pred)

# Notify progress
print(f"Accuracy Score: {accuracy:.4f}")