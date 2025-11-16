# ryu.py
from pico2d import *
from character import Character

class Ryu(Character):
    def __init__(self, x, y, flip=False):
        sheet = load_image("Street Fighter/Ryu.png")
        super().__init__(sheet, x, y, flip)

        self.idle_frames = [(1, 11116, 64, 96), (66, 11116, 64, 96), (131, 11116, 64, 96), (196, 11116, 64, 96)]
        self.walk_forward_frames = [(1, 10745, 79, 95), (82, 10745, 79, 95), (163, 10745, 79, 95), (244, 10745, 79, 95), (325, 10745, 79, 95)]  # 상대쪽
        self.walk_backward_frames = [(1, 10648, 79, 95), (82, 10648, 79, 95), (163, 10648, 79, 95), (244, 10648, 79, 95), (325, 10648, 79, 95), (406, 10648, 79, 95)]  # 뒤로가기
        self.punch_frames = [(1, 10132, 127, 94), (130, 10132, 127, 94), (259, 10132, 127, 94)]
        self.kick_frames = [(1, 9258, 127, 94), (130, 9258, 127, 94)]
        self.jump_frames = [(1, 10422, 63, 111), (66, 10422, 63, 111), (131, 10422, 63, 111), (196, 10422, 63, 111), (261, 10422, 63, 111), (326, 10422, 63, 111)]
        self.crouch_frames = [(1, 10907, 80, 95), (82, 10907, 80, 95), (163, 10907, 80, 95)]
        self.crouch_punch_frames = [(1, 9662, 111, 62), (114, 9662, 111, 62), (227, 9662, 111, 62)]
        self.crouch_kick_frames = [(1, 8757, 159, 62), (162, 8757, 159, 62)]

