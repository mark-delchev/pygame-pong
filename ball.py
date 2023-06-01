import pygame
from paddle import *

class Ball:
    def __init__(self, x, y, screen_height):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed_x = 3
        self.speed_y = 3
        self.screen_height = screen_height

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with the top or bottom of the screen
        if self.y - self.radius < 0 or self.y + self.radius > self.screen_height:
            self.speed_y *= -1  # Reverse the y-speed to bounce off the top or bottom

    def check_collision(self, paddle):
         if (
            self.x + self.radius >= paddle.x
            and self.x - self.radius <= paddle.x + paddle.width
            and self.y + self.radius >= paddle.y
            and self.y - self.radius <= paddle.y + paddle.height
        ):
            # Adjust the ball's position to the edge of the paddle
            if self.x < paddle.x:
                self.x = paddle.x - self.radius
            else:
                self.x = paddle.x + paddle.width + self.radius

            # Reverse the x-speed when colliding with a paddle
            self.speed_x *= -1

    def reset(self, screen_width):
        self.x = screen_width // 2
        self.y = self.screen_height // 2
        self.speed_x *= -1  # Reverse the x-speed for a new direction

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
