import random
import pygame
from constants2 import *
from blocks import *
import sys
from Player import *


pygame.init()

pygame.display.set_caption("Moving Background")

background_x = 0

clock = pygame.time.Clock()

blocks= []
blocks_rect = []
for i in range(100):
    h = random.randint(HEIGHT//2 ,HEIGHT)
    b = Blocks(2000+300*i,h,300,h)
    blocks_rect.append(b.get_rect())
    blocks.append(b)



p1 = Player(100,100,100,100,False,0,HEIGHT)
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.jump()

    p1.location_update()
    keys = pygame.key.get_pressed()
    p1.move(keys)


    background_x -= 1

    # Wrap background around when it goes off-screen
    if background_x <= -background_rect.width:
        background_x = 0

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    collision_index = p1.get_rect().collidelist(blocks_rect)
    # print(collision_index)
    if collision_index != -1:
        p1.stop_jumping()
        print(blocks[collision_index].get_height())
        p1.setfloor_height(blocks[collision_index].get_height())
    else:
        # p1.start_jumping()
        p1.setfloor_height(HEIGHT)


    # Blit the background onto the screen
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + background_rect.width, 0))
    p1.draw()
    for i in range(100):
        blocks[i].move_blocks_x()
        blocks[i].draw()

    blocks_rect = [i.get_rect() for i in blocks]

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)