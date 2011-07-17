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
        self.image = gu.load_image('img/block.bmp')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.movepow = 2

    def update(self, *args):
        if (self.rect.left + self.movepow < 0 or \
            self.rect.right + self.movepow > SCREEN['W']):
            self.movepow *= -1
        self.rect.move_ip(self.movepow, 0)

class Player(Sprite):
    def __init__(self, pos = (0, 0)):
        Sprite.__init__(self)
        self.image = gu.load_image('img/player.bmp', -1)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self, keyin, *args):
        m = { 'x' : 0, 'y' : 0 }
        if keyin[K_LEFT] : m['x'] = -2
        if keyin[K_RIGHT] : m['x'] = 2
        if keyin[K_UP] : m['y'] = -2
        if keyin[K_DOWN] : m['y'] = 2
        self.rect.move_ip(m['x'], m['y'])

class Sprite2:
    def __init__(self):
        self.screen = gu.init((200, 200), 'Sprite tutorial 2')
        self.backscreen = pygame.Surface(self.screen.get_size())
        self.spritegroup = pygame.sprite.RenderClear()
        self.player = pygame.sprite.RenderClear(Player())
        self.spritegroup.add([Block((32 * x, 32 * x)) for x in range(0, 6)])
        self.clock = pygame.time.Clock()
        self.main()

    def main(self):
        while True:
            self.clock.tick(60)
            aDic = { self.spritegroup : None,
                     self.player : pygame.key.get_pressed() }
            [k.clear(self.screen, self.backscreen) for k in aDic.keys()]
            [k.draw(self.screen) for k in aDic.keys()]
            pygame.display.flip()
            [k.update(aDic[k]) for k in aDic.keys()]
            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return

if __name__ == '__main__':
    main = Sprite2()
    # EOF
