#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
import gameutil as gu

Sprite = pygame.sprite.Sprite
SCREEN = { 'W' : 200, 'H' : 200 }

class Block(Sprite):
    def __init__(self, pos = (0, 0)):
        Sprite.__init__(self)
        self.image = gu.load_image('img/block.bmp', -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.movepow = 2

    def update(self):
        if (self.rect.left + self.movepow < 0 or \
            self.rect.right + self.movepow > SCREEN['W']):
            self.movepow *= -1
        self.rect.move_ip(self.movepow, 0)

class Sprite1:
    def __init__(self):
        self.screen = gu.init((200, 200), 'Sprite tutorial 1')
        self.spritegroup = pygame.sprite.RenderPlain()
        self.spritegroup.add([Block((32 * x, 32 * x)) for x in range(0, 6)])
        self.clock = pygame.time.Clock()
        self.main()

    def main(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.spritegroup.draw(self.screen)
            pygame.display.flip()
            self.spritegroup.update()
            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return

if __name__ == '__main__':
    main = Sprite1()
    # EOF
