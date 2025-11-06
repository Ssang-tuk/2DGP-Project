from pico2d import *
from start_screen import StartScreen
from select_screen import SelectScreen

if __name__ == "__main__":
    open_canvas(1200, 800)

    start = StartScreen()
    next_scene = start.run()

    if next_scene == "SELECT":
        select = SelectScreen()
        select.run()

    close_canvas()

    