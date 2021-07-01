import json
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebTemp.settings')
import django
django.setup()
from WebT.models import TData, Sensor
from django.utils import timezone


def add_temp(temp, sensor):
    t = TData(sensor=sensor, amount=temp, datetime=timezone.now())
    t.save()
    sensor.in_range = (sensor.min_temperature <= float(temp) < sensor.max_temperature)
    sensor.save()
    

def change_range(temp, sensor):
    sensor.in_range=(sensor.min_temperature <= temp < sensor.max_temperature)
    print(sensor.min_temperature <= temp < sensor.max_temperature)
    sensor.save()


while True:
    for sensor in Sensor.objects.all():
        url = "http://"+ sensor.ip_address + "/"
        print(url)
        try:
            loaded_html = urlopen(url).read()
            soup = BeautifulSoup(loaded_html, 'html.parser')
            temp = soup.text
            print(temp)
            add_temp(temp, sensor)
            temp = -56
        except:
            print('error')



        # parsed_string = json.loads(loaded_json)
        # add_temp(parsed_string['current']['temp'])
        # print(parsed_string['current']['temp'])
    time.sleep(300)
    # URL = "https://api.openweathermap.org/data/2.5/onecall?lat=59.88333&lon=29.9&exclude=hourly,daily&appid=cb1acd1ea672c75643fb8d6872e7e3b3&units=metric"
    # loaded_json = urlopen(URL).read()
    # parsed_string = json.loads(loaded_json)
    # print(parsed_string['current']['temp'])
    # add_temp(parsed_string['current']['temp'])
