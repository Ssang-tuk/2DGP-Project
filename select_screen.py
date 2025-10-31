from pico2d import *

class SelectScreen:
    def __init__(self):
        self.select_sheet = load_image('Street Fighter/Select.png')
        self.font_sheet = load_image('Street Fighter/Font.png')
        self.running = True
        self.blink_timer = 0
        self.p1_selected_index = 0
        self.p2_selected_index = 1


    def handle_events(self):
        pass


    def update(self):
        pass

    def draw(self):
        clear_canvas()

        self.select_sheet.clip_draw(0, 650, 100, 100, 600, 400, 1200, 800)

        self.font_sheet.clip_draw(350, 119, 130, 18, 600, 700, 600, 70)

        self.select_sheet.clip_draw(0, 495, 110, 125, 500, 450, 200, 250)  # Ryu
        self.select_sheet.clip_draw(0, 370, 110, 125, 700, 450, 200, 250)  # Ken

        update_canvas()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)

