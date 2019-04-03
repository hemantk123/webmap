import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def colour_changer(elev):
    if elev>3000:
        return "red"
    elif elev>2000:
        return "orange"
    else:
        return "green"

map1 = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fg1=folium.FeatureGroup(name="volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fg1.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color=colour_changer(el))))

fg2=folium.FeatureGroup(name="population")

fg2.add_child(folium.GeoJson(data=(open("115 world.json","r",encoding='utf-8-sig').read()),
style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005']<1000000 else 'orange' if x['properties']['POP2005']<2000000  else 'red' }))

map1.add_child(fg1)
map1.add_child(fg2)
map1.add_child(folium.LayerControl())

map1.save("map.html")