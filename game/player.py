import pygame

class Player:
    def __init__(self, position: pygame.math.Vector2):
        self.position = position
        self.rect = pygame.Rect(position.x, position.y, 32, 64)

    def jump(self):
        self.position.y -= 30
        self.rect.y = self.position.y

    def draw_player(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def udpate_gravitiy(self):
        self.position.y += 5
        self.rect.y = self.position.y
