# ryu.py
from pico2d import *
from character import Character

class Ryu(Character):
    def __init__(self, x, y, flip=False):
        sheet = load_image("Street Fighter/Ryu.png")
        super().__init__(sheet, x, y, flip)

