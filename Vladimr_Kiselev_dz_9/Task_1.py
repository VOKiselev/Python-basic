# Task_1
from itertools import cycle
import time

class TrafficLight:

    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for color, sec in cycle(self.__color.items()):
            print(f'Now {color} light')
            time.sleep(sec)

traffic_light =TrafficLight()
traffic_light.running()