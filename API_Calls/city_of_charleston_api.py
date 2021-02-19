import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

zoning_geojson_url = "https://opendata.arcgis.com/datasets/c4d4ce44d9394c578a2999637a54b77f_0.geojson"

zoning_data = requests.get(zoning_geojson_url)

#jprint(zoning_data.json())

print(zoning_data.json().keys())
print(zoning_data.json()['features'][0])