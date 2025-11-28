character.py


from pico2d import *

class Character:
    def __init__(self, sheet, x, y, flip=False):
        self.sheet = sheet
        self.x, self.y = x, y
        self.flip = flip

        # 기본 상태
        self.state = "IDLE"
        self.frame = 0
        self.ftimer = 0

        # 이동 속도
        self.vx = 0
        self.vy = 0

        # 바닥 위치
        self.ground_y = y

        # 점프 파라미터
        self.jump_force = 14
        self.gravity = 1

        self.hit_timer = 0

        # 프레임 리스트
        self.idle_frames = []
        self.walk_forward_frames = []
        self.walk_backward_frames = []
        self.punch_frames = []
        self.kick_frames = []
        self.jump_frames = []
        self.crouch_frames = []
        self.crouch_punch_frames = []
        self.crouch_kick_frames = []
        self.hit_light_frames = []
        self.hit_heavy_frames = []
        self.hit_low_frames = []
        self.hit_sweep_frames = []

        self.air_hit_frames = []  # 공중 피격
        self.getup_frames = []  # 일어나기

        self.death_frames = []

        self.has_hit = False

    def handle_action(self, action):

        if self.state == "JUMP":

            # 공중 좌/우 이동 허용
            if action == "MOVE_FORWARD":
                self.vx = +5 if self.flip else -5
                return

            if action == "MOVE_BACKWARD":
                self.vx = -5 if self.flip else +5
                return

            if action == "STOP":
                self.vx = 0
                return

            # 공중에서 숙이기 불가
            if action in ("CROUCH", "CROUCH_RELEASE"):
                return

            return

        # == 지상 처리 ==

        if action == "MOVE_FORWARD":
            self.vx = +5 if self.flip else -5
            self.state = "WALK_FORWARD"

        elif action == "MOVE_BACKWARD":
            self.vx = -5 if self.flip else +5
            self.state = "WALK_BACKWARD"

        elif action == "STOP":
            self.vx = 0
            self.state = "IDLE"

        elif action == "PUNCH":
            if self.state == "CROUCH":
                self.state = "CROUCH_PUNCH"
            else:
                self.state = "PUNCH"
            self.frame = 0

        elif action == "KICK":
            if self.state == "CROUCH":
                self.state = "CROUCH_KICK"
            else:
                self.state = "KICK"
            self.frame = 0

        elif action == "JUMP":
            self.state = "JUMP"
            self.frame = 0
            self.ftimer = 0
            self.vy = self.jump_force

        elif action == "CROUCH":
            self.state = "CROUCH"
            self.frame = 0

        elif action == "CROUCH_RELEASE":
            if self.state == "CROUCH":
                self.state = "IDLE"
                self.frame = 0

    def update(self):

        if self.state == "DEAD":
            # 마지막 프레임에서 고정
            if self.frame < len(self.death_frames) - 1:
                self.ftimer += 1
                if self.ftimer >= 6:
                    self.ftimer = 0
                    self.frame += 1
            return

        if self.state == "AIR_HIT":
            self.vy -= self.gravity
            self.y += self.vy
            self.x += self.vx * 0.7

            # 프레임 진행
            self.ftimer += 1
            if self.ftimer >= 5:
                self.ftimer = 0
                self.frame = min(self.frame + 1, len(self.air_hit_frames) - 1)

            # 바닥에 닿으면 GETUP으로 이동
            if self.y <= self.ground_y:
                self.y = self.ground_y
                self.vy = 0
                self.vx = 0
                self.state = "GETUP"
                self.frame = 0
                self.ftimer = 0

            return  # 다른 동작 차단

        if self.state == "GETUP":
            self.ftimer += 1
            if self.ftimer >= 6:
                self.ftimer = 0
                self.frame += 1

                if self.frame >= len(self.getup_frames):
                    self.state = "IDLE"
                    self.frame = 0
                    self.is_hit = False

            return  # 다른 동작 차단


        # ===== HIT 상태 처리 =====
        if getattr(self, "is_hit", False):
            self.hit_timer -= 1
            self.x += self.vx  # 넉백 적용

            if self.hit_timer <= 0:
                self.is_hit = False
                self.vx = 0
                self.state = "IDLE"
                self.frame = 0

            return  # 다른 상태 로직 막기

        self.x += self.vx

        # 점프 처리
        if self.state == "JUMP":
            self.y += self.vy
            self.vy -= self.gravity

            if self.y <= self.ground_y:
                self.y = self.ground_y
                self.vy = 0
                self.state = "IDLE"
                self.frame = 0

            # 프레임 속도
        speed = 3 if self.state == "JUMP" else 6

        self.ftimer += 1
        if self.ftimer >= speed:
            self.ftimer = 0
            self.frame += 1

        frames = self.get_current_frames()

        # 안전장치
        if not frames:
            return

        # 프레임 모션이 반복되지 않는것

        if self.state in ("JUMP", "CROUCH",
                          "PUNCH", "KICK",
                          "CROUCH_PUNCH", "CROUCH_KICK"):

            if self.frame >= len(frames):

                self.has_hit = False

                # CROUCH 유지 (마지막 프레임 고정)
                if self.state == "CROUCH":
                    self.frame = len(frames) - 1

                # crouch 공격 → crouch로 복귀
                elif self.state in ("CROUCH_PUNCH", "CROUCH_KICK"):
                    self.state = "CROUCH"
                    self.frame = len(self.crouch_frames) - 1

                # standing 공격 → idle로 복귀
                elif self.state in ("PUNCH", "KICK"):
                    self.state = "IDLE"
                    self.frame = 0

                # 점프는 착지에서 처리됨
                else:
                    self.frame = len(frames) - 1

            # 반복되는 모션들
        else:
            self.frame %= len(frames)

    def get_current_frames(self):

        if self.state == "IDLE": return self.idle_frames
        if self.state == "WALK_FORWARD": return self.walk_forward_frames
        if self.state == "WALK_BACKWARD": return self.walk_backward_frames
        if self.state == "PUNCH": return self.punch_frames
        if self.state == "KICK": return self.kick_frames
        if self.state == "JUMP": return self.jump_frames
        if self.state == "CROUCH": return self.crouch_frames
        if self.state == "CROUCH_PUNCH": return self.crouch_punch_frames
        if self.state == "CROUCH_KICK": return self.crouch_kick_frames

        if self.state == "HIT_LIGHT": return self.hit_light_frames
        if self.state == "HIT_HEAVY": return self.hit_heavy_frames
        if self.state == "HIT_LOW": return self.hit_low_frames
        if self.state == "HIT_SWEEP": return self.hit_sweep_frames

        if self.state == "AIR_HIT": return self.air_hit_frames
        if self.state == "GETUP": return self.getup_frames

        if self.state == "DEAD": return self.death_frames

        return self.idle_frames

    # ============================================================
    def draw(self):
        frames = self.get_current_frames()
        if not frames:
            return

        if self.frame >= len(frames):
            self.frame = len(frames) - 1

        fx, fy, fw, fh = frames[self.frame]

        draw_x = self.x
        draw_y = self.y

        if self.state == "CROUCH_PUNCH" or self.state == "CROUCH_KICK":
            draw_y -= 33

        if self.state == "HIT_LOW" or self.state == "HIT_SWEEP":
            draw_y -= 40

        if self.state == "GETUP" or self.state == "AIR_HIT":
            draw_y += 20

        if self.state == "DEAD":
            draw_y -= 20

        if self.flip:
            if self.state == "CROUCH_PUNCH" or self.state == "CROUCH_KICK" or self.state == "PUNCH":
                draw_x += 20
            self.sheet.clip_composite_draw(
                fx, fy, fw, fh,
                0, 'h',
                draw_x, draw_y,
                fw * 2, fh * 2
            )
        else:
            if self.state == "CROUCH_PUNCH" or self.state == "CROUCH_KICK" or self.state == "PUNCH":
                draw_x -= 20
            self.sheet.clip_draw(
                fx, fy, fw, fh,
                draw_x, draw_y,
                fw * 2, fh * 2
            )

    def get_hitbox(self):
        frames = self.get_current_frames()
        if not frames:
            return None

        fx, fy, fw, fh = frames[self.frame]

        w = fw * 2
        h = fh * 2

        # 기본 hitbox
        left = self.x - (w // 2)
        right = self.x + (w // 2)
        bottom = self.y - (h // 2)
        top = self.y + (h // 2)

        if self.state == "CROUCH":
            top -= 70
            left += 10
            right -= 10

        elif self.state in ("CROUCH_PUNCH", "CROUCH_KICK"):
            bottom -= 30
            top -= 30

        elif self.state in ("JUMP"):
            bottom += 20



        return (left, bottom, right, top)

    def debug_draw(self):
        hb = self.get_hitbox()
        if hb:
            draw_rectangle(hb[0], hb[1], hb[2], hb[3])  # 초록색

        atk = self.get_attack_box()
        if atk:
            draw_rectangle(atk[0], atk[1], atk[2], atk[3], 255, 0, 0)  # 빨강

    def get_attack_box(self):
        frames = self.get_current_frames()
        if not frames:
            return None

        # 공격 상태가 아니면 없음
        if self.state not in ("PUNCH", "KICK", "CROUCH_PUNCH", "CROUCH_KICK"):
            return None

        fx, fy, fw, fh = frames[self.frame]

        w = fw * 2
        h = fh * 2

        left = self.x - (w // 2)
        right = self.x + (w // 2)
        bottom = self.y - (h // 2)
        top = self.y + (h // 2)

        if self.state == "PUNCH":
            left += 40
            right += 5
            bottom += 125
            top -= 30

        elif self.state == "KICK":
            left += 70
            right -= 10
            bottom += 125


        elif self.state == "CROUCH_PUNCH":
            left += 50
            right += 10
            bottom += 50
            top -= 55

        elif self.state == "CROUCH_KICK":
            left += 110
            right += 5
            bottom -= 30
            top -= 120

        # =========================================
        # flip 방향 반전 처리
        # =========================================
        if not self.flip:  # 오른쪽 바라볼 때 좌우 반전 필요
            width = right - left
            left = self.x - (left - self.x) - width
            right = left + width

        return (left, bottom, right, top)

    def take_hit(self, attack_type):
        # 이미 피격 중이면 추가 피격 무시
        if getattr(self, "is_hit", False):
            return

        self.is_hit = True
        self.frame = 0
        self.ftimer = 0

        # 공중 피격
        if self.state == "JUMP":
            self.state = "AIR_HIT"
            self.vy = -5
            self.vx = -4 if self.flip else 4
            self.hit_timer = 999  # 타이머 대신 착지 조건으로 끝남
            return

        # 피격 애니메이션 선택
        if attack_type == "PUNCH":
            self.state = "HIT_LIGHT"

        elif attack_type == "KICK":
            self.state = "HIT_HEAVY"

        elif attack_type == "CROUCH_PUNCH":
            self.state = "HIT_LOW"

        elif attack_type == "CROUCH_KICK":
            self.state = "HIT_SWEEP"  # 넘어짐 모션 가능

        # 넉백 (flip 방향 반대로 밀리게)
        if self.flip:
            self.vx = -3
        else:
            self.vx = 3

        # 피격 유지 시간 (프레임 수)
        self.hit_timer = 20

    def die(self):
        self.state = "DEAD"
        self.vx = 0
        self.vy = 0
        self.frame = 0
        self.ftimer = 0
        self.is_hit = False

