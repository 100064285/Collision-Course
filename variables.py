# Imports
import pygame
import player as player
import enemy1 as e1
import extra_player as player_2
from button import Button, OnePlayer, TwoPlayer

# Variables

# Groups
all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

# Game
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 920

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
title_screen = screen.__copy__()

PLAYER_SPEED = 1
PLAYER_2_SPEED = 1
GAME_SPEED = 1
L1_ENEMY_SPEED = 10
SCORE = 0
LIVES = 3
GAME_OVER = False
MULTIPLAYER = True
SCORE_2 = 0
LIVES_2 = 3

ACCELERATION = 0.7
# Sprites
player = player.Player()
extra_player = player_2.Player()
enemy1 = e1.Enemy()
enemy2 = e1.Enemy()
# enemy3 = e1.Enemy()enemy4 = e1.Enemy()

all_enemies.add(enemy1)
all_enemies.add(enemy2)
# all_enemies.add(enemy3)all_enemies.add(enemy4)

# Buttons
start_button = Button(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 2 / 3, 100, 100, "One Player",
                      OnePlayer)
start2_button = Button(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 2 / 3 + 200, 100, 100, "Two Player",
                       TwoPlayer)

# Counters
FIVE_COUNTER = 0
