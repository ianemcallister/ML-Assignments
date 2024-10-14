# Define dependencies
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress Tensorflow info/warnings

import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from sklearn.model_selection import train_test_split

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the images
x_train = x_train / 255.0
x_test = x_test / 255.0

# Split the dataset into training and validation sets
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

# Define the neural network architecture
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))  # Set the input shape to (28, 28) for MNIST images
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))

# Add output layer (since MNIST has 10 classes)
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (no .values needed)
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))

# Evaluate the model on the test set (no .values needed)
test_loss, accuracy = model.evaluate(x_test, y_test)
print(f'Test Loss: {test_loss:.4f}, Accuracy: {accuracy:.4f}')
