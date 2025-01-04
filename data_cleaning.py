import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.
    
    Parameters:
    - file_path (str): The path to the data file.
    
    Returns:
    - DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def inspect_data(data):
    """
    Prints a summary of the dataset, including info, head, and basic statistics.
    
    Parameters:
    - data (DataFrame): The DataFrame to inspect.
    """
    print("Dataset Info:")
    print(data.info())
    print("\nFirst 5 Rows:")
    print(data.head())
    print("\nDataset Summary Statistics:")
    print(data.describe())

def handle_missing_values(data, strategy="mean", columns=None):
    """
    Handles missing values in specified columns of the DataFrame.
    
    Parameters:
    - data (DataFrame): The DataFrame to process.
    - strategy (str): The strategy to handle missing values ('mean', 'median', 'mode', or 'drop').
    - columns (list): List of columns to apply the strategy to. If None, applies to all columns.
    
    Returns:
    - DataFrame: Updated DataFrame with missing values handled.
    """
    if columns is None:
        columns = data.columns
    
    for col in columns:
        if data[col].isnull().sum() > 0:
            if strategy == "mean":
                data[col].fillna(data[col].mean(), inplace=True)
            elif strategy == "median":
                data[col].fillna(data[col].median(), inplace=True)
            elif strategy == "mode":
                data[col].fillna(data[col].mode()[0], inplace=True)
            elif strategy == "drop":
                data.dropna(subset=[col], inplace=True)
            else:
                print(f"Unknown strategy: {strategy}. Skipping column: {col}")
    return data

def remove_duplicates(data):
    """
    Removes duplicate rows from the dataset.
    
    Parameters:
    - data (DataFrame): The DataFrame to process.
    
    Returns:
    - DataFrame: Updated DataFrame with duplicates removed.
    """
    initial_count = data.shape[0]
    data.drop_duplicates(inplace=True)
    final_count = data.shape[0]
    print(f"Removed {initial_count - final_count} duplicate rows.")
    return data

def validate_columns(data, required_columns):
    """
    Ensures that required columns are present in the dataset.
    
    Parameters:
    - data (DataFrame): The DataFrame to validate.
    - required_columns (list): List of column names that must be present.
    
    Returns:
    - bool: True if all required columns are present, False otherwise.
    """
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Missing required columns: {missing_columns}")
        return False
    print("All required columns are present.")
    return True

def detect_outliers(data, column, method="iqr"):
    """
    Detects outliers in a given column using the specified method.
    
    Parameters:
    - data (DataFrame): The DataFrame to process.
    - column (str): The column to analyze for outliers.
    - method (str): The method to detect outliers ('iqr' or 'zscore').
    
    Returns:
    - DataFrame: Rows considered as outliers.
    """
    if method == "iqr":
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    elif method == "zscore":
        mean = data[column].mean()
        std = data[column].std()
        z_scores = (data[column] - mean) / std
        outliers = data[np.abs(z_scores) > 3]
    else:
        print(f"Unknown method: {method}. No outliers detected.")
        return pd.DataFrame()
    
    print(f"Detected {len(outliers)} outliers in column '{column}'.")
    return outliers

def standardize_column_names(data):
    """
    Standardizes column names to lowercase and replaces spaces with underscores.
    
    Parameters:
    - data (DataFrame): The DataFrame to process.
    
    Returns:
    - DataFrame: Updated DataFrame with standardized column names.
    """
    data.columns = data.columns.str.lower().str.replace(' ', '_')
    print("Column names standardized.")
    return data

def feature_engineering(data):
    """
    Adds engineered features to the dataset, such as age of building and height categories.
    
    Parameters:
    - data (DataFrame): The DataFrame to process.
    
    Returns:
    - DataFrame: Updated DataFrame with new features.
    """
    current_year = pd.Timestamp.now().year
    data['building_age'] = current_year - data['year_completed']
    data['height_category'] = pd.cut(data['height_(m)'], bins=[0, 150, 300, 600], labels=['Low', 'Medium', 'High'])
    print("Feature engineering completed. Added 'building_age' and 'height_category'.")
    return data

def normalize_column(data, column):
    """
    Normalizes a column to a 0-1 scale.
    
    Parameters:
    - data (DataFrame): The DataFrame to process.
    - column (str): The column to normalize.
    
    Returns:
    - DataFrame: Updated DataFrame with the normalized column.
    """
    min_val = data[column].min()
    max_val = data[column].max()
    data[column + '_normalized'] = (data[column] - min_val) / (max_val - min_val)
    print(f"Column '{column}' normalized to 0-1 scale.")
    return data

def save_cleaned_data(data, output_path):
    """
    Saves the cleaned data to a CSV file.
    
    Parameters:
    - data (DataFrame): The DataFrame to save.
    - output_path (str): The file path to save the data to.
    """
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}.")
