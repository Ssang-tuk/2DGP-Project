from pico2d import *
from start_screen import StartScreen


if __name__ == "__main__":
    open_canvas(1200, 800)

    start = StartScreen()
    next_scene = start.run()

    close_canvas()
