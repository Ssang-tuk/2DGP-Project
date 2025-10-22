from pico2d import *

class StartScreen:
    def __init__(self):
        open_canvas(1200, 800)

        self.background = load_image('Street Fighter/Title_T.png')
        self.background2 = load_image('Street Fighter/Title.png')
        self.logo_sheet = load_image('Street Fighter/Logo_1.png')
        self.font = load_image('Street Fighter/Font.png')

        self.blink_timer = 0
        self.running = True

        self.logo_x, self.logo_y, self.logo_w, self.logo_h = 0, 410, 300, 140

    def handle_events(self):
        events = get_events()
        for q in events:
            if q.type == SDL_QUIT:
                self.running = False
            elif q.type == SDL_KEYDOWN and q.key == SDLK_RETURN:
                self.running = False


    def update(self):
        pass

    def draw(self):
        clear_canvas()


        update_canvas()

    def run(self):

        close_canvas()
