from pico2d import *

class SelectScreen:
    def __init__(self):
        self.select_sheet = load_image('Street Fighter/Select.png')
        self.font_sheet = load_image('Street Fighter/Font.png')
        self.running = True
        self.blink_timer = 0
        self.p1_selected_index = 0
        self.p2_selected_index = 1
        self.character_positions = [(500, 500), (700, 500)]
        self.font = load_font('C:/Windows/Fonts/ARLRDBD.TTF', 40)

    def handle_events(self):
        pass


    def update(self):
        self.blink_timer += 1


    def draw(self):
        clear_canvas()

        self.select_sheet.clip_draw(0, 650, 100, 100, 600, 400, 1200, 800)

        self.font_sheet.clip_draw(350, 119, 130, 18, 600, 700, 600, 70)

        self.select_sheet.clip_draw(0, 495, 110, 125, 500, 450, 200, 250)  # Ryu
        self.select_sheet.clip_draw(0, 370, 110, 125, 700, 450, 200, 250)  # Ken

        if self.p1_selected_index == 0:  # Ryu
            self.select_sheet.clip_draw(0, 495, 110, 125, 200, 450, 300, 350)
        else:  # Ken
            self.select_sheet.clip_draw(0, 370, 110, 125, 200, 450, 300, 350)

            # 2P의 현재 선택 인덱스로 오른쪽 캐릭터 표시
        if self.p2_selected_index == 0:  # Ryu
            self.select_sheet.clip_composite_draw(0, 500, 110, 125, 0, 'h', 1025, 450, 300, 350)
            self.select_sheet.clip_draw(0, 495, 110, 25, 1000, 300, 300, 70)
        else:  # Ken
            self.select_sheet.clip_composite_draw(0, 370, 110, 125, 0, 'h', 1025, 450, 300, 350)
            self.select_sheet.clip_draw(0, 370, 110, 25, 1000, 300, 300, 70)

        if (self.blink_timer // 20) % 2 == 0:
            x1, y1 = self.character_positions[self.p1_selected_index]
            x2, y2 = self.character_positions[self.p2_selected_index]

            # 사각형 테두리
            draw_rectangle(x1 - 80, y1 - 170, x1 + 110, y1 + 70, 255, 0, 0)
            draw_rectangle(x2 - 80, y2 - 170, x2 + 110, y2 + 70, 0, 0, 255)

            # "1P" / "2P" 텍스트
            self.font.draw(x1 - 30, y1 + 110, "1P", (255, 0, 0))
            self.font.draw(x2 + 10, y2 + 110, "2P", (0, 0, 255))

        if (self.blink_timer // 30) % 2 == 0:
            self.font_sheet.clip_draw(420, 200, 296, 224, 650, 200, 300, 100)

        update_canvas()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            delay(0.03)

