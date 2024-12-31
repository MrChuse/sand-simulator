import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 600
HEIGHT = 600
FPS = 60

class GP:
    FLOOR_LEVEL = 300
    SAND_SIZE = 1
    PARTICLE = 500



randx = []
for i in range(GP.PARTICLE):
    randx.append(random.randint(1, HEIGHT))
    # randx.append(i * 10)

randy = []
for i in range(GP.PARTICLE):
    randy.append(random.randint(1, GP.FLOOR_LEVEL))
    # randy.append(i * 10)

def sandfall(color, posx, posy, ss):
    screen.fill(color, (posx, posy, ss, ss))
    screen.fill(BLACK, (posx, posy-ss, ss, ss))


def draw_on_screen(screen: pygame.Surface, frame_time: float):
    global randx, randy
    pygame.draw.rect(screen, WHITE, (0, GP.FLOOR_LEVEL, WIDTH, 1))
    for i in range(GP.PARTICLE):
        if randy[i] < GP.FLOOR_LEVEL:
            sandfall(YELLOW, randx[i], randy[i], GP.SAND_SIZE)
    for i in range(GP.PARTICLE):
        randy[i] +=1
    return



pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))


frame_by_frame = False
should_next_frame = False
play = True
clock = pygame.time.Clock()
while play:
    frame_time = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                play = False
            elif event.key == pygame.K_SPACE:
                frame_by_frame = not frame_by_frame
            elif event.key == pygame.K_RIGHT:
                should_next_frame = True

    if not frame_by_frame:
        draw_on_screen(screen, frame_time)
    else:
        if should_next_frame:
            draw_on_screen(screen, frame_time)
            should_next_frame = False

    pygame.display.flip()
