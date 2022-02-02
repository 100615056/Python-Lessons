# Source: https://www.edureka.co/blog/snake-game-with-pygame/

import pygame
import time
import random

pygame.init()

# Defining colours for sprites and backgrounds
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
background = (51, 153, 255)

# Defining the width and height of the game display
width = 600
height = 400
# Setting up display
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
# Font
font = pygame.font.SysFont(None, 25)

# Snake
snake_block = 10
snake_speed = 15


# Print score
def Your_score(score):
    value = font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Grow Snake
def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])


# Display game over message
def message(msg, color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])


# Game Loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake
    x = width / 2
    y = height / 2
    snake_list = []
    length_of_snake = 1

    x1_change = 0
    y1_change = 0

    # Food Coordinates
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", green)
            Your_score(length_of_snake - 1)
            pygame.display.update()
            # Keyboard Events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # Player Movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # Game Boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x1_change
        y += y1_change
        dis.fill(background)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        # Create snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # Check if snake runs into itself
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)

        pygame.display.update()
        # Check if snake and food are at the same spot
        if x == foodx and y == foody:
            foodx = round(random.randrange(
                0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
