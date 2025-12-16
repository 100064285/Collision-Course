# Imports
import pygame

import game_over
import variables as var


# Create Player

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Create Image
        self.image = pygame.Surface([50, 50])
        self.image.fill([50, 180, 235])
        # Create Bounding Box
        self.rect = self.image.get_rect()
        self.rect.y = var.SCREEN_HEIGHT / 1.5
        self.rect.x = var.SCREEN_WIDTH / 2

    def update(self):
        keys = pygame.key.get_pressed()
        if var.LIVES_2 < 1:
            self.rect.y = -1000
            self.image = pygame.Surface([0, 0])
        else:
            if not var.GAME_OVER:
                # Controls
                # Move Left
                if keys[pygame.K_a] and self.rect.left > 0:
                    if var.PLAYER_2_SPEED < 15 * var.GAME_SPEED:
                        var.PLAYER_2_SPEED += var.ACCELERATION * var.GAME_SPEED
                    self.rect.x -= var.PLAYER_2_SPEED
                # Move Right
                elif keys[pygame.K_d] and self.rect.right < var.SCREEN_WIDTH:
                    if var.PLAYER_2_SPEED < 15 * var.GAME_SPEED:
                        var.PLAYER_2_SPEED += var.ACCELERATION * var.GAME_SPEED
                    self.rect.x += var.PLAYER_2_SPEED
                # Reset Speed
                else:
                    if var.PLAYER_2_SPEED > 1:
                        var.PLAYER_2_SPEED = 1

        # Reset Button (keep on 'R' so spacebar can be used for shooting)
        if keys[pygame.K_r]:
            game_over.reset()
