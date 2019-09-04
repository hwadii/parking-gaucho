import pygame
from pygame.locals import *
from constants import *
import math

inputs = [False, False, False, False, False, False]

class Car:
    def __init__(self, pos, img, direction=0, accel=0):
        self.pos = pos
        self.img = img
        self.direction = direction
        self.accel = accel

    def move(self):
        vx = math.cos(self.direction / 57.29) * self.accel
        vy = math.sin(self.direction / 57.29) * self.accel
        self.pos = (self.pos[0] + vx, self.pos[1] - vy)
        # if self.accel > 0 or self.accel < 0:
        if inputs[0]==True:
            self.direction-= 3
            while self.direction < 0:
                self.direction += 360
        if inputs[1]==True:
            self.direction+= 3
            while self.direction > 359:
                self.direction -= 360
        if inputs[2] == True:
            self.accel += 0.5
        if inputs[3] == True and self.accel >= 0:
            self.accel -= 5
        if self.accel > 0.125:
            self.accel -= 0.25
        if self.accel >= -4 and self.accel < 0:
            self.accel += 1

def commands():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                inputs[1]=True
            elif event.key==K_RIGHT:
                inputs[0]=True
            elif event.key==K_UP:
                inputs[2]=True
            elif event.key==K_DOWN:
                inputs[3]=True
            elif event.key==K_SPACE:
                inputs[4]=True
            elif event.key==K_LCTRL:
                inputs[5]=True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()



        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                inputs[1]=False
            elif event.key==pygame.K_RIGHT:
                inputs[0]=False
            elif event.key==pygame.K_UP:
                inputs[2]=False
            elif event.key==pygame.K_DOWN:
                inputs[3]=False
            elif event.key==pygame.K_SPACE:
                inputs[4]=False
            elif event.key==pygame.K_LCTRL:
                inputs[5]=False

def afficher_pieces(screen, level):
    piece_img = pygame.image.load("assets/coin.png")
    for piece in coins[level]:
        screen.blit(piece_img, piece.pos())

def ramasser_pieces():
    for i, coin in enumerate(coins[current_level]):
        collision = detectCollisions(coin.x,coin.y,coin.width,coin.height,rect.x,rect.y,rect.width,rect.height)
        coin.render(collision)
        if collision:
            coins[current_level].pop(i)

def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    else:
        return False