from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

# def convert_to_fahrenheit(temp):
#     return (temp * 9/5) + 32

# def convert_to_kelvin(temp):
#     return temp + 273.15

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather_obj():
    city = request.args.get('city')
    #units = request.args.get('units', 'metric')
    
    weather_data = get_current_weather(city)

    data_obj = {
            "title_city": weather_data["name"],
            "weather_description": weather_data["weather"][0]["description"],
            "temp": weather_data["main"]["temp"],
            "temp_feels": weather_data["main"]["feels_like"],
            "temp_min": weather_data["main"]["temp_min"],
            "temp_max": weather_data["main"]["temp_max"],      
        }
    

    return render_template('weather.html', data_obj=data_obj)
    
    
if __name__ == "__main__":
    serve(app, host ="0.0.0.0", port=9000)