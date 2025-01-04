import pandas as pd
import numpy as np
import os
import time
from data_cleaning import clean_data
from data_validation import load_data, check_missing_values, check_range_values
from data_analysis import analyze_data
from geographical_analysis import plot_geographical_data
from visualization import create_visualizations
from predictive_model import run_predictive_model
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Load and Clean Data
def load_and_clean_data(file_path='tallest_buildings.csv'):
    """
    Load and clean the dataset.
    """
    logger.info("Loading data...")
    df = load_data(file_path)
    if df is None:
        logger.error("Failed to load data.")
        return None

    logger.info("Cleaning data...")
    cleaned_df = clean_data(df)
    if cleaned_df is None:
        logger.error("Data cleaning failed.")
        return None
    
    return cleaned_df

# Check data validation issues
def validate_data(df):
    """
    Check for missing values and other range issues.
    """
    logger.info("Validating data...")
    check_missing_values(df)
    check_range_values(df)

# Perform data analysis
def perform_data_analysis(df):
    """
    Perform various types of data analysis on the dataset.
    """
    logger.info("Performing data analysis...")
    analyze_data(df)

# Perform geographical analysis
def perform_geographical_analysis(df):
    """
    Plot geographical data based on the 'City' and 'Country' columns.
    """
    logger.info("Performing geographical analysis...")
    plot_geographical_data(df)

# Generate visualizations
def generate_visualizations(df):
    """
    Create various visualizations such as bar plots, scatter plots, etc.
    """
    logger.info("Generating visualizations...")
    create_visualizations(df)

# Main orchestration function
def main(file_path='tallest_buildings.csv'):
    """
    Main function that orchestrates the entire process.
    """
    start_time = time.time()

    # Step 1: Load and Clean Data
    logger.info("Starting data loading and cleaning...")
    df = load_and_clean_data(file_path)
    if df is None:
        logger.error("Exiting due to data loading/cleaning failure.")
        return
    
    # Step 2: Validate Data
    validate_data(df)

    # Step 3: Perform Data Analysis
    perform_data_analysis(df)

    # Step 4: Perform Geographical Analysis
    perform_geographical_analysis(df)

    # Step 5: Generate Visualizations
    generate_visualizations(df)

    # Step 6: Run Predictive Modeling
    logger.info("Running predictive model...")
    run_predictive_model(file_path)

    # Timing
    end_time = time.time()
    logger.info(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    file_path = 'tallest_buildings.csv'  # Path to your dataset
    main(file_path)
