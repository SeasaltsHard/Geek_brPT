import random
from random import choice


class Car:
    """Main car"""
    direction = ['⬆ north', '↗ northeast', '➡ east', '↘ southeast', '⬇ south',
                 '↙ southwest', '⬅ west', '↖ northwest']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n}. Colored in {c}.\nPolice? {p}')

    def start(self):
        print(f'{self.name}: Engine on!')

    def stop(self):
        print(f'{self.name}: Engine off!')

    def turn(self):
        print(f'{self.name}: turned {random.choice(Car.direction)}')

    def car_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):
    """Town car"""

    def car_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().car_speed()


class WorkCar(Car):
    """Cargo truck"""

    def car_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().car_speed()


class SportCar(Car):
    """Sport Car"""

    def car_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 240 else super().car_speed()


class PoliceCar(Car):
    """Patrol Car"""

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)

    def car_speed(self):
        return f'{self.name}: Car speed: {self.speed}. No limit mode.'


Town_Car = TownCar('Renault X5', 'Безцветный', 75)
Cargo_truck = WorkCar('BMW Cargo', 'Белый', 50)
Sport_Car = SportCar('Копейка', 'Из-за грязи не видно', 45)
Patrol_car = PoliceCar('Xiaomi', 'Серый', 250)

Car_list = [Town_Car, Cargo_truck, Sport_Car, Patrol_car]

for car in Car_list:
    car.start()
    print(car.car_speed())
    car.turn()
    car.stop()
    print()
