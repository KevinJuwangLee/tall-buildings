import pandas as pd

def load_data(file_path='tallest_buildings_cleaned.csv'):
    """
    Load the cleaned dataset.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None

def check_missing_values(df):
    """
    Check for missing values in the dataset.
    """
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("Missing values detected:")
        print(missing_values[missing_values > 0])
    else:
        print("No missing values detected.")

def check_data_types(df):
    """
    Validate data types of each column.
    """
    print("Column data types:")
    print(df.dtypes)
    print("\nChecking for invalid types:")
    
    # Example checks
    if not pd.api.types.is_numeric_dtype(df['Height']):
        print("Error: 'Height' column should be numeric.")
    if not pd.api.types.is_string_dtype(df['City']):
        print("Error: 'City' column should be of string type.")

def check_unique_values(df):
    """
    Check for duplicate entries in the dataset.
    """
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Warning: {duplicates} duplicate rows found.")
    else:
        print("No duplicate rows detected.")

def check_range_values(df):
    """
    Validate numeric ranges for specific columns.
    """
    if (df['Height'] <= 0).any():
        print("Error: 'Height' column contains non-positive values.")
    if (df['Floors'] <= 0).any():
        print("Error: 'Floors' column contains non-positive values.")
    if not df['Year Completed'].between(1800, 2025).all():
        print("Error: 'Year Completed' contains values outside the valid range (1800-2025).")

def run_validations(file_path='tallest_buildings_cleaned.csv'):
    """
    Run all validation checks.
    """
    df = load_data(file_path)
    if df is None:
        return
    
    print("\n--- Data Validation Report ---")
    check_missing_values(df)
    check_data_types(df)
    check_unique_values(df)
    check_range_values(df)
    print("\nValidation completed.")

if __name__ == "__main__":
    run_validations()
