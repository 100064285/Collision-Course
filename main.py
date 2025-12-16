# Imports
import pygame
import random
import game_over as over
import multiplayer
import variables as var
from button import Button, OnePlayer, TwoPlayer

# pygame initial setup
pygame.init()
clock = pygame.time.Clock()
screen = var.screen
title = var.title_screen
game_state = "title"
# game setup
all_sprites = var.all_sprites
global player
player = var.player
extra_player = var.extra_player
all_sprites.add(extra_player)

all_sprites.add(var.all_enemies)
all_sprites.add(var.player)

random_color = [random.randint(0, 100), 0, random.randint(0, 255)]
# While Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        action = var.start_button.handle_event(event)
        action = var.start2_button.handle_event(event)
    # fill the screen with a color to wipe away anything from last frame
    if game_state == "running":
        if not var.MULTIPLAYER:
            all_sprites.remove(extra_player)
            extra_player.rect.y = 4000
        screen.fill(random_color)

        # Bottom of Screen
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        pygame.draw.circle(var.screen, [100, 100, 100], [random.randint(0, var.SCREEN_WIDTH),
                                                         random.randint(round(var.SCREEN_HEIGHT * 2 / 3),
                                                                        var.SCREEN_HEIGHT)], 5)
        # Reset Enemy Off-Screen
        for i in var.all_enemies:
            if i.rect.y > var.SCREEN_HEIGHT:
                if var.LIVES >= 1:
                    var.SCORE += 1

                if var.LIVES_2 >= 1:
                    var.SCORE_2 += 1

                if var.FIVE_COUNTER >= 5:
                    var.FIVE_COUNTER = 1
                    var.GAME_SPEED += 1 / len(var.all_enemies)
                else:
                    var.FIVE_COUNTER += 1
                i.reset()
            # Check for Collision
            i.check_collision()
            # Check for laser hits
            hits = pygame.sprite.spritecollide(i, var.lasers, True)
            if hits:
                i.take_hits(len(hits))

        # Game Over
        if var.MULTIPLAYER:
            if (var.LIVES < 1) & (var.LIVES_2 < 1):
                over.run()
        if not var.MULTIPLAYER:
            if var.LIVES < 1:
                over.run()

        # print("Counter" + f"{var.FIVE_COUNTER}")
        print("Game Speed" + f"{var.GAME_SPEED}")
        print("Player Speed" + f"{var.PLAYER_SPEED}")

        # Draw Score
        font = pygame.font.Font(None, 36)
        score = font.render(f"Score: {var.SCORE}", 1, (10, 10, 10), (0, 0, 255))
        scorepos = score.get_rect()
        scorepos.centerx = screen.get_rect().width * 2 / 5
        # Draw Lives
        livesText = font.render(f"Lives: {var.LIVES}", 1, (10, 10, 10), (255, 0, 0))
        livesTextPos = livesText.get_rect()
        livesTextPos.centerx = screen.get_rect().width * 1 / 5

        if var.MULTIPLAYER:
            if not var.GAME_OVER:
                multiplayer.extra_ui()
                extra_player.update()
                score = font.render(f"Score 1: {var.SCORE}", 1, (10, 10, 10), (50, 50, 255))
                livesText = font.render(f"Lives 1: {var.LIVES}", 1, (10, 10, 10), (255, 50, 50))

        # Draw Text
        if not var.GAME_OVER:
            screen.blit(livesText, livesTextPos)
            screen.blit(score, scorepos)

        # Draw

        if not var.GAME_OVER:
            all_sprites.draw(screen)
            var.all_enemies.update()
            player.update()
            var.lasers.update()
    elif game_state == "title":
        title_font = pygame.font.Font(None, 48)
        title.fill([50, 50, 200])
        title_text = title_font.render("Collision Course", True, (0, 0, 0))
        title.blit(title_text, (title.get_rect().centerx, var.SCREEN_HEIGHT * 1 / 5))
        screen.blit(title, screen.get_rect())
        var.start_button.draw(screen)
        var.start2_button.draw(screen)
        print(var.MULTIPLAYER)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
