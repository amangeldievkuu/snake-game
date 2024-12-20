import pygame
import sys
import random
from snake import Snake
from apple import Apple

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.cell_size = 15
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        # Clock and timing
        self.clock = pygame.time.Clock()
        self.fps = 5

        # Initial Snake Setup
        start_x = self.width // 2 // self.cell_size * self.cell_size
        start_y = self.height // 2 // self.cell_size * self.cell_size

        self.snake = Snake(direction=pygame.Vector2(1, 0), position=[
            pygame.Vector2(start_x, start_y),
            pygame.Vector2(start_x - self.cell_size, start_y),
            pygame.Vector2(start_x - 2 * self.cell_size, start_y)
        ], color='green')

        # Initial Apple
        self.apple = self.generate_apple()

        # Game state
        self.running = True
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

    def generate_apple(self):
        while True:
            apple_pos = Apple(self.width, self.height, self.cell_size, color='red')
            if apple_pos not in self.snake.position:
                return apple_pos

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps) 

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                # Change direction
                if event.key == pygame.K_LEFT and self.snake.direction  != pygame.Vector2(1, 0):
                    self.snake.move_left()
                elif event.key == pygame.K_RIGHT and self.snake.direction  != pygame.Vector2(-1, 0):
                    self.snake.move_right()
                elif event.key == pygame.K_UP and self.snake.direction  != pygame.Vector2(0, 1):
                    self.snake.move_up()
                elif event.key == pygame.K_DOWN and self.snake.direction  != pygame.Vector2(0, -1):
                    self.snake.move_down()

    def update(self):
        self.snake.move()
    
        if self.snake.check_collision(width=self.width, height=self.height):
            self.running = False
            return

        # Check if apple is eaten
        if self.snake.position[0] == self.apple.position:
            self.score += 1
            self.apple = self.generate_apple()
        else:
            self.snake.position.pop()


    def draw(self):
        self.display.fill("white")

        # Draw Snake
        for i, pos in enumerate(self.snake.position):
            color = 'green' if i == 0 else 'darkgreen'
            pygame.draw.rect(self.display, color, (pos.x, pos.y, self.cell_size, self.cell_size))

        # Draw Apple
        pygame.draw.rect(self.display, 'red', (self.apple.x, self.apple.y, self.cell_size, self.cell_size))

        # Draw Score
        score_surface = self.font.render(f"Score: {self.score}", True, (0, 0, 0), (123,35,255))
        self.display.blit(score_surface, (10, 10))
        pygame.display.flip()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
