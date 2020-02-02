import folium

# initialize map
richmond_map = folium.Map(location=[49.189848, -123.126379], zoom_start=13, tiles="Stamen Terrain")

# add markers using FeatureGroup
fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[49.189848, -123.126379], popup='Home', icon=folium.Icon(color='green')))
richmond_map.add_child(fg)

# generate map
richmond_map.save('richmond_map.html')
