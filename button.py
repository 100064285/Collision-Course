import pygame

import variables as var


class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.is_hovered = False
        self.color = (50, 50, 180)
        self.hover_color = (180, 50, 180)

    def draw(self, screen):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            if self.action:
                self.action()  # Execute the associated action


def OnePlayer():
    var.MULTIPLAYER = False
    import main
    main.game_state = "running"


def TwoPlayer():
    var.MULTIPLAYER = True
    import main
    main.game_state = "running"
