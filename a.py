import folium
# tiles = "Stamen Terrain"

map1 = folium.Map(location=[49.189848, -123.126379], zoom_start=11, tiles="Stamen Terrain")


map1.save('map1.html')
