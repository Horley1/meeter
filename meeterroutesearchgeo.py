import overpy
api = overpy.Overpass()
r = api.query("""
node["railway"="station"]["station"="subway"]
 (55.078,36.573,56.225,39.095);
out;""")
for station in r.nodes:
	print(station.lat, station.lon, end="\n")
