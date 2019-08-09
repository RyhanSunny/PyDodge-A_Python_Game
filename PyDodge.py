# FIRST WE HAVE TO INSTALL PyGame ON CMD USING:
# pip install pygame AND FOLLOW SUNNY ON IG ;) (@notyour_sunshine_) ABSOLUTELY MANDATORY :P LOL JK
# IMPORT PYGAME LIBRARY
import pygame
import sys  # IMPORT [2]
import random  # IMPORT 3

# INITIALIZE PYGAME
pygame.init()

# VARIABLES USED BELOW
WIDTH = 800
HEIGHT = 600

RED = 246, 114, 128
BLUE = 63, 130, 153
BG_COLOR = 244, 217, 187

player_size = 50
player_pos = [(WIDTH / 2) - player_size, HEIGHT - (2 * player_size)]

enemy_size = 50
# we want enemy position to be random, so we use a library for that see IMPORT [3]
enemy_position = [random.randint(0, WIDTH - enemy_size), 0]

# CREATE A SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# OK NEXT WE DEVELOP OUR GAME LOOP SO BASICALLY > KEEP GAME RUNNING -WHILE- GAME NOT OVER
# NOTE PYGAME IS AN EVENT BASED LIBRARY
# SO WE'RE GONNA HAVE A FOR LOOP INSIDE THE WHILE LOOP THAT WILL TRACK ALL OF OUR EVENTS

game_over = False

while not game_over:
    for event in pygame.event.get():
        # WE WILL PUT ALL OUR EVENTS INSIDE THIS FOR LOOP

        # EVENT 1: QUIT EVENT (TO SMOOTHLY EXIT THE SCREEN)
        if event.type == pygame.QUIT:
            sys.exit()  # WE HAVE TO IMPORT THE SYSTEM LIBRARY FOR THIS. SEE: import [2] ABOVE
        # BEFORE EVENT 2 WE'LL DRAW A SHAPE ON THE SCREEN. SEE COMMENT A1 BELOW

        # EVENT 2: MOVEMENT
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x, y]
        # AFTER EVENT 2 WE'RE GONNA DECLARE ENEMY VARIABLES AND DRAW ENEMY SHAPE. SEE COMMENT A2 BELOW
    # CHANGE OUR BACKGROUND COLOR
    screen.fill(BG_COLOR)

    # A1: OK NOW THAT WE HAVE OUR BASIC SCREEN WE WILL START DRAWING SHAPES AND EVENTUALLY MANIPULATE THEM
    # FOR DRAWING SHAPES ON PYGAME FOLLOW: https://www.pygame.org/docs/ref/draw.html
    # drawing player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # A2: drawing enemy
    # pygame.draw.circle(screen, BLUE, enemy_position, 25)
    pygame.draw.rect(screen, BLUE, (enemy_position[0], enemy_position[1], enemy_size, enemy_size))

    # WE NEED TO UPDATE OUR SCREEN EVERY ITERATION
    pygame.display.update()


## TODO: MAKE ENEMY FALL, CREATE MORE ENEMIES