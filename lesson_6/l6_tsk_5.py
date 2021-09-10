class Stationery:
    def __init__(self, title='Drawtools'):
        self.title = title

    def draw(self):
        print(f'Draw, {self.title}!')


class Pen(Stationery):
    def draw(self):
        print(f'Draw with {self.title} pen!')


class Pencil(Stationery):
    def draw(self):
        print(f'Draw with {self.title} pencil!')


class Marker(Stationery):
    def draw(self):
        print(f'Draw with {self.title} marker!')


stat = Stationery()
pen = Pen("Red")
pencil = Pencil('Grey')
marker = Marker('Black')

supplies = [stat, pen, pencil, marker]
for i in supplies:
    i.draw()
