import pygame
import utils
from utils import Car
from constants import *

pygame.init()
pygame.display.set_caption('ParkingGaucho')
screen = pygame.display.set_mode((1280, 800))
playing = True
fps = 60
current_level = 0
direction = starting_dirs[current_level]



car = Car(starting_pos[current_level], car_img, direction)

while playing:
    pygame.time.Clock().tick(fps)
    screen.fill(0)
    screen.blit(parking[current_level], (0, 0))

    utils.commands()
    utils.afficher_pieces(screen, current_level)

    rect = pygame.transform.rotate(car.img, car.direction).get_rect(center=car.pos)
    screen.blit(pygame.transform.rotate(car.img, car.direction), rect)
    car.move()



    pygame.display.update()