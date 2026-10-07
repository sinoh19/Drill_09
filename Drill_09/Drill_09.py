from pico2d import *


WIDTH, HEIGHT = 800, 600
CHARACTER_SIZE = 100

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = WIDTH // 2, HEIGHT // 2

while running:
    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT)
    character.clip_draw(
        0, 300, 100, 100,
        x, y, CHARACTER_SIZE, CHARACTER_SIZE
    )
    update_canvas()

close_canvas()
