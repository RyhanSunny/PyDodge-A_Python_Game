# FIRST WE HAVE TO INSTALL PyGame USING CMD: pip install pygame
# AND THEN WE HAVE TO FOLLOW ME ON IG ;) (@notyour_sunshine_)
# NOW IMPORT PYGAME LIBRARY
import pygame
import sys  # IMPORT [2] : SYSTEM
import random  # IMPORT [3] : RANDOMIZE
from pygame.locals import *

# INITIATE PyGame
pygame.init()

# ~ ALL THE VARIABLES GO HERE:
WIDTH = 800
HEIGHT = 600

RED = 246, 114, 128
BLUE = 63, 130, 153
BG_COLOR = 244, 217, 187
FNT_COLOR = 189, 113, 68  # 250, 152, 90

player_size = 45
player_pos = [(WIDTH / 2) - player_size, HEIGHT - (2 * player_size+10)]
# player_speed =
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]  # for random int, use library see IMPORT 3
enemy_list = [enemy_pos]
enemy_speed = 7
# DECLARE CLOCK TO SET FRAME RATE
CLOCK = pygame.time.Clock()
# CREATE A SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False
score = 0
# pyFont = pygame.font.SysFont("Century Gothic", 35)
# pyFont2 = pygame.font.SysFont("Century Gothic", 15)

pyFont = pygame.font.Font("AdventPro-Light.ttf", 40)
pyFont2 = pygame.font.Font("AdventPro-Light.ttf", 20)


# ~ END OF VARIABLES


# ~ ALL OUR FUNCTIONS GO HERE:
# FUNCTION 1: DETECTING COLLISION
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (p_x <= e_x < (p_x + player_size)) or (e_x <= p_x < (e_x + enemy_size)):
        if (p_y <= e_y < (p_y + player_size)) or (e_y <= p_y < (e_y + enemy_size)):
            return True
    return False


# FUNCTION 2: MULTIPLYING ENEMIES
def enemies_fall(enemy_list):
    # adding a delay, so the enemies fall randomly
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:  # NUMBER OF ENEMIES AND DELAY BETWEEN THEM
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


# FUNCTION 3: MAKING NEW ENEMIES
def create_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


# FUNCTION 4: UPDATE ENEMY POSITIONS
def update_enemy_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] < HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score


# FUNCTION 5: COLLISION CHECK
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


# FUNCTION 6:
def set_level(score, enemy_speed):
    enemy_speed = (1/50)*score+3  # *USING LINEAR ALGEBRA TO FIND Y = MX + B
    #  WHERE Y IS enemy_speed X IS score, M IS SLOPE AND B IS INTERCEPT
    return enemy_speed


# ~ END OF FUNCTIONS

# OK SO WE DEVELOP OUR GAME UNDER A WHILE LOOP,
# SO BASICALLY -WHILE- GAME = NOT OVER -> KEEP GAME RUNNING

while not game_over:
    for event in pygame.event.get():
        # EVENT 1: QUIT EVENT (TO SMOOTHLY EXIT THE SCREEN)
        if event.type == pygame.QUIT:
            sys.exit()  # WE HAVE TO IMPORT THE SYSTEM LIBRARY FOR THIS. SEE: import [2] ABOVE

        # EVENT 2: MOVEMENT
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x, y]


    # CHANGE OUR BACKGROUND COLOR
    screen.fill(BG_COLOR)

    # FOR DRAWING SHAPES ON PyGame I FOLLOWED: https://www.pygame.org/docs/ref/draw.html

    # drawing player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    # MAKING THE PLAYER MOVE ON EVENT 2 ABOVE

    # UPDATING MULTIPLE ENEMY POSITION AND APPLYING THEIR COLLISION
    enemies_fall(enemy_list)
    score = update_enemy_pos(enemy_list, score)
    enemy_speed = set_level(score, enemy_speed)

    # score text
    text = "Score: {}".format(score)
    label = pyFont.render(text, 1, FNT_COLOR)
    screen.blit(label, (WIDTH - 188, HEIGHT - 58))

    # logo text
    text2 = "PyDodge"
    label2 = pyFont.render(text2, 1, FNT_COLOR)
    screen.blit(label2, (35, HEIGHT - 58))

    # signature text
    text2 = "github.com/RyhanSunny"
    label2 = pyFont2.render(text2, 1, FNT_COLOR)
    screen.blit(label2, (WIDTH / 2 - 95, HEIGHT - 42))

    # initiating collision check
    if collision_check(enemy_list, player_pos):
        game_over = True

    # A2: drawing new enemy
    # INITIALLY I USED: pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    # BUT LATER MOVED IT INTO A FUNCTION ABOVE, SEE FUNCTION 3
    create_enemies(enemy_list)

    # ~ignore~
    # A3: UPDATING ENEMY POSITION: CODE moved to FUNCTION 4
    # if 0 <= enemy_pos[1] < HEIGHT:
    #     enemy_pos[1] += enemy_speed
    # else:
    #     # enemy_list.pop(idx)
    #     enemy_pos[1] = 0
    #     enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

    # if detect_collision(player_pos, enemy_pos):
    #     game_over = True
    # ~ignore~

    # SETTING FRAME RATE
    CLOCK.tick(60)
    # WE NEED TO UPDATE OUR SCREEN EVERY ITERATION
    pygame.display.update()

# TODO: press and hold move, off screen boundary/ jumping to the other side

# ~ignore~ CIRCLE SHAPE THAT MIGHT BE USEFUL LATER: (needs anti-aliasing)
# pygame.draw.circle(screen, BLUE, enemy_pos, 25) ~ ignore ~
