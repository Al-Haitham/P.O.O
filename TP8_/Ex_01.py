from collections import namedtuple

PointGPS=namedtuple("PointGPS", ["latitude", "longitude"])

marrakech=PointGPS(31.63, -8.00)
rabat=PointGPS(34.02, -6.84)

print(marrakech[0], marrakech[1])
print(rabat[0], rabat[1])

print(marrakech.latitude, marrakech.longitude)
print(rabat.latitude, rabat.longitude)

print(marrakech._asdict())
print(rabat._asdict())

marrakech=marrakech._replace(longitude=-7.95)
print(marrakech)

print(PointGPS._fields)