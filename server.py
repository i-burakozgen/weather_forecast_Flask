from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

def convert_to_fahrenheit(temp_celsius):
        return (temp_celsius * 9/5) + 32

def convert_to_kelvin(temp_celsius):
        return temp_celsius + 273.15

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather_obj():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
        
    weather_data = get_current_weather(city)
    if weather_data.get('cod') == '404':
            raise ValueError("City not found")

    data_obj = {
            "title_city": weather_data["name"],
            "weather_description": weather_data["weather"][0]["description"],
            "temp": weather_data["main"]["temp"],
            "temp_feels":weather_data['main']['feels_like'],
            "temp_min":weather_data['main']['temp_min'],
            "temp_max":weather_data['main']['temp_max'],    
        }
    temp_celsius_main = data_obj["temp"]
    temp_celsius_feels = data_obj["temp_feels"]
    temp_celsius_min = data_obj["temp_min"]
    temp_celsius_max = data_obj["temp_max"]
    if units == "imperial":
        temp_unit = '°F'
        temp_celsius_main = convert_to_fahrenheit(temp_celsius_main)
        temp_celsius_feels = convert_to_fahrenheit(temp_celsius_feels)
        temp_celsius_min = convert_to_fahrenheit(temp_celsius_min)
        temp_celsius_max = convert_to_fahrenheit(temp_celsius_max)
    elif units == "standard":
        temp_unit = '°K'
        temp_celsius_main =  convert_to_kelvin(temp_celsius_main)
        temp_celsius_feels = convert_to_kelvin(temp_celsius_feels)
        temp_celsius_min =  convert_to_kelvin(temp_celsius_min)
        temp_celsius_max =  convert_to_kelvin(temp_celsius_max)
    else:
        temp_unit = '°C'
        
    temp_obj = {
        "temp_main":temp_celsius_main,
        "temp_feels":temp_celsius_feels,
        "temp_main_min":temp_celsius_min,
        "temp_main_max":temp_celsius_max,
        "temp_units":temp_unit,
        
    }
    
    
    
    

    return render_template('weather.html', data_obj=data_obj, temp_obj = temp_obj)
    
    
if __name__ == "__main__":
    serve(app, host ="0.0.0.0", port=9000)