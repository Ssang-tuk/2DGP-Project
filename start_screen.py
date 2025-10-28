from pico2d import *

class StartScreen:
    def __init__(self):

        self.background = load_image('Street Fighter/Title_T.png')
        self.background2 = load_image('Street Fighter/Title.png')
        self.logo_sheet = load_image('Street Fighter/Logo_1.png')
        self.font = load_image('Street Fighter/Font.png')

        self.blink_timer = 0
        self.running = True

        self.start_x, self.start_y = 640, 250
        self.start_w, self.start_h = 300, 100

        self.next_scene = None

    def handle_events(self):
        events = get_events()
        for q in events:
            if q.type == SDL_QUIT:
                self.running = False
                self.next_scene = None
            elif q.type == SDL_MOUSEBUTTONDOWN:
                mx, my = q.x, 800 - q.y
                if self.is_start_clicked(mx, my):
                    print("Start 클릭됨!")
                    self.running = False
                    self.next_scene = "SELECT"

    def is_start_clicked(self, mx, my):
        left = self.start_x - (self.start_w // 2)
        right = self.start_x + (self.start_w // 2)
        bottom = self.start_y - (self.start_h // 2)
        top = self.start_y + (self.start_h // 2)
        return left <= mx <= right and bottom <= my <= top

    def update(self):
        self.blink_timer += 1

    def draw(self):
        clear_canvas()

        self.background2.clip_draw(10, 138, 380, 380, 200, 400, 400, 900)
        self.background2.clip_draw(10, 138, 380, 380, 600, 400, 400, 900)
        self.background2.clip_draw(10, 138, 380, 380, 1000, 400, 400, 900)
        self.background.clip_draw(400, 0, 385, 528, 200, 375, 400, 900)
        self.background.clip_composite_draw(400, 0, 385, 528, 0, 'h', 600, 375, 400, 900)
        self.background.clip_draw(400, 0, 385, 528, 1000, 375, 400, 900)
        self.background.clip_draw(10, 10, 380, 100, 200, 50, 400, 100)
        self.background.clip_draw(10, 10, 380, 100, 600, 50, 400, 100)
        self.background.clip_draw(10, 10, 380, 100, 1000, 50, 400, 100)
        self.background.clip_draw(800, 423, 270, 100, 200, 660, 155, 120)
        self.background.clip_draw(785, 280, 290, 130, 600, 660, 155, 120)
        self.background.clip_draw(785, 15, 120, 130, 955, 660, 70, 120)
        self.background.clip_draw(845, 175, 230, 100, 1010, 650, 140, 100)
        self.logo_sheet.clip_draw(0, 410, 300, 140, 600, 500, 500, 250)

        if (self.blink_timer // 30) % 2 == 0:
            self.font.clip_draw(420, 200, 296, 224,
                                self.start_x, self.start_y,
                                self.start_w, self.start_h)
        update_canvas()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)

        return self.next_scene
