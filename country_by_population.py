import folium
import pandas

# initialize map
volcanoes_map = folium.Map(location=[34.3946, 147.2062], zoom_start=3, tiles="Stamen Terrain")

# FeatureGroup 'My Map'
fg = folium.FeatureGroup(name='My Map')

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='UTF-8-sig').read())))

# add feature group
volcanoes_map.add_child(fg)

# generate map
volcanoes_map.save('country_by_population.html')
