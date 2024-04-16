from constants2 import *
import pygame
import sys

class Blocks():
    def __init__(self, blocks_x, blocks_y, blocks_width, blocks_height):
        self.blocks_x = blocks_x
        self.blocks_y = blocks_y
        self.blocks_width = blocks_width
        self.blocks_height = blocks_height

    def draw(self):
        pygame.draw.rect(screen, ORANGE, (self.blocks_x, self.blocks_y, self.blocks_width, self.blocks_height))

    def move_blocks_x(self):
        self.blocks_x -= 5

    def get_rect(self):
        return pygame.Rect(self.blocks_x,self.blocks_y,self.blocks_width,self.blocks_height)

    def get_height(self):
        return blocks_y