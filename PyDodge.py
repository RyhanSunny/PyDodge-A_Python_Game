# FIRST WE HAVE TO INSTALL PyGame USING CMD: pip install pygame
# AND THEN WE HAVE TO FOLLOW ME ON IG ;) (@notyour_sunshine_)
# NOW IMPORT PYGAME LIBRARY
import pygame
import sys  # IMPORT [2] : SYSTEM
import random  # IMPORT [3] : RANDOMIZE

# INITIATE PyGame
pygame.init()

# ~ ALL THE VARIABLES GO HERE:
WIDTH = 800
HEIGHT = 600

RED = 246, 114, 128
BLUE = 63, 130, 153
BG_COLOR = 244, 217, 187

player_size = 50
player_pos = [(WIDTH / 2) - player_size, HEIGHT - (2 * player_size)]
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]  # for random int, use library see IMPORT 3
enemy_list = [enemy_pos]
enemy_speed = 4
# DECLARE CLOCK TO SET FRAME RATE
CLOCK = pygame.time.Clock()
# CREATE A SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False


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
    if len(enemy_list) < 10:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


# FUNCTION 3: MAKING NEW ENEMIES
def create_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


# FUNCTION 4: UPDATE ENEMY POSITIONS
def update_enemy_pos(enemy_list):
    for idx, enemy_pos in enumerate(enemy_list):
        if 0 <= enemy_pos[1] < HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)


# FUNCTION 5: COLLISION CHECK
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


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
    update_enemy_pos(enemy_list)
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
    CLOCK.tick(120)
    # WE NEED TO UPDATE OUR SCREEN EVERY ITERATION
    pygame.display.update()

# TODO: CREATE COLLISION METRICS, CREATE MORE ENEMIES
# ~ignore~ CIRCLE SHAPE THAT MIGHT BE USEFUL LATER:
# pygame.draw.circle(screen, BLUE, enemy_pos, 25) ~ ignore ~
