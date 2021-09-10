class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_amount(self, weight=25, thickness=5):
        return print(f'Amount of asphalt needed = \033[31m{self.length * self.width * weight * thickness / 1000}'
                     f'\033[0m tons')
# Colours are fun! Thank you!


a = Road(2000, 25)
(a.mass_amount())
