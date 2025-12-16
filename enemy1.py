import random
import pygame
import variables as vars


# Create Enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        # Sprite and health depend on meteor type (brown vs grey)
        self._set_sprite_and_health()

        # Create Bounding Box that matches sprite size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, max(0, vars.SCREEN_WIDTH - self.rect.width))

        self.angle = 0
        self.rotation_speed = random.randint(1, 10)
        # Add to Group
        vars.all_enemies.add(self)

    def _set_sprite_and_health(self):
        """Pick a random meteor sprite and set health based on color.

        - Brown meteors: 1 hit
        - Grey meteors: 3 hits (and will tint darker on each hit)
        """
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
            self.is_grey = "Grey" in image_path
        except pygame.error:
            # Fallback to a simple colored square if images are missing
            self.image = pygame.Surface([120, 120])
            self.image.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            self.is_grey = False

        self.max_health = 3 if self.is_grey else 1
        self.health = self.max_health

    def update(self):
        # Move Down Screen
        if not vars.GAME_OVER:
            self.rect.y += vars.L1_ENEMY_SPEED * vars.GAME_SPEED

    def reset(self):
        # Reset to Top of Screen with a (possibly) new random meteor sprite
        self._set_sprite_and_health()
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(0, max(0, vars.SCREEN_WIDTH - self.rect.width))

    def take_hits(self, num_hits: int):
        """Apply one or more laser hits to this meteor.

        Grey meteors darken slightly on each hit so the player can see damage.
        """
        for _ in range(num_hits):
            if self.is_grey:
                # Darken the meteor slightly to show damage
                darken_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
                darken_surface.fill((40, 40, 40))  # subtract some RGB
                self.image.blit(darken_surface, (0, 0), special_flags=pygame.BLEND_RGB_SUB)

            self.health -= 1
            if self.health <= 0:
                self.reset()
                break

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
