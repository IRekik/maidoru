import sys
import pygame
from game import Game

def main():
    pygame.init()

    # Set up the display
    width, height = 512, 512
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maidoru")

    game = Game(width, height)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Keyboard input
        keys = pygame.key.get_pressed()
        game.handle_input(keys)

        # Update and draw the game
        game.update()
        game.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
