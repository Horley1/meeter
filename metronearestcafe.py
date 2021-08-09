import overpy
import math 
api = overpy.Overpass()
mindist = 100000000000000

print("Введите станцию метро: ")
metrostation=input()

askcoords=f"""
node["railway"="station"]["station"="subway"][name="{metrostation}"];
out;"""

ask=f"""node["railway"="station"]["station"="subway"][name="{metrostation}"];
node(around:1500)["cuisine"="coffee_shop"];
out;"""

mcoords=api.query(askcoords)
r=api.query(ask)



for cafe in r.nodes:
	dlon = cafe.lon - mcoords.nodes[0].lon
	dlat = cafe.lat - mcoords.nodes[0].lat
	a = (math.sin(dlat/2))**2 + math.cos(mcoords.nodes[0].lat) * math.cos(cafe.lat) * (math.sin(dlon/2))**2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = 6371 * c * 1000
	if d<mindist:
		mindist=d
		minlat=cafe.lat
		minlon=cafe.lon
print("Вот ближайшая кофейня:")
print(minlat, minlon)







