import pygame

class Sprite:
    #Class permettant de créer autant de sprite que nous le souhaitons

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def render(self,collision):
        if (collision==True):
            s = pygame.Surface((self.width,self.height))
            s.fill((0,255,0,128))
        else:
            s = pygame.Surface((self.width,self.height))
            s.fill((0,255,0,128))

    def pos(self):
        return (self.x, self.y)

parking = [pygame.image.load("assets/lvl1Finale.jpg"), pygame.image.load("assets/lvl2Finale.jpg"), pygame.image.load("assets/lvl3Finale.jpg")]
car_img = pygame.image.load("assets/veh2.png")

coins = [[Sprite(939,98,48,48), Sprite(1055,658,48,48), Sprite(201,642,48,48)]]

starting_pos = [(119, 100), (1186, 679), (1200, 100)]
starting_dirs = [0, 180, -90]