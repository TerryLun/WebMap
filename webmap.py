import folium
import pandas

# initialize map
volcanoes_map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Stamen Terrain")

data = pandas.read_csv('volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])


# add markers using FeatureGroup
fg = folium.FeatureGroup(name='My Map')
for lt, ln, el, nm in zip(lat, lon, elev, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm+'\n'+str(el)+' m', icon=folium.Icon(color='red')))
volcanoes_map.add_child(fg)

# generate map
volcanoes_map.save('volcanoes_map.html')
