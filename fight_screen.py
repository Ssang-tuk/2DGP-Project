from pico2d import *

class FightScreen:
    def __init__(self):
        self.font_sheet = load_image('Street Fighter/Font.png')
        self.stage_1 = load_image('Street Fighter/Stage_1.png')
        self.stage_1_T = load_image('Street Fighter/Stage_1_T.png')


        self.running = True



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