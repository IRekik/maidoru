import pygame
from map_collision import generate_collision_map

class Player:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.x_position = 0
        self.y_position = 12
        self.width = 10
        self.height = 10
        self.obstacles = generate_collision_map("txt_files/collision_pixels.txt")

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

    def doesItCollide(self, next_x_position, next_y_position):
        if (next_x_position, next_y_position) in self.obstacles:
            return True
        return False

    def move_left(self):
        if self.x_position > 0 and not self.doesItCollide(self.x_position - 1, self.y_position):
            self.x_position -= 1

    def move_right(self):
        if self.x_position < (self.map_width - self.width) and not self.doesItCollide(self.x_position + self.width - 1, self.y_position):
            self.x_position += 1

    def move_up(self):
        if self.y_position > 0 and not self.doesItCollide(self.x_position, self.y_position - 1):
            self.y_position -= 1

    def move_down(self):
        if self.y_position < (self.map_height - self.height) and not self.doesItCollide(self.x_position, self.y_position + self.width - 1):
            self.y_position += 1

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x_position, self.y_position, self.width, self.height))