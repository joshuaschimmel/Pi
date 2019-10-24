# https://tutorials-raspberrypi.com/control-a-raspberry-pi-hd44780-lcd-display-via-i2c/

#import lcddriver
import weather as w
import datetime
import time

"""
LCD-Methods:
lcd_display_string(string, line)
lcd_clear()
lcd_backlight(self, state)
lcd_strobe(data)
lcd_write(cmd, mode=0)
"""
width = 16
height = 2
weather = w.Weather(None, "Hamburg-Mitte")

#lcd = lcddriver.lcd()
#lcd.lcd_clear()


def main():
    """main loop doing all the stuffs TODO"""
    """get and format the data"""
    observation = weather.get_observation()
    forecast = weather.get_forecast()
    draw_list = build_draw_list(observation, forecast)

    try:
        while 1:
            for drawable in draw_list:
                print(drawable[0])
                print(drawable[1], "\n")
                time.sleep(6.5)
            weather.update()
            observation = weather.get_observation()
            forecast = weather.get_forecast()
            draw_list = build_draw_list(observation, forecast)

    except KeyboardInterrupt:
        print("\n\nInterrupt detected, exiting...")



def build_weather_string(observation):
    """
    Builds the weather strings for the display and returns a tupel
    of those strings for each line of the display.
    The input is and observation-dictionary from the Weather class.
    The finished display schould look like the following:
    |dd.mm.yyyy hh:mm| at 16 chr.
    |-00°C light rain| at 16 chr.
    """
    t = observation["time"]
    top_line = "%2.0d.%2.0d.%4.0d %2.0d:%2.0d"
    top_data = (t.day, t.month, t.year, t.hour, t.minute)
    bottom_line ="%3.0fC %s"
    bottom_data = (observation["temp"], observation["status"])
    return (top_line % top_data, bottom_line % bottom_data)

def build_draw_list(observation, forecast):
    """builds the draw list and returns it"""
    observation_tuple = build_weather_string(observation)
    max_tuple = build_weather_string(forecast["max"])
    min_tuple = build_weather_string(forecast["min"])
    """initialise intro text"""
    obs_intro = ("Weather in", "Hamburg-Mitte")
    max_intro = ("Forecast Warmest", "")
    min_intro = ("Forecast Coldest", "")

    draw_list = [
    obs_intro, observation_tuple,
    max_intro, max_tuple,
    min_intro, min_tuple
    ]
    return draw_list

# ads # of whitespaces until str will be displayed at the given
# position
def finishString(str, startPos):
    itr = 0
    while(itr < startPos):
        str = " " + str
        itr += 1

main()
#hello :)
