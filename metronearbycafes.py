import overpy
api = overpy.Overpass()
print("Введите станцию метро: ")
metrostation=input()
ask=f"""node["railway"="station"]["station"="subway"][name="{metrostation}"];
node(around:1500)["cuisine"="coffee_shop"];
out;"""
r = api.query(ask)
print("Вот ближайшие кафе:", end="\n")
for cafe in r.nodes:
	print(cafe.lat, cafe.lon, end="\n")
