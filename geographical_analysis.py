import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Load the cleaned dataset
def load_data(file_path='tallest_buildings_cleaned.csv'):
    return pd.read_csv(file_path)

# Prepare GeoDataFrame
def prepare_geodata(df):
    # Assuming the dataset contains 'Latitude' and 'Longitude' columns
    df = df.dropna(subset=['Latitude', 'Longitude'])
    geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
    geo_df = gpd.GeoDataFrame(df, geometry=geometry)
    return geo_df

# Plot distribution of buildings globally
def plot_global_distribution(geo_df, output_file='global_distribution.png'):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot(color='lightgrey', edgecolor='black', figsize=(15, 10))
    geo_df.plot(ax=ax, color='blue', markersize=10, alpha=0.7, label='Buildings')
    plt.title('Global Distribution of Tallest Buildings')
    plt.legend()
    plt.savefig(output_file)
    plt.show()

# Plot number of buildings per country
def plot_buildings_by_country(df, output_file='buildings_by_country.png'):
    country_counts = df['Country'].value_counts()
    fig, ax = plt.subplots(figsize=(12, 8))
    country_counts.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Number of Tallest Buildings by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel('Number of Buildings')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

# Analyze tallest building heights by region
def region_height_analysis(df, region_mapping, output_file='region_heights.png'):
    df['Region'] = df['Country'].map(region_mapping)
    region_avg_height = df.groupby('Region')['Height'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(12, 8))
    region_avg_height.plot(kind='barh', color='salmon', ax=ax)
    ax.set_title('Average Height of Tallest Buildings by Region')
    ax.set_xlabel('Average Height (m)')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    # Load and prepare data
    data = load_data()
    geo_data = prepare_geodata(data)
    
    # Plot geographical distribution
    plot_global_distribution(geo_data)
    
    # Plot buildings by country
    plot_buildings_by_country(data)
    
    # Define region mapping (example for demonstration purposes)
    region_map = {
        'United States': 'North America',
        'China': 'Asia',
        'United Arab Emirates': 'Middle East',
        'Saudi Arabia': 'Middle East',
        'Malaysia': 'Asia',
        'Canada': 'North America',
        'Australia': 'Oceania',
        # Add other countries and their regions as needed
    }
    
    # Analyze heights by region
    region_height_analysis(data, region_map)
