import geocoder
import reverse_geocoder as rg
import json

g = geocoder.ip('me')
print(g.latlng[0])
print(g.latlng[1])

print(results)
