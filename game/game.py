import pygame
import sys


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

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

    def update(self):
        """Update the game state."""
        pass

    def draw(self):
        """Render the game elements."""
        self.screen.fill((138, 138, 138))

        pygame.display.update()
