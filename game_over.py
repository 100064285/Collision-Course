import pygame
import variables as vars


def run():
    # Set Game Over
    vars.GAME_OVER = True
    # Set Fonts
    bigFont = pygame.font.Font(None, 108)
    font = pygame.font.Font(None, 36)
    # Game Over Text
    text = bigFont.render("Game Over!", 1, (10, 10, 10), (0, 0, 255))
    textpos = text.get_rect()
    textpos.centerx = vars.screen.get_rect().centerx
    textpos.centery = vars.screen.get_rect().centery * 1/5
    # Score Text
    score = font.render(f"Score: {vars.SCORE}", 1, (10, 10, 10), (0, 0, 255))
    scorepos = score.get_rect()
    scorepos.centery = vars.screen.get_rect().centery * 2/5
    # Add to Screen

    # Reset

    keys = pygame.key.get_pressed()
    if vars.GAME_OVER:
        if keys[pygame.K_SPACE]:
            vars.GAME_OVER = False
            vars.LIVES
    # Multiplayer
    if vars.MULTIPLAYER:
        score = font.render(f"Player 1 Score: {vars.SCORE}", 1, (10, 10, 10), (0, 0, 255))
        scorepos.centerx = vars.screen.get_rect().centerx
        score2 = font.render(f"Player 2 Score: {vars.SCORE_2}", 1, (10, 10, 10), (0, 0, 255))
        score2pos = score2.get_rect()
        score2pos.centerx = vars.screen.get_rect().centerx
        score2pos.centery = vars.screen.get_rect().centery * 3/5
        vars.screen.blit(score2, score2pos)

    vars.screen.blit(text, textpos)
    vars.screen.blit(score, scorepos)


def reset():
    vars.GAME_OVER = False
    vars.SCORE = 0
    vars.SCORE_2 = 0
    vars.LIVES = 3
    vars.LIVES_2 = 3
    vars.GAME_SPEED = 1
    vars.enemy1.reset()
