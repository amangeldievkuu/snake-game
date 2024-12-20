import random
import pygame

class Apple():
    def __init__(self, width, height, cell_size = 15, color = 'red'):
        self.color = color
        self.x = random.randint(0, (width // cell_size) - 1) * cell_size
        self.y = random.randint(0, (height // cell_size) - 1) * cell_size
        self.position = pygame.Vector2(self.x, self.y)