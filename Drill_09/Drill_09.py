from pico2d import *


WIDTH, HEIGHT = 800, 600

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')

clear_canvas()
background.draw(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT)
update_canvas()

close_canvas()
