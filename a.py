import folium

# initialize map
map1 = folium.Map(location=[49.189848, -123.126379], zoom_start=13, tiles="Stamen Terrain")

# add marker
map1.add_child(folium.Marker(location=[49.189848, -123.126379], popup='Home', icon=folium.Icon(color='green')))

# generate map
map1.save('map1.html')
