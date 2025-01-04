import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_height_trend(data, country_name):
    """
    Plots the height trend of buildings in a given country over time.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    - country_name (str): The name of the country to filter data by.
    """
    country_data = data[data['Country'] == country_name]
    if country_data.empty:
        print(f"No data found for country: {country_name}")
        return
    
    sorted_data = country_data.sort_values(by='Year Completed')
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_data['Year Completed'], sorted_data['Height (m)'], marker='o', label=country_name)
    plt.title(f'Height Trend of Tallest Buildings in {country_name}')
    plt.xlabel('Year Completed')
    plt.ylabel('Height (m)')
    plt.grid()
    plt.legend()
    plt.show()

def compare_country_trends(data, countries):
    """
    Plots the height trends of buildings for multiple countries over time.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    - countries (list of str): List of country names to compare.
    """
    plt.figure(figsize=(12, 8))
    for country in countries:
        country_data = data[data['Country'] == country]
        if not country_data.empty:
            sorted_data = country_data.sort_values(by='Year Completed')
            plt.plot(sorted_data['Year Completed'], sorted_data['Height (m)'], marker='o', label=country)
    
    plt.title('Height Trends of Tallest Buildings by Country')
    plt.xlabel('Year Completed')
    plt.ylabel('Height (m)')
    plt.grid()
    plt.legend()
    plt.show()

def country_building_distribution(data):
    """
    Visualizes the distribution of tallest buildings by country.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    """
    plt.figure(figsize=(10, 8))
    sns.countplot(y='Country', data=data, order=data['Country'].value_counts().index)
    plt.title('Distribution of Tallest Buildings by Country')
    plt.xlabel('Count of Buildings')
    plt.ylabel('Country')
    plt.show()

def tallest_buildings_bar_chart(data, top_n=10):
    """
    Creates a bar chart for the top N tallest buildings.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    - top_n (int): Number of top tallest buildings to display.
    """
    top_buildings = data.nlargest(top_n, 'Height (m)')
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Height (m)', y='Building', data=top_buildings)
    plt.title(f'Top {top_n} Tallest Buildings')
    plt.xlabel('Height (m)')
    plt.ylabel('Building')
    plt.show()

def height_histogram(data, bins=15):
    """
    Plots a histogram of building heights.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    - bins (int): Number of bins for the histogram.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data['Height (m)'], bins=bins, color='blue', edgecolor='black')
    plt.title('Distribution of Building Heights')
    plt.xlabel('Height (m)')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def correlation_heatmap(data):
    """
    Displays a heatmap of correlations between numerical attributes in the dataset.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    """
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

def yearly_construction_trend(data):
    """
    Plots the number of buildings constructed per year.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    """
    yearly_count = data['Year Completed'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_count.index, yearly_count.values, marker='o', color='green')
    plt.title('Yearly Construction Trend of Tallest Buildings')
    plt.xlabel('Year')
    plt.ylabel('Number of Buildings')
    plt.grid()
    plt.show()

def floors_vs_height_scatter(data):
    """
    Creates a scatter plot to show the relationship between the number of floors and building height.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Floors', y='Height (m)', data=data, hue='Country')
    plt.title('Number of Floors vs Height of Buildings')
    plt.xlabel('Floors')
    plt.ylabel('Height (m)')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def tallest_in_each_country(data):
    """
    Creates a bar chart showing the tallest building in each country.
    
    Parameters:
    - data (DataFrame): The DataFrame containing building data.
    """
    tallest_per_country = data.loc[data.groupby('Country')['Height (m)'].idxmax()]
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Height (m)', y='Country', data=tallest_per_country)
    plt.title('Tallest Building in Each Country')
    plt.xlabel('Height (m)')
    plt.ylabel('Country')
    plt.show()
