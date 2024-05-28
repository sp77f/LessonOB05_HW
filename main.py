import pygame
import time
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
green_light = (0, 200, 0)

# Размеры экрана
display_width = 800
display_height = 600

# Размер блока змейки
block_size = 20

clock = pygame.time.Clock()

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Змейка')

font = pygame.font.SysFont(None, 25)

def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])
        #print(x)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [display_width/4, display_height/2])

def gameLoop():
    game_exit = False
    game_over = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    randAppleX = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0

    while not game_exit:
        while game_over == True:
            game_display.fill(white)
            message_to_screen("Игра окончена. Нажмите C для игры заново или Q для выхода", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
            game_display.fill(red)
            pygame.display.update()
            time.sleep(0.2)
            game_display.fill(white)
            pygame.display.update()

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)
        pygame.draw.rect(game_display, red, [randAppleX, randAppleY, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
                game_display.fill(red)
                pygame.display.update()
                time.sleep(0.2)
                game_display.fill(white)
                pygame.display.update()

        snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0
            snake_length += 1
            print("Еда съедена")
            game_display.fill(green_light)
            pygame.display.update()
            time.sleep(0.2)
            game_display.fill(white)
            pygame.display.update()

        clock.tick(10)

    pygame.quit()
    quit()

gameLoop()