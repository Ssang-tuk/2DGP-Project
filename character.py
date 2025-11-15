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

        self.x += self.vx


    def get_current_frames(self):

        pass

    # ============================================================
    def draw(self):

         pass