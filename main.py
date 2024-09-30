from flask import Flask, render_template
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükler
API_KEY = os.getenv("API_KEY")
city_name = "Istanbul" # input("Şehir ismi nedir? ")

today = datetime.now()
day = today.strftime("%A")

LAT_LONG_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"

for_lat_long = requests.get(LAT_LONG_URL)

data = for_lat_long.json()
lat = data[0]["lat"]
lon = data[0]["lon"]

WEATHER_URL = F"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"


r = requests.get(WEATHER_URL)

data_weather = r.json()

hava_durumu = data_weather["weather"][0]["main"]

temp = data_weather["main"]["temp"] - 273.15
temp = f"{temp:.2f}"

humi = data_weather["main"]["humidity"]
press = data_weather["main"]["pressure"]

print(day, temp, humi, press)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", temp=temp)

if __name__ == "__main__":
    app.run(debug=True)