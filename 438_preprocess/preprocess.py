# define dependencies
import pandas as pd

# Load the dataset
df = pd.read_csv('example_dataset.csv')

# Perform data preprocessing and feature engineering steps

# Step 1. Handle missing values by adding mean
df.fillna(df.mean(), inplace=True)

# Step 2. Remove duplicates (if there are any)
df.drop_duplicates(inplace=True)

# Step 3. Engineer new features
df['feature_6'] = df['feature_2'] * df['feature_5']

# Save the preprocessed dataset
df.to_csv('preprocessed_dataset.csv', index=False)

# Notify progress
print('Preprocessing completed and the dataset is saved as "preprocessed_dataset.csv".')