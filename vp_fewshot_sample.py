import sys
import pygame
from pygame.locals import *
import os
import random

# Categories and images
categories = ['cat', 'dog', 'turtle']
images = {cat: [pygame.image.load(os.path.join(cat, img)) for img in os.listdir(cat)] for cat in categories}

# Shuffle images
for img_list in images.values():
    random.shuffle(img_list)

background = pygame.image.load("animal wallpaper.jpeg")  # Load the background image

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
startgame = pygame.Surface((400,100))
quit = pygame.Surface((400,100))

pygame.font.init() 
font = pygame.font.SysFont('skia', 48)
text = font.render("Animal Classification", True, (0,0,0))
game = font.render("Start Game", True,(0,0,0))
quit = font.render("Quit", True, (0,0,0))

RED = (255,0,0)
LIGHTRED = (255, 117, 117)
BLUE = (89, 197, 214)
BLACK = (0,0,0)

startgame = pygame.Surface((475,100))
quit = pygame.Surface((475,100))

width = screen.get_width()
height = screen.get_height()

button_width = 500
button_height = 100
button_spacing = 25
button_x = width // 2 - button_width // 2
button_y = height // 2 - button_height // 2

toggle1 = 0
toggle2 = 0

results = []

width = screen.get_width()
height = screen.get_height()

toggle1 = 0
toggle2 = 0

RED = (255,0,0)
LIGHTRED = (255, 117, 117)
BLUE = (89, 197, 214)
BLACK = (0,0,0)

# Game state
stage = 'start'
num_examples = len(categories)
example_count = 0
correct_count = 0

# Calculate total test images
total_test_images = sum(len(img_list) for img_list in images.values())

# Feedback message
message = ''
feedback_button = pygame.Rect(350, 500, 150, 50)

# Button setup
next_button = pygame.Rect(600, 500, 150, 50)
category_buttons = [pygame.Rect(20 + i * 270, 500, 150, 50) for i in range(len(categories))]
button_width = 500
button_height = 100
button_spacing = 50
button_x = width // 2 - button_width // 2
button_y = height // 2 - button_height // 2

def prepare_image_list():
    image_list = [(cat, img) for cat in categories for img in images[cat]]
    random.shuffle(image_list)
    return image_list

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            if stage == 'start':
                # Press anywhere to start the game
                stage = 'training'
                training_images = prepare_image_list()
                category, image = training_images.pop()
                message = f'This is a {category}'

            elif stage == 'training' and next_button.collidepoint(mouse_pos):
                # Press 'Next' to move to next image
                example_count += 1
                if example_count >= num_examples:
                    # If we've shown enough examples, switch to testing stage
                    example_count = 0
                    stage = 'testing'
                    testing_images = prepare_image_list()
                    category, image = testing_images.pop()
                    message = ''
                else:
                    # Otherwise, load next image
                    category, image = training_images.pop()
                    message = f'This is a {category}'

            elif stage == 'feedback' and feedback_button.collidepoint(mouse_pos):
                # Acknowledge feedback and move to next image
                example_count += 1
                if example_count >= total_test_images:
                    stage = 'end'
                else:
                    stage = 'testing'
                    category, image = testing_images.pop()

            elif stage == 'testing':
                # Check if one of category buttons is clicked
                for i, button in enumerate(category_buttons):
                    if button.collidepoint(mouse_pos):
                        # Check if player's guess was correct
                        if categories[i] == category:
                            message = 'Correct!'
                            correct_count += 1
                        else:
                            message = f'Incorrect! The correct category was {category}'
                        # Switch to feedback stage
                        stage = 'feedback'
                    if button.collidepoint(mouse_pos):
                     guess = categories[i]
                     correct = (guess == category)
                     results.append((category, guess, correct))  # Add this line
                     message = 'Correct!' if correct else f'Incorrect! It was a {category}'
                     stage = 'feedback'
                     break

    screen.fill((255, 255, 255))

    if stage == 'start':
        mouse_pos = pygame.mouse.get_pos
        # Display start screen
        screen.blit(background, (0, 0))  # Draw the background
        pygame.display.flip
        pygame.draw.rect(screen, BLUE, [125,125,540,100], 0)
        screen.blit(text, (175,150))

        #Start game button
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
        # text = font.render('Click to start', True, (0, 0, 0))
        # screen.blit(text, (20, 80))

        if toggle1 == 1:
            startgame.fill(LIGHTRED)

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

    elif stage in ['training', 'testing', 'feedback']:
        # Display images
        screen.blit(image, (20, 80))
        # Display 'Next' button if in 'training' stage
        if stage == 'training':
            pygame.draw.rect(screen, [0, 255, 0], next_button)  # draw button
            text = font.render('Next', True, (BLACK))
            screen.blit(text, (next_button.x + 20, next_button.y + 0))
        # Display category buttons if in 'testing' stage
        elif stage == 'testing':
            for i, button in enumerate(category_buttons):
                pygame.draw.rect(screen, [0, 255, 0], button)  # draw button
                text = font.render(categories[i], True, (BLACK))
                screen.blit(text, (button.x + 15, button.y + 0))
        # Display feedback message
        text = font.render(message, True, (BLACK))
        screen.blit(text, (200, 400))
        if stage == 'feedback':
            pygame.draw.rect(screen, [0, 255, 0], feedback_button)  # draw button
            text = font.render('Next', True, (BLACK))
            screen.blit(text, (feedback_button.x + 25, feedback_button.y + 0))

    elif stage == 'end':
        # Display final accuracy
        accuracy = correct_count / total_test_images
        text = font.render('Game Over! Your accuracy: {:.2f}'.format(accuracy), True, (0, 0, 0))
        screen.blit(text, (20, 80))

    print(results)

    pygame.display.flip()

pygame.quit()
