import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Define the Paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 80
        self.speed = 5

    def update(self, direction):
        self.y += direction * self.speed
        # Boundary checks to prevent the paddle from going off the screen
        if self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def render(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))