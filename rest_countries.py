# Below is an api endpoint to show you all countries that speak spanish. Dive into the data and answer the following
# questions:

# 1) Display the common name, currency symbol, population and timezone of each country that is NOT landlocked and is in
# the South American continent.
currency = []
timezone = []
# 2) using the latitude and longitude of the data from the query above, diplay the country information on a world map (using code below)


import requests
import json

url = 'https://restcountries.com/v3.1/lang/spanish'

# make the call to the API
r = requests.get(url)

#create an output file so you can see the json response that was returned by the API call
outfile = open('hw_output.json','w')
response_dict = r.json()
json.dump(response_dict,outfile,indent=4)

print(f"status code: {r.status_code}")


# Create a list of country names, longitudes, latitudes and population for all countries.
# NOTE: It is important to use these names for the map to work correctly.
names = []
lons = []
lats = []
population = []

# populate this list with the data from the api call using a loop and print out information
# per requirements in 1)
for country in response_dict:
    if country['continents'][0] == 'South America' and not country['landlocked']:
        names.append(country['name']['common'])
        lats.append(country['latlng'][0])
        lons.append(country['latlng'][1])
        population.append(country['population'])
        currency.append(list(country.get('currencies', {}).values())[0].get('symbol', ''))
        timezone.append(country['timezones'][0])

        print(f'Common Name: {country['name']['common']}')
        print(f"Currency Symbol: {list(country.get('currencies', {}).values())[0].get('symbol', '')}")
        print(f"Population: {country['population']:,}")
        print(f"Timezone: {country['timezones'][0]}")
        print()



#Plotly World Map (NOTE: NO CODING NEEDED HERE!)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text':names,
    'marker':{
        'size':[p/3_000_000 for p in population],
        'color':population,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Population'}
    },
}]

my_layout = Layout(title='South American Countries that are not landlocked')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='south_america.html')
