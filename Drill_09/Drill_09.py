from pico2d import *


WIDTH, HEIGHT = 800, 600
CHARACTER_SIZE = 100
SPEED = 5

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
pressed_keys = set()
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
facing = 1


def handle_events():
    global running, facing

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN):
                pressed_keys.add(event.key)
                if event.key == SDLK_RIGHT:
                    facing = 1
                elif event.key == SDLK_LEFT:
                    facing = -1
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)


while running:
    handle_events()

    dir_x = int(SDLK_RIGHT in pressed_keys) - int(SDLK_LEFT in pressed_keys)
    dir_y = int(SDLK_UP in pressed_keys) - int(SDLK_DOWN in pressed_keys)

    if dir_x != 0:
        facing = dir_x

    x += dir_x * SPEED
    y += dir_y * SPEED

    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT)
    character.clip_draw(
        frame * 100, 300 if facing == 1 else 200, 100, 100,
        x, y, CHARACTER_SIZE, CHARACTER_SIZE
    )
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
