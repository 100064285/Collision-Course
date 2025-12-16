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
        # Shooting
        self.last_shot_time = 0
        self.shot_cooldown = 250  # milliseconds

    def update(self):
        keys = pygame.key.get_pressed()
        if var.LIVES < 1:
            self.rect.y = -1000
            self.image = pygame.Surface([0, 0])

        if not var.GAME_OVER:
            current_time = pygame.time.get_ticks()

            # Shooting (spacebar) with cooldown
            if keys[pygame.K_SPACE] and current_time - self.last_shot_time >= self.shot_cooldown:
                laser = Laser(self.rect.centerx, self.rect.top)
                var.all_sprites.add(laser)
                var.lasers.add(laser)
                self.last_shot_time = current_time

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
        if keys[pygame.K_r]:
            game_over.reset()


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Laser, self).__init__()
        # Laser sprite (fallback to a simple rectangle if the image is missing)
        try:
            self.image = pygame.image.load("assets/lasers/laserBlue07.png").convert_alpha()
        except pygame.error:
            self.image = pygame.Surface([6, 20])
            self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        # Move up the screen
        self.rect.y -= 15
        # Remove if it goes off-screen
        if self.rect.bottom < 0:
            self.kill()
