import folium
import pandas

# initialize map
volcanoes_map = folium.Map(location=[34.3946, 147.2062], zoom_start=3, tiles="Stamen Terrain")

# generate map
volcanoes_map.save('country_by_population.html')
