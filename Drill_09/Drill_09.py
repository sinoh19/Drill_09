from pico2d import *


WIDTH, HEIGHT = 800, 600

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

clear_canvas()
background.draw(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT)
character.clip_draw(
    0, 300, 100, 100,
    WIDTH // 2, HEIGHT // 2, 100, 100
)
update_canvas()

close_canvas()
