import folium
import pandas

# initialize map
country_by_population_map = folium.Map(location=[41.4432, 2.0803], zoom_start=3, tiles="Stamen Terrain")

# FeatureGroup 'My Map'
fg = folium.FeatureGroup(name='Population by Colour')

# read Geojson file then add child
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='UTF-8-sig').read(), style_function=lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 10_000_000 else 'orange' if 10_000_000 <= x['properties'][
        'POP2005'] < 20_000_000 else 'red'}))

# add feature group
country_by_population_map.add_child(fg)

# add layer control
country_by_population_map.add_child(folium.LayerControl())

# generate map
country_by_population_map.save('country_by_population.html')
