import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up snake
snake_size = 20
snake_speed = 15
snake = [(width // 2, height // 2)]
snake_direction = (1, 0)  # Initial direction: right

# Set up initial food position
food = (random.randrange(1, (width // snake_size)) * snake_size,
        random.randrange(1, (height // snake_size)) * snake_size)

# Set up clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
                
        
        

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * snake_size
    y += snake_direction[1] * snake_size
    snake.insert(0, (x, y))

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randrange(1, (width // snake_size)) * snake_size,
                random.randrange(1, (height // snake_size)) * snake_size)
    else:
        snake.pop()
        

    # Check for collisions with itself
    if len(snake) > 1 and snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()

    # Fill the screen with a background color
    screen.fill(black)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, red, (food[0], food[1], snake_size, snake_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(snake_speed)
