import pygame
import sys
from paddle import *
from ball import *



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
