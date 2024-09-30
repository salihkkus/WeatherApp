from flask import Flask, render_template, request
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

def get_city_weather(city):
    load_dotenv()  # .env dosyasını yükler
    API_KEY = os.getenv("API_KEY")
    # city_name = "Istanbul" 

    today = datetime.now()
    day = today.strftime("%A")

    LAT_LONG_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"

    for_lat_long = requests.get(LAT_LONG_URL)

    data = for_lat_long.json()
    lat = data[0]["lat"]
    lon = data[0]["lon"]

    WEATHER_URL = F"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"


    r = requests.get(WEATHER_URL)

    data_weather = r.json()

    weather = data_weather["weather"][0]["main"]

    temp = data_weather["main"]["temp"] - 273.15
    temp = f"{temp:.2f}"

    humi = data_weather["main"]["humidity"]
    press = data_weather["main"]["pressure"]

    state = data_weather["name"]
    
    city_data = [day, weather, temp, humi, press, state]
    return city_data

app = Flask(__name__)

@app.route("/")
def index():
    city = request.args.get('city')
    
    city_data = get_city_weather(city)
    day = city_data[0]
    weather = city_data[1]
    temp = city_data[2]
    humi = city_data[3]
    press = city_data[4]
    state = city_data[5]
    
    print(state)
    
    return render_template("index.html", humi=humi, press=press, temp=temp, city=city, state=state, weather=weather, day=day)

if __name__ == "__main__":
    app.run(debug=True)
    
'''@app.route(f"/?city={city_name}")
def search():
    '''