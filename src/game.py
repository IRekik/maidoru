import pygame
from player import Player


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(width, height)

    def handle_input(self, keys):
        self.player.handle_input(keys)

    def update(self):
        self.player.update()

    def draw(self, screen):
        # Draw the background image
        background = pygame.image.load("../images/background.jpg")
        screen.blit(background, (0, 0))

        # Draw the player character
        self.player.draw(screen)
