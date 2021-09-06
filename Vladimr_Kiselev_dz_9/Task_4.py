# Task_4
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = True


    def go(self):
        print(f'{self.name} went')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}\n')

    def show_speed(self):
        print(f'current speed of: {self.speed} ')

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'warning: overspeed by {self.speed - 60}')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'warning: overspeed by {self.speed - 40}')

class PoliceCar(Car):
    pass
class SportCar(Car):
    pass

car_1 = WorkCar(80, 'red', 'bibka', False)
car_1.show_speed()
car_1.turn('to the left')

car_2 = TownCar(80, 'blue', "brun'-brun'", False)
car_2.show_speed()
car_2.turn('to the right')