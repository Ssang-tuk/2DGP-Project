# ken.py
from pico2d import *
from character import Character

class Ken(Character):
    def __init__(self, x, y, flip=False):
        sheet = load_image("Street Fighter/Ken.png")
        super().__init__(sheet, x, y, flip)

        self.idle_frames = []
        self.walk_forward_frames = []
        self.walk_backward_frames = []
        self.punch_frames = []
        self.kick_frames = []
        self.jump_frames = []
        self.crouch_frames = []
        self.crouch_punch_frames = []
        self.crouch_kick_frames = []