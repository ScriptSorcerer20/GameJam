import pygame
from game.game import Game


def main():

    running = True
    playing = True

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    width, height = pygame.display.get_window_size()
    clock = pygame.time.Clock()

    pygame.display.set_caption("Inner Echo")
    #icon_img = pygame.image.load('assets/icon.png')
    #pygame.display.set_icon(icon_img)

    #start_menu = StartMenu(screen, clock)
    #game_menu = GameMenu(screen, clock)

    game = Game(screen, clock)

    while running:

        #playing = start_menu.run()

        while playing:
            playing = game.run()

            #playing = game_menu.run()

if __name__ == "__main__":
    main()