from unittest import result
import phonenumbers
import folium

number= "" #enter phone number (+905555555555)

from phonenumbers import geocoder

key = "" # https://opencagedata.com api key for map

samNumber=phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber,"en")
print(yourLocation)


from phonenumbers import carrier
service_nmber = phonenumbers.parse(number)
print(carrier.name_for_number(service_nmber, "en"))

from opencage.geocoder import OpenCageGeocode 
geocoder = OpenCageGeocode(key)

query=str(yourLocation)

result=geocoder.geocode(query)
# print(result)

lat=result[0]["geometry"]["lat"]

lng=result[0]["geometry"]["lng"]

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)

folium.Marker([lat, lng],popup= yourLocation).add_to(myMap)

myMap.save("myLocation.htlm") 
