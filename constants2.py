import pygame
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
ORANGE = (115,66,34)
WIDTH, HEIGHT = 1200,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Moving Background")
background = pygame.image.load('./images/bg.png')
background_rect = background.get_rect()

background_x = 0


clock = pygame.time.Clock()


rectangle_width = 50
rectangle_height = 50
rectangle_x = 200
rectangle_y = 300
jumping = False
rectangle_velocity_y = 0


blocks_x =2000
blocks_y = 350
blocks_width = 500
blocks_height = 500

clock.tick(60)
FPS = 60

screen.fill((255, 255, 255))

player_rect = Rect(200, 500, 50, 50)
player_rect2 = Rect(200, 0, 50, 50)
gravity = 4