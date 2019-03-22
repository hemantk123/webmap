import folium
maplad=folium.Map(location=[18.9317, 66.9912],zoom_start=10,tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[18.939417, 66.995612],popup="pani hae dekh kya rha hae",icon=folium.Icon(color="green")))
maplad.add_child(fg)

maplad.save("ladpur.html")
