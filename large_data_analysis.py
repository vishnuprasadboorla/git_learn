# Just trying to make some chnages to see it in inspect

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import datetime

# Here If you can see I AM MAKING CHANGES TO FILE THAT WE SAVED FROM GITHUB. So, to push these code changes back to GitHub, I can do it using by clicking the "main" which is on left.

# Thats ok to find some peace in coding, thats it.

# Generate a large random dataset
def generate_large_dataset(rows=1000000, cols=10):
    np.random.seed(42)
    data = np.random.rand(rows, cols)
    columns = [f'Feature_{i}' for i in range(cols)]
    df = pd.DataFrame(data, columns=columns)
    df['Timestamp'] = pd.date_range(start='1/1/2020', periods=rows, freq='T')
    df['Category'] = np.random.choice(['A', 'B', 'C', 'D'], size=rows)
    return df

# Perform some data analysis
def analyze_data(df):
    print("Basic Statistics:")
    print(df.describe())
    print("\nCategory Distribution:")
    print(df['Category'].value_counts())
    
    # Plot feature distribution
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Feature_0'], bins=50, kde=True)
    plt.title('Feature_0 Distribution')
    plt.show()

# Apply complex transformations
def transform_data(df):
    df['Feature_Sum'] = df.iloc[:, :-2].sum(axis=1)
    df['Feature_Mean'] = df.iloc[:, :-2].mean(axis=1)
    df['Feature_Std'] = df.iloc[:, :-2].std(axis=1)
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month
    df['Day'] = df['Timestamp'].dt.day
    return df

# Execute pipeline
def main():
    start_time = time.time()
    df = generate_large_dataset()
    print("Dataset Generated")
    df = transform_data(df)
    print("Data Transformed")
    analyze_data(df)
    end_time = time.time()
    print(f"Total Execution Time: {end_time - start_time:.2f} seconds")

# this is the end of the code. Just to test databricks git integration functionality
print(f"this is to inform you that code executed succesfully. Byeeeee")

if __name__ == "__main__":
    main()