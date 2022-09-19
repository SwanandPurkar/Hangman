import pygame
import os
import math
import random

# setup display
pygame.init()
width = 800
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("HANGMAN")

# button variables
radius = 20
gap = 15
letters = []
start_x = round((width-((radius*2)+gap)*13)/2)
start_y = 400
A = 65
for i in range(26):
    x = start_x+(gap*2)+(((radius*2)+gap)*(i % 13))
    y = start_y+((i//13))*(gap+(radius*2))
    letters.append([x, y, chr(A+i), True])

# game variables
hangman_status = 0
words = ["DEVELOPER", "PYTHON", "INDIA", "PUNE", "ENGINEERING"]
word = random.choice(words)
guessed = []

FPS = 60
clock = pygame.time.Clock()
flag = True

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

# alphabet fonts
alphabet_font = pygame.font.SysFont('comicsans', 40)
word_font = pygame.font.SysFont('comicsans', 60)
title_font = pygame.font.SysFont('comicsans', 60)

# Loading the background image
bg_img = pygame.image.load('hangman_bg4.jpg')
bg_img = pygame.transform.scale(bg_img, (width, height))


def draw():

    text = title_font.render("BANG BEFORE THE HANG", 1, (0, 0, 0))
    window.blit(text, (width/2-text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter+" "
        else:
            display_word += "_ "

    text = word_font.render(display_word, 1, (255, 255, 255))
    window.blit(text, (400, 200))
    # draw buttons
    for letter in letters:
        x, y, alphabet, visible = letter
        if visible:
            pygame.draw.circle(window, (255, 255, 255), (x, y), radius, 3)
            text = alphabet_font.render(alphabet, 1, (255, 0, 0))
            window.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    window.blit(images[hangman_status], (180, 150))
    pygame.display.update()


def display_message(msg):
    pygame.time.delay(1000)
    window.blit(bg_img, (0, 0))
    text = word_font.render(msg, 1, (0, 0, 0))
    window.blit(text, (width/2-text.get_width() /
                2, height/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


# game loop
while flag:
    clock.tick(FPS)
    window.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, alphabet, visible = letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+(y-m_y)**2)
                    if dis < radius:
                        letter[3] = False
                        guessed.append(alphabet)
                        if alphabet not in word:
                            hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won == True:
        display_message("YOU ARE SAFE!")
        break

    if hangman_status == 6:
        display_message("YOU ARE HANGED!")
        break


pygame.quit()
