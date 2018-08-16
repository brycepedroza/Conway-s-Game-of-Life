import pyglet
from gameOfLife import GameOfLife

width = 1500
height = 900

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(width, height)
        self.ticker = 0
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     20)
        pyglet.clock.schedule_interval(self.update, 1.0/20.0)

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()

    def update(self, dt):
        self.gameOfLife.runRules()




if __name__ == '__main__':
    window = Window()
    pyglet.app.run()

