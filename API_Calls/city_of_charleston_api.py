import requests

zoning_geojson_url = "https://opendata.arcgis.com/datasets/c4d4ce44d9394c578a2999637a54b77f_0.geojson"

zoning_data = requests.get(zoning_geojson_url)

zoning_data