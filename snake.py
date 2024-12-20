import pygame

class Snake():
    def __init__(self, direction, position, color = 'green'):
        self.direction = direction
        self.position = position
        self.color = color
        
    # Move the snake by one cell in the current direction
    def move(self, cell_size=15):
        new_head = self.position[0] + self.direction * cell_size
        self.position.insert(0, new_head)

    def move_left(self):
        self.direction = pygame.Vector2(-1, 0)

    def move_right(self):
        self.direction = pygame.Vector2(1, 0)

    def move_up(self):
        self.direction = pygame.Vector2(0, -1)

    def move_down(self):
        self.direction = pygame.Vector2(0, 1)
        
    def check_collision(self, width, height):
        head = self.position[0]

        if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height:
            return True
        
        # self collision
        if head in self.position[1:]:
            return True
        
        return False
