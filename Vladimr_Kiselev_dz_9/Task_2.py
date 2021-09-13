# Task_2
class Road:

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness

    def mass_asphalt(self):
        mass = self._length * self._width * 25 * self.thickness
        print(f'Required mass of asphalt: {mass} ton')

some_road = Road(5000, 20, 0.05)
some_road.mass_asphalt()