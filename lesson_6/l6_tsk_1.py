import time
import itertools


class TrafficLights:
    __color = ['Green', [7, 32]], ['Yellow', [2, 33]], ['Red', [7, 31]], ['Yellow', [2, 33]]

    def process(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end="")
            time.sleep(light[1][0])


TF = TrafficLights()
TF.process()
