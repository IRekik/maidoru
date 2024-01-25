import pygame
import sys

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maidoru")

x_position = 0
y_position = 0

def move_right():
    global x_position
    if x_position < 700:
        x_position += 1

def move_left():
    global x_position
    if x_position > 0:
        x_position -= 1

def move_up():
    global y_position
    if y_position > 0:
        y_position -= 1

def move_down():
    global y_position
    if y_position < 500:
        y_position += 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_left()
    if keys[pygame.K_RIGHT]:
        move_right()
    if keys[pygame.K_UP]:
        move_up()
    if keys[pygame.K_DOWN]:
        move_down()

    # Draw a red rectangle on the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (x_position, y_position, 100, 100))

    pygame.display.flip()