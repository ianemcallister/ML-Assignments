# define dependencies
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# load the dataset
df = pd.read_csv('exampledataset2.csv')

# Extract features
x = df['text']
y = df['sentiment']

# Assign trainging and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Init Convetorizer
vectorizer = CountVectorizer()

# Fit the vectorizer on the training data and transform the data into feature vecotrs
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

# init the model
model = SVC()

# Train the model
model.fit(x_train_vectorized, y_train)

# Make predictions
y_pred = model.predict(x_test_vectorized)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the model
print(f"Accuracy: {accuracy:.2f}")