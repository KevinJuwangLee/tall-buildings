# IBM Data Science Professional Certificate - Tallest Buildings Analysis

This repository contains a comprehensive data analysis project focused on the tallest buildings dataset, built as part of the **IBM Data Science Professional Certificate**. The goal of this project is to explore, clean, analyze, visualize, and build predictive models using real-world data of the tallest buildings worldwide. The project spans multiple stages of data science workflow, from data collection and cleaning to validation, analysis, geographical study, visualization, and predictive modeling.

## Project Overview

This project involves working with a dataset containing details about the tallest buildings in the world, including information like building names, cities, countries, height, number of floors, and the year completed. By leveraging various data science techniques and tools, the project aims to:
- Load and clean the dataset.
- Validate data for inconsistencies or missing values.
- Analyze the dataset to extract meaningful insights.
- Perform geographical analysis of building distributions.
- Create visualizations to display trends and correlations.
- Build and run predictive models to forecast building heights based on certain features.

## Project Files

### **1. `main.py`**
This file orchestrates the entire data science pipeline. It loads the dataset, cleans it, validates it, performs analysis, generates visualizations, and runs predictive models. The script runs in a sequential flow, integrating the functionality of all the other modules in the project.

Key Responsibilities:
- **Data Loading and Cleaning**: Uses functions from `data_cleaning.py` and `data_validation.py` to load and clean the data.
- **Data Validation**: Performs checks for missing values and out-of-range values using the functions from `data_validation.py`.
- **Data Analysis**: Analyzes the dataset to identify trends and generate statistical insights using `data_analysis.py`.
- **Geographical Analysis**: Leverages the `geographical_analysis.py` to plot geographical data, showing how buildings are distributed around the world.
- **Visualization**: Creates various visualizations using `visualization.py` to display patterns and correlations.
- **Predictive Modeling**: Integrates predictive models built in `predictive_model.py` to predict future building heights based on other variables.
  
### **2. `index.py`**
This file provides more in-depth analysis and organization of the project, including additional preprocessing steps and data transformations. It complements `main.py` by focusing on data extraction, preprocessing, and performing detailed statistical analysis.

Key Responsibilities:
- **Preprocessing**: Enhances data preparation for analysis.
- **Advanced Analysis**: Provides further exploration of the dataset, including more complex analysis like identifying key trends and outliers.

### **3. `data_analysis.py`**
This file contains functions that perform detailed analysis on the dataset. It includes:
- **Descriptive Statistics**: Calculating means, medians, standard deviations, and other summary statistics for various features.
- **Exploratory Data Analysis (EDA)**: Conducting EDA to find patterns, correlations, and potential relationships between features like height, city, and country.

Key Responsibilities:
- **Statistical Analysis**: Analyzing the distribution of various attributes (height, country, floors, etc.).
- **Identifying Trends**: Identifying trends in building heights and distributions over time.

### **4. `data_cleaning.py`**
This module is responsible for cleaning the dataset. It ensures the data is ready for analysis by removing duplicates, handling missing values, and formatting it correctly. Cleaning functions include:
- **Handling Missing Values**: Filling or removing missing values.
- **Data Type Conversion**: Converting columns into appropriate data types (e.g., converting height from string to numeric).
- **Outlier Removal**: Identifying and removing outliers that could skew analysis.

Key Responsibilities:
- **Data Preprocessing**: Ensures the dataset is clean and ready for further steps.
- **Handling Anomalies**: Deals with problematic values that could interfere with accurate analysis.

### **5. `data_validation.py`**
This file contains functions for validating the dataset. It checks for:
- **Missing Values**: Identifies columns with missing values and provides options to handle them.
- **Value Range Checks**: Ensures numerical columns like height and year completed are within plausible ranges.
  
Key Responsibilities:
- **Data Validation**: Ensures that the data is consistent, accurate, and usable before moving on to analysis.

### **6. `geographical_analysis.py`**
This module performs geographical analysis on the dataset. It focuses on mapping and plotting the distribution of the tallest buildings worldwide. Using tools like `matplotlib` and `geopandas`, this file generates visual insights about where the tallest buildings are concentrated across cities and countries.

Key Responsibilities:
- **Mapping**: Plots the geographical distribution of buildings on a world map.
- **Geographical Insights**: Extracts insights into how location influences building heights.

### **7. `predictive_model.py`**
This file contains the core predictive modeling functionality. It takes the cleaned dataset and applies machine learning models to predict building heights based on other features like number of floors, country, and year completed. 
- **Modeling**: Uses regression algorithms like Linear Regression, Random Forest, or other machine learning models to predict building heights.
- **Model Evaluation**: Evaluates model performance using metrics like RMSE (Root Mean Squared Error) and R^2.

Key Responsibilities:
- **Predictive Modeling**: Trains and tests machine learning models to predict building heights.
- **Model Tuning**: Fine-tunes models for optimal performance.

### **8. `visualization.py`**
This module contains various functions for generating visualizations of the dataset. Using libraries like `matplotlib`, `seaborn`, and `plotly`, it creates:
- **Bar Charts**: For comparing the number of buildings by country or city.
- **Line Graphs**: To track building heights over time.
- **Scatter Plots**: To show relationships between various building attributes (e.g., height vs. year completed).

Key Responsibilities:
- **Visualization Creation**: Generates plots and charts that help in visualizing the trends in the data.

### **9. `scrape.js`**
This JavaScript file was designed to scrape data from an external source (in this case, GDP data). It's used to extract economic information that could potentially be used in the analysis to correlate GDP with building heights.

Key Responsibilities:
- **Data Scraping**: Extracts relevant data from web pages to supplement the analysis, such as GDP information of different countries.

### **10. `Jupyter Notebook`**
The Jupyter Notebook serves as an interactive environment where all the data exploration, cleaning, validation, and visualizations are first tested before being coded into the respective Python files. It is a step-by-step guide to understand the data and perform preliminary analysis.

Key Responsibilities:
- **Exploratory Data Analysis (EDA)**: Interactively exploring the dataset and testing data cleaning and validation procedures.
- **Visualization**: Creating quick visualizations of the data to gain insights.

---

## How It All Works Together

- **Data Loading & Cleaning**: The `main.py` file orchestrates the loading and cleaning of the data using the functions from `data_cleaning.py` and `data_validation.py`. The data is first cleaned and then validated for missing or erroneous values.
  
- **Exploratory Data Analysis & Statistical Analysis**: The `data_analysis.py` file conducts a thorough analysis to extract trends, summary statistics, and key insights from the data. 

- **Geographical Analysis**: Using `geographical_analysis.py`, the project visualizes the geographical spread of the tallest buildings, allowing us to see patterns in where the tallest buildings are located.

- **Visualization**: The `visualization.py` module is used throughout the project to create various charts and graphs, which help visualize the trends and patterns in the dataset.

- **Predictive Modeling**: In the `predictive_model.py` file, machine learning models are built to predict building heights based on historical data and other features. This is one of the more advanced parts of the project, as it incorporates supervised learning techniques.

---

## Key Learnings from the Project

### Data Cleaning
- **Handling Missing Data**: I learned how to detect and address missing data, which is a common issue in real-world datasets. I used techniques like imputation and deletion of rows with critical missing values.
  
- **Outlier Detection**: Removing outliers is essential to ensure that they do not skew statistical results or model predictions. I learned how to identify and handle these outliers effectively.

### Data Validation
- **Data Consistency**: I gained a deep understanding of ensuring the consistency of data, especially in terms of validating numerical ranges and ensuring there are no incorrect values in the dataset.
  
- **Checking for Errors**: I learned how to systematically check for errors in the data, such as values that don’t make sense (e.g., building heights that are too low or too high).

### Data Analysis
- **Exploratory Data Analysis (EDA)**: This project allowed me to perform EDA using summary statistics and visualizations to uncover hidden insights and trends in the data.

### Geographical Analysis
- **Geospatial Data Visualization**: I had the opportunity to work with geographical data and create maps to visualize the locations of the tallest buildings, which helped me understand the geographical distribution patterns of such structures.

### Predictive Modeling
- **Machine Learning Techniques**: This was one of the most exciting parts of the project, where I applied regression models to predict building heights based on other variables. I learned about model evaluation, feature selection, and performance tuning.

### Visualization
- **Effective Communication**: I learned how to use various types of charts to communicate findings effectively. Visualization tools like `matplotlib` and `seaborn` helped me transform raw data into clear and compelling visual insights.

### Reflection
- This project has been instrumental in honing my data science skills. I’ve gained practical experience in the full lifecycle of a data science project, from data wrangling to model building, and I’ve learned how to present data insights in meaningful ways. The project has helped me build a robust foundation for future data science work and apply machine learning to solve real-world problems.

---

## Future Improvements

- **Model Improvement**: I can further improve the predictive models by experimenting with more complex algorithms and refining feature selection.
- **Real-Time Data Scraping**: I could set up a real-time scraping mechanism to automatically pull the latest data about the tallest buildings, making the project more dynamic.
- **Integration with Other Datasets**: The project could be expanded by integrating other datasets, such as construction costs or material usage, to gain more insights.

---

This project represents my journey through the **IBM Data Science Professional Certificate**, and showcases developing strong data science in tackling real-world problems.

