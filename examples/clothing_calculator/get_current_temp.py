import requests
import configparser
import os

# Uses Open Weather Map API
# https://openweathermap.org/current
def get_current_weather():
    # Compute config file path
    config = configparser.ConfigParser()
    root_path_list = os.path.dirname(os.path.abspath(__file__)).split('/')[:-2]
    config_path = "/".join(root_path_list) + '/secrets.ini'
    config.read(config_path)

    api_key = config['DEFAULT']['weather_api_key']

    # New York Brooklyn Weather URL
    lat = "40.678178"
    lon = "-73.944158"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}' \
          f'&appid={api_key}&units=metric'

    res = requests.get(url)
    return res.json()
