from constants2 import *
import pygame

class Player():
    def __init__(self, player_x, player_y, player_height, player_width,is_jumping,velocity,floor_height):
        self.player_x = player_x
        self.player_y = player_y
        self.player_height = player_height
        self.player_width = player_width
        self.is_jumping = is_jumping
        self.velocity = velocity
        self.floor_height = floor_height

    def jump(self):

        if self.is_jumping == False:
            self.velocity =-20
            self.is_jumping = True



    def location_update(self):
        self.player_y += self.velocity
        if self.player_y < self.floor_height - self.player_height:
            self.velocity += 0.5
        else:
             self.player_y = self.floor_height - self.player_height
             self.velocity = 0
             self.is_jumping = False

    def move(self,keys):
        if keys[pygame.K_UP]:
            self.player_y -= 3
        if keys[pygame.K_DOWN]:
            self.player_y += 3
        if keys[pygame.K_LEFT]:
            self.player_x -= 3
        if keys[pygame.K_RIGHT]:
            self.player_x += 3

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.player_x, self.player_y,self.player_width, self.player_height))

    def get_rect(self):
        return  pygame.Rect(self.player_x,self.player_y,self.player_width,self.player_height)

    def stop_jumping(self):
        self.is_jumping = False
    def start_jumping(self):
        self.is_jumping = True

    def setfloor_height(self,y):
        self.floor_height = y