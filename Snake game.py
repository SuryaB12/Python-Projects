import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    game_screen.blit(value, [0, 0])

# Snake properties
snake_x, snake_y = width / 2, height / 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]
snake_block = 10

# Food properties
food_x = random.randrange(0, width // 10) * 10
food_y = random.randrange(0, height // 10) * 10

# Clock for controlling speed
clock = pygame.time.Clock()

# Display the snake
def display_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(game_screen, green, [segment[0], segment[1], snake_block, snake_block])

# Main game loop
def game_loop():
    global snake_x, snake_y, change_x, change_y, food_x, food_y

    game_over = False
    game_close = False

    while not game_over:
        while game_close:
            game_screen.fill(blue)
            your_score(len(snake_body) - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        # Event handling for key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -snake_block
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = snake_block
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -snake_block
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = snake_block

        # Update snake position
        snake_x = (snake_x + change_x) % width
        snake_y = (snake_y + change_y) % height

        # Check for collisions with food
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randrange(0, width // 10) * 10
            food_y = random.randrange(0, height // 10) * 10
        else:
            snake_body.pop(0)

        # Add new snake segment
        snake_body.append((snake_x, snake_y))

        # Check for collision with self
        if len(snake_body) > 1 and (snake_x, snake_y) in snake_body[:-1]:
            game_close = True

        # Draw everything
        game_screen.fill(black)
        pygame.draw.rect(game_screen, red, [food_x, food_y, snake_block, snake_block])
        display_snake(snake_body)
        your_score(len(snake_body) - 1)
        pygame.display.update()

        # Control the speed of the game
        clock.tick(12)

    pygame.quit()

# Run the game
game_loop()