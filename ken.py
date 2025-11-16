# ken.py
from pico2d import *
from character import Character

class Ken(Character):
    def __init__(self, x, y, flip=False):
        sheet = load_image("Street Fighter/Ken.png")
        super().__init__(sheet, x, y, flip)

        self.idle_frames = [(1, 10660, 64, 96), (66, 10660, 64, 96), (131, 10660, 64, 96), (196, 10660, 64, 96)]
        self.walk_forward_frames = [(1, 10290, 79, 94), (82, 10290, 79, 94), (163, 10290, 79, 94), (244, 10290, 79, 94), (325, 10290, 79, 94)]  # 상대쪽
        self.walk_backward_frames = [(1, 10193, 79, 94), (82, 10193, 79, 94), (163, 10193, 79, 94), (244, 10193, 79, 94), (325, 10193, 79, 94), (406, 10193, 79, 94)]  # 뒤로가기
        self.punch_frames = [(1, 9676, 127, 94), (130, 9676, 127, 94), (259, 9676, 127, 94)]
        self.kick_frames = [(1, 8803, 127, 94), (130, 8803, 127, 94)]
        self.jump_frames = [(1, 9967, 63, 110), (66, 9967, 63, 110), (131, 9967, 63, 110), (196, 9967, 63, 110), (261, 9967, 63, 110), (326, 9967, 63, 110)]
        self.crouch_frames = [(1, 10452, 79, 94), (82, 10452, 79, 94), (163, 10452, 79, 94)]
        self.crouch_punch_frames = [(1, 9207, 111, 62), (114, 9207, 111, 62), (227, 9207, 111, 62)]
        self.crouch_kick_frames = [(1, 8237, 159, 62), (162, 8237, 159, 62)]