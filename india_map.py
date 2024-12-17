import folium
from IPython.display import display
from folium.plugins import HeatMap, MiniMap
import requests

# Centering the map over India
map_center = [22.9734, 78.6569]
mymap = folium.Map(location=map_center, zoom_start=5)

# Adding markers for major cities in India
cities = {
    "New Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Bangalore": [12.9716, 77.5946],
    "Kolkata": [22.5726, 88.3639],
    "Chennai": [13.0827, 80.2707],
    "Hyderabad": [17.366, 78.476]
}

# Add markers with custom icons
for city, coordinates in cities.items():
    folium.Marker(
        coordinates,
        popup=city,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mymap)

# Adding a polygon to outline a region (Delhi region example)
folium.Polygon(
    locations=[[28.7041, 77.1025], [28.85, 77.12], [28.72, 77.30], [28.57, 77.08]], 
    color="red", 
    fill=True, 
    fill_color="red"
).add_to(mymap)

# Adding heatmap layer (example data points)
heat_data = [
    [28.6139, 77.2090],  # New Delhi
    [19.0760, 72.8777],  # Mumbai
    [12.9716, 77.5946],  # Bangalore
    [22.5726, 88.3639],  # Kolkata
    [13.0827, 80.2707],   # Chennai
    [17.366, 78.476]      # Hyderbad
]

HeatMap(heat_data).add_to(mymap)

# Adding a minimap to the main map
minimap = MiniMap()
mymap.add_child(minimap)

# Load GeoJSON data (for India states; replace URL with actual data source)
geojson_url = 'https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson'  # Example URL
geojson_data = requests.get(geojson_url).json()

# Adding the GeoJSON layer
folium.GeoJson(geojson_data, name="geojson").add_to(mymap)

# Displaying the map
display(mymap)

*/#################################################
import folium
from IPython.display import display
from folium.plugins import HeatMap, MiniMap
import requests

# Centering the map over India
map_center = [22.9734, 78.6569]
mymap = folium.Map(location=map_center, zoom_start=5)

# Adding city markers and labels
cities = {
    "Somnath": [20.8880, 70.4014],
    "Mahakaleshwar": [23.1828, 75.7684],
    "Omkareshwar": [22.2454, 76.1511],
    "Kedarnath": [30.734627, 79.066895],
    "Bhimashankar": [19.0720, 73.5359],
    "Viswanath": [25.3109, 83.0107],
    "Trimbakeshwar": [19.9322, 73.5308],
    "Vaidyanath": [20.8341, 83.7956],
    "Mallikarjuna": [16.0740, 78.8680],
    "Rameshwaram": [9.2876, 79.3129],
    "Nageshwar": [22.3360, 69.0870],
    "Grishneshwar": [20.0249, 75.1699]
}

# Add markers and labels for each city
for city, coordinates in cities.items():
    # Marker
    folium.Marker(
        location=coordinates,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(mymap)
    
    # Label as DivIcon
    folium.map.Marker(
        coordinates,
        icon=folium.DivIcon(
            icon_size=(150, 36),
            icon_anchor=(0, 0),
            html=f'<div style="font-size: 12pt; color: black; font-weight: bold;">{city}</div>'
        )
    ).add_to(mymap)

# Adding a polygon to outline a region
folium.Polygon(
    locations=[
        [20.8880, 70.4014], [23.1828, 75.7684], [22.2454, 76.1511],
        [30.734627, 79.066895], [19.0720, 73.5359], [25.3109, 83.0107],
        [19.9322, 73.5308], [20.8341, 83.7956], [16.0740, 78.8680],
        [9.2876, 79.3129], [22.3360, 69.0870], [20.0249, 75.1699]
    ],
    color="red",
    fill=True,
    fill_color="red"
).add_to(mymap)

# Adding heatmap layer
heat_data = list(cities.values())
HeatMap(heat_data).add_to(mymap)

# Adding a minimap
minimap = MiniMap()
mymap.add_child(minimap)

# Load GeoJSON data for India states
geojson_url = 'https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson'
geojson_data = requests.get(geojson_url).json()
folium.GeoJson(geojson_data, name="geojson").add_to(mymap)

# Adding layer control
folium.LayerControl().add_to(mymap)

# Display the map
display(mymap)
############################*/
