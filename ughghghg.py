import pygame, sys
from pygame.locals import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Few Shot Learning Task')

pygame.font.init() 
font = pygame.font.SysFont('skia', 48)
text = font.render("Animal Classification", True, (0,0,0))
game = font.render("Start Game", True,(0,0,0))
quit = font.render("Quit", True, (0,0,0))

# image = "francysam.jpg"
imp = pygame.image.load("animal wallpaper.jpeg").convert()

RED = (255,0,0)
LIGHTRED = (255, 117, 117)
BLUE = (89, 197, 214)
BLACK = (0,0,0)

startgame = pygame.Surface((400,100))
quit = pygame.Surface((400,100))

width = screen.get_width()
height = screen.get_height()

button_width = 400
button_height = 100
button_spacing = 50
button_x = width // 2 - button_width // 2
button_y = height // 2 - button_height // 2

mouse_pos = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

toggle1 = 0
toggle2 = 0

# Game state
game_state = 'start'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == 'start':
        # screen.fill((255,255,255))
        game_state = "running"

#Title screen 
        # Animal wallpaper background
        screen.blit(imp,(0,0))
        pygame.display.flip
        # Title screen
        pygame.draw.rect(screen, BLUE, [125,125,540,100], 0)
        screen.blit(text, (175,150))

#Start game button
        # pygame.draw.rect(screen, RED, [210,300,400,100], 0)
        # screen.blit(tutorial, (270,320))
        if toggle1 == 0:
            startgame.fill(RED)
            button1_rect = startgame.get_rect()
            button1_rect.x = button_x
            button1_rect.y = button_y
            screen.blit(startgame, button1_rect)
            text1 = font.render('Start Game',True, BLACK)
            text1_rect = text1.get_rect()
            text1_rect.center = button1_rect.center
            screen.blit(text1, text1_rect)

            if toggle1 == 1:
                startgame.fill(LIGHTRED)

        # if toggle1 == 2:
        #     # screen.blit(imp,(0,0))
        #     # pygame.display.flip
        #     screen.fill((255,255,255))

    #Quit button
            # pygame.draw.rect(screen, RED, [210,450,400,100], 0)
            # screen.blit(game, (290,470))
        if toggle2 == 0:
            quit.fill(RED)
            button2_rect = quit.get_rect()
            button2_rect.x = button_x
            button2_rect.y = button_y + button_height + button_spacing
            screen.blit(quit, button2_rect)
            text2 = font.render('Quit', True, BLACK)
            text2_rect = text2.get_rect()
            text2_rect.center = button2_rect.center
            screen.blit(text2, text2_rect)

            if toggle2 == 1:
                quit.fill(LIGHTRED)

# Select option
        if button1_rect.collidepoint(mouse_pos):
                toggle1 = 1
                # print("hi")
                if event.type == MOUSEBUTTONDOWN:
                 toggle1 = 2
        if button1_rect.collidepoint(mouse_pos) == 0:
            toggle1 = 0
        if button2_rect.collidepoint(mouse_pos):
                 toggle2 = 1
                 if event.type == MOUSEBUTTONDOWN:
                  pygame.quit()
                  sys.exit()
                #   print("hello2")
                #  print("hi2")
        if button2_rect.collidepoint(mouse_pos) == 0:
            toggle2 = 0
        if event.type == MOUSEBUTTONDOWN:
            print("hi")
        # if button1_rect.collidepoint(click):
        #     # screen.blit(imp,(0,0))
        #     # pygame.display.flip
        #     print("hi")
        # if click[0] == 1 and click != None:
        #     screen.blit(imp,(0,0))()         

    pygame.display.update()