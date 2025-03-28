import pygame
import sys

from game.player import Player
from game.util import load_images
from game.tilemap import Tilemap


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.player = Player(pygame.math.Vector2(50, 50))

        self.assets = {
            'grass': load_images('tiles/grass'),
        }

        self.tilemap = Tilemap(self, tile_size=16)
        self.tilemap.load('map.json')

    def run(self):
        """Main game loop."""
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        return False

    def handle_events(self):
        """Handle user input and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self):
        """Update the game state."""
        self.player.udpate_gravitiy()

    def draw(self):
        """Render the game elements."""
        self.screen.fill((138, 138, 138))

        self.tilemap.render(self.screen)

        self.player.draw_player(self.screen)

        pygame.display.update()
