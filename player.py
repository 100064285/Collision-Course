# Imports
import pygame

import game_over
import variables as var


# Create Player

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Create Image (try to load a spaceship sprite, fall back to a square)
        try:
            self.image = pygame.image.load("assets/ships/playerShip1_blue.png").convert_alpha()
        except pygame.error:
            self.image = pygame.Surface([50, 50])
            self.image.fill([76, 52, 235])
        # Create Bounding Box
        self.rect = self.image.get_rect()
        self.rect.y = var.SCREEN_HEIGHT / 1.5
        self.rect.x = var.SCREEN_WIDTH / 2

    def update(self):
        keys = pygame.key.get_pressed()
        if var.LIVES < 1:
            self.rect.y = -1000
            self.image = pygame.Surface([0, 0])

        if not var.GAME_OVER:
            # Controls
            # Move Left
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                if var.PLAYER_SPEED < 15 * var.GAME_SPEED:
                    var.PLAYER_SPEED += var.ACCELERATION * var.GAME_SPEED
                self.rect.x -= var.PLAYER_SPEED
            # Move Right
            elif keys[pygame.K_RIGHT] and self.rect.right < var.SCREEN_WIDTH:
                if var.PLAYER_SPEED < 15 * var.GAME_SPEED:
                    var.PLAYER_SPEED += var.ACCELERATION * var.GAME_SPEED
                self.rect.x += var.PLAYER_SPEED
            # Reset Speed
            else:
                if var.PLAYER_SPEED > 1:
                    var.PLAYER_SPEED = 1

        # Reset Button
        if keys[pygame.K_r] | keys[pygame.K_SPACE]:
            game_over.reset()
