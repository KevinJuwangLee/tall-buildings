import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_summary_statistics(data):
    """
    Calculates summary statistics for numerical columns in the dataset.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    
    Returns:
    - DataFrame: Summary statistics including mean, median, standard deviation, and range.
    """
    summary = data.describe().transpose()
    summary['range'] = summary['max'] - summary['min']
    summary = summary[['mean', '50%', 'std', 'range']].rename(columns={'50%': 'median'})
    print("Summary statistics calculated.")
    return summary

def plot_column_distribution(data, column):
    """
    Plots the distribution of a specified column.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    - column (str): The column to plot.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True, color='blue', bins=30)
    plt.title(f'Distribution of {column}', fontsize=16)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def calculate_correlation_matrix(data):
    """
    Calculates the correlation matrix for numerical columns.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    
    Returns:
    - DataFrame: The correlation matrix.
    """
    correlation_matrix = data.corr()
    print("Correlation matrix calculated.")
    return correlation_matrix

def plot_correlation_heatmap(data):
    """
    Plots a heatmap of the correlation matrix.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    """
    correlation_matrix = data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title('Correlation Heatmap', fontsize=16)
    plt.show()

def analyze_trends(data, x_column, y_column):
    """
    Analyzes trends between two variables using a scatter plot with a trend line.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    - x_column (str): The column to use as the x-axis.
    - y_column (str): The column to use as the y-axis.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column, color='purple')
    sns.regplot(data=data, x=x_column, y=y_column, scatter=False, color='red')
    plt.title(f'Trend Analysis: {x_column} vs {y_column}', fontsize=16)
    plt.xlabel(x_column, fontsize=14)
    plt.ylabel(y_column, fontsize=14)
    plt.grid(alpha=0.5)
    plt.show()

def top_n_entries(data, column, n=5, ascending=False):
    """
    Returns the top N rows based on a specific column.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    - column (str): The column to sort by.
    - n (int): The number of top rows to return.
    - ascending (bool): Whether to sort in ascending order.
    
    Returns:
    - DataFrame: The top N rows.
    """
    top_entries = data.sort_values(by=column, ascending=ascending).head(n)
    print(f"Top {n} entries based on '{column}':")
    return top_entries

def category_analysis(data, category_column, numerical_column):
    """
    Analyzes a numerical variable grouped by a categorical variable.
    
    Parameters:
    - data (DataFrame): The DataFrame to analyze.
    - category_column (str): The categorical column.
    - numerical_column (str): The numerical column to analyze.
    """
    group_data = data.groupby(category_column)[numerical_column].mean().sort_values()
    plt.figure(figsize=(10, 6))
    group_data.plot(kind='bar', color='teal')
    plt.title(f'{numerical_column} by {category_column}', fontsize=16)
    plt.xlabel(category_column, fontsize=14)
    plt.ylabel(f'Average {numerical_column}', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def export_analysis_results(data, output_path):
    """
    Exports key analysis results to a CSV file.
    
    Parameters:
    - data (DataFrame): The DataFrame containing analysis results.
    - output_path (str): The file path to save the results.
    """
    data.to_csv(output_path, index=False)
    print(f"Analysis results saved to {output_path}.")
