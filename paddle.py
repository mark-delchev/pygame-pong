import pygame

# Define the Paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 80
        self.speed = 5

    def update(self, direction, screen_height):
        self.y += direction * self.speed
        # Boundary checks to prevent the paddle from going off the screen
        if self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))