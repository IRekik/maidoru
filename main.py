import pygame
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

pixel = 0
goingRight = True
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw a red rectangle on the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (pixel, 50, 100, 100))

    pygame.display.flip()
    if pixel == 0:
        goingRight = True
    elif pixel == 750:
        goingRight = False

    if goingRight:
        pixel += 1
    else:
        pixel -= 1