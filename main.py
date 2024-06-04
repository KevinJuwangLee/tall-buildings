from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_tallest_buildings'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
table = soup.find('table', {'class': 'wikitable sortable'})

#print(table)

headers = [_.text.strip() for _ in table.find_all('th')[1:]]
#print(headers)

building = []
city = []
country = []
height = []
floors = []
built = []


for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    building.append(cells[1].text.strip())
    city.append(cells[2].text.strip())
    country.append(cells[3].text.strip())
    height.append(cells[4].text.strip())
    floors.append(cells[6].text.strip())
    built.append(cells[7].text.strip())


buildings_df = pd.DataFrame({
    'Building': building,
    'City': city,
    'Country': country,
    'Height': height,
    'Floors': floors,
    'Year Completed': built
})

# Export the DataFrame to a CSV file
buildings_df.to_csv('tallest_buildings.csv', index=False)

# Basic Data Analysis
#print(buildings_df.head())
#print(buildings_df.describe())

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Distribution of buildings by country
#plt.figure(figsize=(10, 6))
#sns.countplot(y='Country', data=buildings_df, order=buildings_df['Country'].value_counts().index)
#plt.title('Distribution of Tallest Buildings by Country')
#plt.show()

# Failed web scraping due to MacroTrends' restrictions
#def getGDP(country):
#    urlGDP = f'https://www.macrotrends.net/global-metrics/countries/{country}/united-states/gdp-gross-domestic-product'
#    pageGDP = requests.get(urlGDP)
#    soupGDP = BeautifulSoup(pageGDP.text, 'html.parser')
#    print(soupGDP)
#    chart = soupGDP.find_all(class_='amcharts-graph-g1')[1]
#    
#    circles = [_.a['aria-label'] for _ in chart.find_all('circle')[35:]]
#    print(circles[0])
#
#
#getGDP("USA")

def getBuildingsByCountry(country):
    array = [0 for _ in range(1995, 2023)]
    df = pd.read_csv('tallest_buildings.csv')
    for row in df.itertuples(index=False, name=None):
        if row[2].strip() == country:
            if 1995 > int(row[5]):
                array[0] += 1
            if 1995 <= int(row[5]) and int(row[5]) <= 2022:
                array[int(row[5]) - 1995] += 1
    for i in range(1, len(array)):
        array[i] = array[i] + array[i-1]
    return array

print(getBuildingsByCountry("United States"))