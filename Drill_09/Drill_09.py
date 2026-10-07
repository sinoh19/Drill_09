from pico2d import *


WIDTH, HEIGHT = 800, 600
CHARACTER_SIZE = 100

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
pressed_keys = set()
x, y = WIDTH // 2, HEIGHT // 2
frame = 0


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN):
                pressed_keys.add(event.key)
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)


while running:
    handle_events()

    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT)
    character.clip_draw(
        frame * 100, 300, 100, 100,
        x, y, CHARACTER_SIZE, CHARACTER_SIZE
    )
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
