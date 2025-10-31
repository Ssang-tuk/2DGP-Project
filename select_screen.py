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


        update_canvas()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)

