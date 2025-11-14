# ken.py
from pico2d import *
from character import Character

class Ken(Character):
    def __init__(self, x, y, flip=False):
        sheet = load_image("Street Fighter/Ken.png")
        super().__init__(sheet, x, y, flip)

