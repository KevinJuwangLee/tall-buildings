import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import clean_data
from data_validation import load_data, check_missing_values, check_range_values

# Load and clean the data
def load_and_clean_data(file_path='tallest_buildings.csv'):
    """
    Load and clean the dataset. This function calls the clean_data module for processing.
    """
    # Load data
    data = load_data(file_path)
    if data is None:
        return None

    # Data Cleaning
    cleaned_data = clean_data(data)
    return cleaned_data

# Feature engineering
def feature_engineering(df):
    """
    Create new features or process existing features for model training.
    """
    # Encoding categorical data: 'City', 'Country', 'Building'
    label_encoder = LabelEncoder()
    df['City_encoded'] = label_encoder.fit_transform(df['City'])
    df['Country_encoded'] = label_encoder.fit_transform(df['Country'])
    
    # Converting 'Year Completed' to a more useful feature by calculating building age
    df['Building_age'] = 2025 - df['Year Completed']  # Assuming current year is 2025

    return df

# Prepare data for training and testing
def prepare_data(df):
    """
    Prepare the dataset by splitting into features (X) and target (y) and then into train-test sets.
    """
    # Select features (X) and target (y)
    X = df[['City_encoded', 'Country_encoded', 'Building_age', 'Floors']]
    y = df['Height']

    # Split into train and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature Scaling (Standardization)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test

# Train a Linear Regression Model
def train_linear_regression(X_train, y_train):
    """
    Train a Linear Regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Train a Random Forest Regressor Model
def train_random_forest(X_train, y_train):
    """
    Train a Random Forest Regressor model.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model performance
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of the model using MAE, MSE, RMSE, and R².
    """
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R² Score: {r2}")

    # Plotting actual vs predicted values
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.title("Actual vs Predicted Building Heights")
    plt.xlabel("Actual Height")
    plt.ylabel("Predicted Height")
    plt.show()

# Visualizing feature importance for Random Forest Model
def plot_feature_importance(model, X):
    """
    Plot feature importance using Random Forest.
    """
    feature_importances = model.feature_importances_
    features = X.columns

    plt.figure(figsize=(10, 6))
    sns.barplot(x=features, y=feature_importances)
    plt.title("Feature Importance")
    plt.xlabel("Features")
    plt.ylabel("Importance")
    plt.xticks(rotation=45)
    plt.show()

# Main function to orchestrate the predictive modeling
def run_predictive_model(file_path='tallest_buildings_cleaned.csv'):
    """
    Run the entire predictive modeling process: data loading, cleaning, feature engineering,
    model training, evaluation, and visualization.
    """
    # Load and clean the data
    df = load_and_clean_data(file_path)
    if df is None:
        print("Data could not be loaded. Exiting.")
        return

    # Check for missing values or range issues after cleaning
    check_missing_values(df)
    check_range_values(df)

    # Feature engineering
    df = feature_engineering(df)

    # Prepare data for training
    X_train, X_test, y_train, y_test = prepare_data(df)

    # Train models
    print("\nTraining Linear Regression Model...")
    lr_model = train_linear_regression(X_train, y_train)
    print("\nEvaluating Linear Regression Model...")
    evaluate_model(lr_model, X_test, y_test)

    print("\nTraining Random Forest Regressor Model...")
    rf_model = train_random_forest(X_train, y_train)
    print("\nEvaluating Random Forest Regressor Model...")
    evaluate_model(rf_model, X_test, y_test)

    # Plot feature importance (Random Forest only)
    print("\nPlotting Feature Importance for Random Forest Model...")
    plot_feature_importance(rf_model, pd.DataFrame(X_train))

if __name__ == "__main__":
    run_predictive_model()
