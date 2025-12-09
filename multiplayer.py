import pygame
import variables as vars


def extra_ui():
    # Draw Score
    font = pygame.font.Font(None, 36)
    score = font.render(f"Score2 : {vars.SCORE_2}", 1, (10, 10, 10), (100, 255, 255))
    scorepos = score.get_rect()
    scorepos.centerx = vars.screen.get_rect().width * 4 / 5
    vars.screen.blit(score, scorepos)
    # Draw Lives
    livesText = font.render(f"Lives 2: {vars.LIVES_2}", 1, (10, 10, 10), (255, 255, 0))
    livesTextPos = livesText.get_rect()
    livesTextPos.centerx = vars.screen.get_rect().width * 3 / 5
    vars.screen.blit(livesText, livesTextPos)
