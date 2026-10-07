import os

from pico2d import *


WIDTH, HEIGHT = 800, 600
CHARACTER_SIZE = 100
SPEED = 5

# 상대 경로 이미지 로드의 기준을 이 파일이 있는 폴더로 고정한다.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
pressed_keys = set()
x, y = WIDTH // 2, HEIGHT // 2
frame = 0
facing = 1  # 1: 오른쪽, -1: 왼쪽
animation = 300  # 오른쪽 idle


def handle_events():
    global running, facing

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN):
                # 집합을 사용해 키 반복 입력에도 속도가 증가하지 않게 한다.
                pressed_keys.add(event.key)
                if event.key == SDLK_RIGHT:
                    facing = 1
                elif event.key == SDLK_LEFT:
                    facing = -1
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)


while running:
    handle_events()
    if not running:
        break

    dir_x = int(SDLK_RIGHT in pressed_keys) - int(SDLK_LEFT in pressed_keys)
    dir_y = int(SDLK_UP in pressed_keys) - int(SDLK_DOWN in pressed_keys)

    # 좌우 키가 함께 눌렸다가 하나만 해제되어도 이동 방향을 바라본다.
    if dir_x != 0:
        facing = dir_x

    half_size = CHARACTER_SIZE // 2
    next_x = max(half_size, min(WIDTH - half_size, x + dir_x * SPEED))
    next_y = max(half_size, min(HEIGHT - half_size, y + dir_y * SPEED))
    moving = next_x != x or next_y != y
    x, y = next_x, next_y

    # clip_draw의 세로 좌표는 이미지 아래쪽부터 계산한다.
    # 아래부터 왼쪽 이동, 오른쪽 이동, 왼쪽 idle, 오른쪽 idle.
    if moving:
        next_animation = 100 if facing == 1 else 0
    else:
        next_animation = 300 if facing == 1 else 200

    if animation != next_animation:
        animation = next_animation
        frame = 0

    clear_canvas()
    background.draw(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT)
    character.clip_draw(
        frame * 100, animation, 100, 100,
        x, y, CHARACTER_SIZE, CHARACTER_SIZE
    )
    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
