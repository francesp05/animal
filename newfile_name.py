# import stuff you need (the library books to use for your project)
import pygame, sys
from pygame.locals import *

# start pygame
pygame.init()

# initialize a window of set dimensions (pixel width by height)
screen = pygame.display.set_mode((400, 300))

# set title of window
pygame.display.set_caption('Hello World!')

# create a variable to track the state of the game (i.e. start, running, input, phase 1, 2, 3, etc...)
game_state = "start"

while True:

    # check the game state variable - only erase the screen to background color if at the beginning of the game/trial
    if game_state == "start":
        screen.fill((255,255,255)) # (0,0,0) is black, (255,255,255) is white... visit "htmlcolorcodes.com" for other variations
        game_state = "running"

    ### DO NOT FORGET THIS PART!!!!!!!! ###
    # get all input events
    for event in pygame.event.get():
        # if quit is initiated, close the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ########################################

        # get keyboard (key down press) input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left pressed")
                pygame.draw.rect(screen,(26,134,105),(200,150,100,50)) # (screen,(R,G,B),(xcoor,ycoor,xwid,yheight)) -> draw rectange of color (R,G,B) at (x,y) coord with (x,y) width/height
            if event.key == pygame.K_RIGHT:
                print("right presssed")
                pygame.draw.rect(screen,(134,42,105),(250,50,100,50)) # (screen,(R,G,B),(xcoor,ycoor,xwid,yheight)) -> draw rectange of color (R,G,B) at (x,y) coord with (x,y) width/height
        
        # get keyboard (key up press) input
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("left unpressed")
                pygame.draw.rect(screen,(0,0,0),(200,150,100,50)) # (screen,(R,G,B),(xcoor,ycoor,xwid,yheight)) -> draw rectange of color (R,G,B) at (x,y) coord with (x,y) width/height
            if event.key == pygame.K_RIGHT:
                print("right unpresssed")
                pygame.draw.rect(screen,(0,0,0),(250,50,100,50)) # (screen,(R,G,B),(xcoor,ycoor,xwid,yheight)) -> draw rectange of color (R,G,B) at (x,y) coord with (x,y) width/height
        
        # can also do more cool things with other inputs (i.e. pygame.mouse.get_pos())

    # DO COOL STUFF HERE!!!
    # you could make things appear/disappear based on time or other non-input triggers

    # update the screen to show all the cool stuff you did in this loop
    pygame.display.update() # IF YOU FORGET THIS LINE -> NOTHING WILL SHOW UP!!!
    