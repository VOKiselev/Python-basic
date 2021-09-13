#Task_5
class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start rendering')

class Pen(Stationary):
    def draw(self):
        print(f'Start recording with {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Starting {self.title} drawing')

class Handle(Stationary):
    def draw(self):
        print(f'Starting selection with {self.title}')

brush_0 = Stationary('Brush')
brush_0.draw()
brush_1 = Pen('Pen')
brush_1.draw()
brush_2 = Pencil('Pencil')
brush_2.draw()
brush_3 = Handle('Handle')
brush_3.draw()