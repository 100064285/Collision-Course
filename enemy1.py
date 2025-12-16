import random
import pygame
import variables as vars


# Create Enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # Choose a random meteor sprite (brown or grey, big size)
        meteor_choices = [
            "assets/meteors/meteorBrown_big1.png",
            "assets/meteors/meteorBrown_big2.png",
            "assets/meteors/meteorBrown_big3.png",
            "assets/meteors/meteorBrown_big4.png",
            "assets/meteors/meteorGrey_big1.png",
            "assets/meteors/meteorGrey_big2.png",
            "assets/meteors/meteorGrey_big3.png",
            "assets/meteors/meteorGrey_big4.png",
        ]
        try:
            image_path = random.choice(meteor_choices)
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error:
            # Fallback to a simple colored square if images are missing
            self.image = pygame.Surface([120, 120])
            self.image.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

        # Create Bounding Box that matches sprite size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, max(0, vars.SCREEN_WIDTH - self.rect.width))
        # Health: takes 2 laser hits to destroy
        self.health = 2

        self.angle = 0
        self.rotation_speed = random.randint(1, 10)
        # Add to Group
        vars.all_enemies.add(self)

    def update(self):
        # Move Down Screen
        if not vars.GAME_OVER:
            self.rect.y += vars.L1_ENEMY_SPEED * vars.GAME_SPEED

    def reset(self):
        # Reset to Top of Screen with a (possibly) new random meteor sprite
        meteor_choices = [
            "assets/meteors/meteorBrown_big1.png",
            "assets/meteors/meteorBrown_big2.png",
            "assets/meteors/meteorBrown_big3.png",
            "assets/meteors/meteorBrown_big4.png",
            "assets/meteors/meteorGrey_big1.png",
            "assets/meteors/meteorGrey_big2.png",
            "assets/meteors/meteorGrey_big3.png",
            "assets/meteors/meteorGrey_big4.png",
        ]
        try:
            image_path = random.choice(meteor_choices)
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error:
            self.image = pygame.Surface([120, 120])
            self.image.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, max(0, vars.SCREEN_WIDTH - self.rect.width))
        self.health = 2

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
