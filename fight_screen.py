from pico2d import *

class FightScreen:
    def __init__(self):
        pass

    def handle_events(self):
        events = get_events()


    def update(self):
        pass

    def draw(self):
        clear_canvas()




        update_canvas()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)
        close_canvas()