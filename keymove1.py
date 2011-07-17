#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import os.path
import pygame
from pygame.locals import *

class keyMove1:
    def __init__(self):
        self.SCR = { 'W' : 200, 'H' : 100 }
        self.main()

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((self.SCR['W'], self.SCR['H']))
        pygame.display.set_caption('Hello pygame')

        image = pygame.image.load( \
            os.path.join(os.path.dirname(__file__), 'img/char.bmp'))
        image = image.convert()
        imagerect = image.get_rect()
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)              # keep the 60 fps
            screen.blit(image, imagerect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
                elif (event.type == KEYDOWN and event.key == K_RIGHT):
                    imagerect.move_ip(1, 0)
                elif (event.type == KEYDOWN and event.key == K_LEFT):
                    imagerect.move_ip(-1, 0)
                else:
                    pass

if __name__ == '__main__':
    main = keyMove1()
