import folium
import pandas

# initialize map
volcanoes_map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")

data = pandas.read_csv('volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = """<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br><br>
Height: %s m
"""


# return marker color
def color_producer(ele):
    if ele < 1000:
        return 'green'
    elif 1000 <= ele < 3000:
        return 'orange'
    else:
        return 'red'


# add markers using FeatureGroup
fg = folium.FeatureGroup(name='Volcanoes')
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fg.add_child(
        folium.CircleMarker(location=[lt, ln], radius=7, popup=folium.Popup(iframe), fill_color=color_producer(el),
                            color='grey', fill_opacity=0.8))

# add feature group
volcanoes_map.add_child(fg)

# add layer control
volcanoes_map.add_child(folium.LayerControl())

# generate map
volcanoes_map.save('volcanoes_map.html')
