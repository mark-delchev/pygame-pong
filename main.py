import pygame
import sys

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

# Define the Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with the top or bottom of the screen
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
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

    def reset(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x *= -1  # Reverse the x-speed for a new direction

    def render(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

# Create the paddles and the ball
paddle_a = Paddle(20, screen_height // 2 - 30)
paddle_b = Paddle(screen_width - 30, screen_height // 2 - 30)
ball = Ball(screen_width // 2, screen_height // 2)

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game state
        # Inside the game loop, after handling the events
        keys = pygame.key.get_pressed()

        # Player A controls
        if keys[pygame.K_w]:
            paddle_a.update(-1)  # Move paddle A up
        elif keys[pygame.K_s]:
            paddle_a.update(1)  # Move paddle A down

        # Player B controls
        if keys[pygame.K_UP]:
            paddle_b.update(-1)  # Move paddle B up
        elif keys[pygame.K_DOWN]:
            paddle_b.update(1)  # Move paddle B down



        # Render graphics
        screen.fill((0, 0, 0))  # Clear the screen with a black color
        paddle_a.render()
        paddle_b.render()
        ball.update()
        
        ball.render()
        ball.check_collision(paddle_a)
        ball.check_collision(paddle_b)
        if ball.x - ball.radius > screen_width or ball.x + ball.radius < 0:
            ball.reset()
        # Update the game display
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS

# Run the game
def run_game():
    game_loop()
    pygame.quit()
    sys.exit()

# Entry point of the program
if __name__ == "__main__":
    run_game()
