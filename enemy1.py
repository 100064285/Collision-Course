# Imports
import random
import pygame
import variables as vars


# Create Enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # Create Image
        self.image = pygame.Surface([120, 120])
        self.image.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        # Create Bounding Box
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, vars.SCREEN_WIDTH)

        self.angle = 0
        self.rotation_speed = random.randint(1, 10)
        # Add to Group
        vars.all_enemies.add(self)

    def update(self):
        # Move Down Screen
        if not vars.GAME_OVER:
            self.rect.y += vars.L1_ENEMY_SPEED * vars.GAME_SPEED

    def reset(self):
        # Reset to Top of Screen
        self.rect.y = 0
        self.rect.x = random.randint(0, vars.SCREEN_WIDTH)

    def check_collision(self):
        # Check for Player Collision
        if self.rect.colliderect(vars.player):
            self.reset()
            if vars.SCORE != 0:
                vars.SCORE -= 1
            vars.LIVES -= 1

        # Check for Player 2 Collision
        if self.rect.colliderect(vars.extra_player):
            self.reset()
            if vars.SCORE_2 != 0:
                vars.SCORE_2 -= 1
            vars.LIVES_2 -= 1
