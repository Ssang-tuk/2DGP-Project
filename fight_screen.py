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

        self.stage_1.clip_draw(10, 150, 770, 210, 600, 350, 1220, 500)
        self.stage_1_T.clip_draw(10, 380, 1020, 170, 600, 150, 1200, 300)
        self.stage_1.clip_draw(10, 560, 770, 54, 600, 680, 1220, 250)

        self.stage_1_T.clip_draw(920, 264, 100, 13, 536, 312, 102, 25)
        self.stage_1_T.clip_draw(935, 290, 87, 64, 850, 330, 102, 64)

        update_canvas()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)
        close_canvas()