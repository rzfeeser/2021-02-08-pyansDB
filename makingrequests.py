import requests
import pandas

x = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY")

ciscojson = pandas.DataFrame(x.json())

print(ciscojson)
