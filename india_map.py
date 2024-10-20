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
