
from pico2d import *
from start_screen import StartScreen
from select_screen import SelectScreen
from fight_screen import FightScreen

if __name__ == "__main__":
    open_canvas(1200, 800)
    start = StartScreen()
    next_scene = start.run()

    if next_scene == "SELECT":
        select = SelectScreen()

        next_scene, p1_index, p2_index = select.run()

        if next_scene == "FIGHT":
            fight = FightScreen(p1_index, p2_index)
            fight.run()

    close_canvas()
