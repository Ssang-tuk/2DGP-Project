from pico2d import *
from ryu import Ryu
from ken import Ken

class FightScreen:
    def __init__(self, p1_index, p2_index):
        self.font_sheet = load_image('Street Fighter/Font.png')
        self.stage_1 = load_image('Street Fighter/Stage_1.png')
        self.stage_1_T = load_image('Street Fighter/Stage_1_T.png')

        self.running = True

        character_classes = [Ryu, Ken]

        # 스프라이트는 기본 왼쪽 시선 이므로  P1만 flip(True)
        self.p1 = character_classes[p1_index](300, 200, flip=True)
        self.p2 = character_classes[p2_index](900, 200, flip=False)

    #   입력 처리: KEY 에서 action 변환하기
    def handle_events(self):
        events = get_events()

        for e in events:
            if e.type == SDL_QUIT:
                self.running = False

            if e.type == SDL_KEYDOWN:

                # ------------------------------
                #   P1 입력 (WASD + 4,5)
                # ------------------------------
                if e.key == SDLK_d:
                    self.p1.handle_action("MOVE_FORWARD")
                elif e.key == SDLK_a:
                    self.p1.handle_action("MOVE_BACKWARD")
                elif e.key == SDLK_w:
                    self.p1.handle_action("JUMP")
                elif e.key == SDLK_s:
                    self.p1.handle_action("CROUCH")
                elif e.key == SDLK_4:
                    self.p1.handle_action("PUNCH")
                elif e.key == SDLK_5:
                    self.p1.handle_action("KICK")


                #   P2 입력 (화살표 + , .)

                elif e.key == SDLK_LEFT:
                    self.p2.handle_action("MOVE_FORWARD")
                elif e.key == SDLK_RIGHT:
                    self.p2.handle_action("MOVE_BACKWARD")
                elif e.key == SDLK_UP:
                    self.p2.handle_action("JUMP")
                elif e.key == SDLK_DOWN:
                    self.p2.handle_action("CROUCH")
                elif e.key == ord(','):
                    self.p2.handle_action("PUNCH")
                elif e.key == ord('.'):
                    self.p2.handle_action("KICK")

            # -------- KEYUP --------
            elif e.type == SDL_KEYUP:

                # P1 멈춤
                if e.key in (SDLK_d, SDLK_a):
                    self.p1.handle_action("STOP")
                if e.key == SDLK_s:
                    self.p1.handle_action("CROUCH_RELEASE")

                # P2 멈춤
                if e.key in (SDLK_LEFT, SDLK_RIGHT):
                    self.p2.handle_action("STOP")
                if e.key == SDLK_DOWN:
                    self.p2.handle_action("CROUCH_RELEASE")

    # =========================================================
    def update(self):
        self.p1.update()
        self.p2.update()

    # =========================================================
    def draw(self):
        clear_canvas()

        self.stage_1.clip_draw(10, 150, 770, 210, 600, 350, 1220, 500)
        self.stage_1_T.clip_draw(10, 380, 1020, 170, 600, 150, 1200, 300)
        self.stage_1.clip_draw(10, 560, 770, 54, 600, 680, 1220, 250)

        self.stage_1_T.clip_draw(920, 264, 100, 13, 536, 312, 102, 25)
        self.stage_1_T.clip_draw(935, 290, 87, 64, 850, 330, 102, 64)

        self.p1.draw()
        self.p2.draw()
        update_canvas()

    # =========================================================
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)
