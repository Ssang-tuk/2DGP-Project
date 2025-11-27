from pico2d import *
from ryu import Ryu
from ken import Ken

def box_intersects(a, b):
    if not a or not b:
        return False
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])

class FightScreen:
    def __init__(self, p1_index, p2_index):
        self.font_sheet = load_image('Street Fighter/Font.png')
        self.stage_1 = load_image('Street Fighter/Stage_1.png')
        self.stage_1_T = load_image('Street Fighter/Stage_1_T.png')
        self.fight_img = load_image("Street Fighter/Fight.png")
        self.ko_img = load_image("Street Fighter/KO.png")
        self.show_ko = False
        self.show_fight = True
        self.fight_timer = 1.0

        self.running = True

        self.hp_max = 100
        self.p1_hp = self.hp_max
        self.p2_hp = self.hp_max

        self.hp_bar_full = self.font_sheet
        self.hp_bar_fill = self.font_sheet

        self.hp_full_clip = (13, 209, 327, 15)
        self.hp_fill_clip = (13, 193, 327, 15)

        self.hp_half = self.hp_full_clip[2] // 2

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

                p1_locked = self.p1.state in ("AIR_HIT", "GETUP", "HIT_LIGHT", "HIT_HEAVY", "HIT_LOW", "HIT_SWEEP")
                p2_locked = self.p2.state in ("AIR_HIT", "GETUP", "HIT_LIGHT", "HIT_HEAVY", "HIT_LOW", "HIT_SWEEP")

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

        if self.show_fight:
            self.fight_timer -= 0.02  # delay(0.02) 맞춰서 감소
            if self.fight_timer <= 0:
                self.show_fight = False
            return

        p1_atk = self.p1.get_attack_box()
        p2_body = self.p2.get_hitbox()

        p2_atk = self.p2.get_attack_box()
        p1_body = self.p1.get_hitbox()

        # P1 hits P2?
        if p1_atk and not self.p1.has_hit and box_intersects(p1_atk, p2_body):
            self.p2.take_hit(self.p1.state)  # 공격 종류 전달
            self.p1.has_hit = True

            self.p2_hp = max(0, self.p2_hp - 10)
            print(f"P1 HIT! ({self.p1.state})  → P2 HP: {self.p2_hp}")

        # P2 hits P1?
        if p2_atk and not self.p2.has_hit and box_intersects(p2_atk, p1_body):
            self.p1.take_hit(self.p2.state)
            self.p2.has_hit = True

            self.p1_hp = max(0, self.p1_hp - 10)
            print(f"P2 HIT! ({self.p2.state})  → P1 HP: {self.p1_hp}")

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