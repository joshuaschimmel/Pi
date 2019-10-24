import pyowm
import time
import datetime



#TODOs
#1. script comment \w goal
#2. structure for return data
#x 3. observation of current weather
#x 4. update of observation
#5. structure for forecast data
#6. x day forecast (3h limit max 8)
#7. x update forecast


"""Weather Class whomst instances interact with the OpenWeatherMap-API"""
class Weather:
    """Needs a valid API key and city name"""
    def __init__(self, key, city):
        self.owm = pyowm.OWM(key)
        self.city = city
        #observation
        self.update_observation()
        #forecast
        self.update_forecast()

    def update(self):
        """calls both update functions"""
        self.update_observation()
        self.update_forecast()

    def update_observation(self):
        """Updates the observation with fresh data"""
        self.observation = self.pull_observation()

    def update_forecast(self):
        """Updates the forecast with fresh data"""
        self.forecast = self.pull_forecast()

    """
    returns an object with the temperature, an datetime object with the
    reference time and the status as detailed falvor-text
    """
    def get_observation(self):
        weather = self.observation.get_weather()
        observation = {
        "temp": weather.get_temperature("celsius")["temp"],
        "time": weather.get_reference_time("date"),
        "status": weather.get_detailed_status()
        }
        return observation

    """
    returns a forecast with the min/max temperature, the times and status
    for a 24h time-window
    """
    def get_forecast(self):
        self.forecast.actualize()
        weathers = self.forecast.get_weathers()[0:8]
        max_val = -100
        min_val = 100
        for weather in weathers:
            temperature = weather.get_temperature("celsius")["temp"]
            if(temperature > max_val):
                max_val = temperature
                max = weather
            elif(temperature < min_val):
                min_val = temperature
                min = weather
        max = { #maybe save this for later?
        "temp": max.get_temperature("celsius")["temp"],
        "time": max.get_reference_time("date"),
        "status": max.get_detailed_status()}
        min = {
        "temp": min.get_temperature("celsius")["temp"],
        "time": min.get_reference_time("date"),
        "status": min.get_detailed_status()
        }
        return {"max": max, "min": min}

    """fetches the observation using the pyowm library"""
    def pull_observation(self):
        return self.owm.weather_at_place(self.city)

    """fetches the forecast using the pyowm library"""
    def pull_forecast(self):
        f = self.owm.three_hours_forecast(self.city).get_forecast()
        f.actualize()
        return f
