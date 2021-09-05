import pygame
import time
import random
import sys

pygame.init()

# Screen Initialize
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 680
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CAPTION = pygame.display.set_caption("Noob Typing Test")
clock = pygame.time.Clock()

# Basic RGB
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

# Checking input_rect enable or disable
color_active = pygame.Color('cyan')
color_passive = pygame.Color('darkgray')
color = color_passive

# User Input Config
input_rect = pygame.Rect(50, 450, 1200, 45)
reset_rect = pygame.Rect(600, 600, 185, 40)
restart_rect = pygame.Rect(600, 600, 185, 40)
base_font = pygame.font.Font(None, 35)
title_font = pygame.font.Font(None, 91)
over_font = pygame.font.Font(None, 50)
reset_font = pygame.font.Font(None, 35)
user_text = ''
word_color = white

# Paragraph
paragraph = open("type.txt", "r").readlines()
words = random.choice(paragraph)[:-1]
paragraph1 = open("type.txt", "r").readlines()
reset_words = random.choice(paragraph1)[:-1]


def game_over_screen():
    global seconds
    WINDOW.fill((0, 0, 0))
    inGameTitle = title_font.render("Noob Typing Test", True, cyan)
    WINDOW.blit(inGameTitle, (400, 50))
    game_over_text = over_font.render("You Finished", True, red)
    WINDOW.blit(game_over_text, (550, 200))
    timer = base_font.render("Finish Time: " + str(seconds - 1), True, white)
    WINDOW.blit(timer, (540, 300))

    if seconds >= 25:
        remark = base_font.render("", True, white)
        WINDOW.blit(remark, (300, 400))
    elif seconds >= 20:
        remark = base_font.render("", True, white)
        WINDOW.blit(remark, (300, 400))
    elif seconds >= 16:
        remark = base_font.render("", True, white)
        WINDOW.blit(remark, (300, 400))
    elif seconds >= 13:
        remark = base_font.render("", True, white)
        WINDOW.blit(remark, (300, 400))
    elif seconds >= 10:
        remark = base_font.render(" ", True, white)
        WINDOW.blit(remark, (300, 400))
    elif seconds < 10:
        remark = base_font.render("", True, white)
        WINDOW.blit(remark, (300, 400))

    pygame.draw.rect(WINDOW, yellow, restart_rect)
    restart = base_font.render("RESTART", True, black)
    WINDOW.blit(restart, (602, 604))

start_ticks = pygame.time.get_ticks()
active = False

game_close = False
game_over = False


def main_loop():
    global active, user_text, seconds, start_ticks

    while not game_close:
        WINDOW.fill(black)
        pygame.draw.rect(WINDOW, yellow, reset_rect)
        reset_text = reset_font.render("New Sentence?", True, black)
        WINDOW.blit(reset_text, (602, 604))

        text_surface2 = base_font.render(words, True, word_color)
        WINDOW.blit(text_surface2, (90, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if reset_rect.collidepoint(event.pos):
                    text_surface3 = base_font.render(reset_words, True, word_color)
                    WINDOW.blit(text_surface3, (90, 350))
                    pygame.display.flip()

                if restart_rect.collidepoint(event.pos):
                    break

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        inGameTitle = title_font.render("Noob Typing Test", True, cyan)
        WINDOW.blit(inGameTitle, (400, 50))

        pygame.draw.rect(WINDOW, color, input_rect, 2)
        text_surface1 = base_font.render(user_text, True, cyan)
        WINDOW.blit(text_surface1, (input_rect.x + 10, input_rect.y + 12))

        if active == True and len(user_text) > 0:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if '.' in user_text:
                user_text.replace(user_text, ' ')
                break

            timer = base_font.render("Time: " + str(seconds - 2), True, white)
            WINDOW.blit(timer, (1010, 510))

        pygame.display.flip()
        clock.tick(60)

main_loop()
game_over_screen()
pygame.display.flip()
time.sleep(3)
