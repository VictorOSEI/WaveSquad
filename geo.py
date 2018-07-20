import urllib
import json

def getLocation():
	url = "https://geoip-db.com/json"
	response = urllib.urlopen(url)
	raw = json.loads(response.read())
        lat, lon = raw.get("latitude"), raw.get("longitude")
        city = raw.get("city", "Unknown city")
        state = raw.get("state", "Unknown region")
        country = raw.get("country_name", "Unknown country")

        if lat and lon:
            pin = "\n@(" + str(lat) + ", " + str(lon) + ")"
        else:
            pin = ""
	return pin
        #return ", ".join([city, state, country]) + pin
