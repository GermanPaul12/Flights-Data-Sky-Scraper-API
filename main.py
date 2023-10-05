import requests
import creds

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlightEverywhere"



querystring = {"originSkyId":"FRA","travelDate":"2023-10-05","currency":"EUR"}

headers = {
	"X-RapidAPI-Key": creds.X_RapidAPI_Key,
	"X-RapidAPI-Host": creds.X_RapidAPI_Host
}

response = requests.get(url, headers=headers, params=querystring)

json_response = response.json()
data = json_response["data"]

for i in range(len(data)):
    country_data = data[i]
    
    TIMESTAMP = json_response["timestamp"]
    COUNTRY_ID = country_data["Meta"]["CountryId"]
    COUNTRY_NAME = country_data["Meta"]["CountryNameEnglish"]
    PRICE = country_data["Payload"]["Price"]
    CURRENCY = country_data["Payload"]["CurrencyId"]
    IMAGE_URL = country_data["Payload"]["ImageUrl"]
    
    with open("data.csv", "a+") as f:
        f.write(f"{COUNTRY_ID},{COUNTRY_NAME},{PRICE},{CURRENCY},{TIMESTAMP},{IMAGE_URL}\n")