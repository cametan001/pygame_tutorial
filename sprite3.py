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

    def reflect(self):
        self.movepow *= -1
        self.update()

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

    def move(self, keyin):
        m = { 'x' : 0, 'y' : 0 }
        if keyin[K_LEFT]: m['x'] = -2
        if keyin[K_RIGHT]: m['x'] = 2
        if keyin[K_UP]: m['y'] = -2
        if keyin[K_DOWN]: m['y'] = 2
        return m           # return move position

class Sprite3:
    def __init__(self):
        self.screen = gu.init((200, 200), 'Sprite tutorial 3')
        self.backscreen = pygame.Surface(self.screen.get_size())
        self.spritegroup = pygame.sprite.RenderClear()
        self.player = Player((0, 32))
        self.playergrp = pygame.sprite.RenderClear(self.player)
        self.spritegroup.add([Block((32 * x, 32 * x)) for x in range(0, 6)])
        self.clock = pygame.time.Clock()
        self.collide = pygame.sprite.spritecollide
        self.main()

    def main(self):
        while True:
            self.clock.tick(60)
            aTuple = (self.spritegroup, self.playergrp)
            [k.clear(self.screen, self.backscreen) for k in aTuple]
            [k.draw(self.screen) for k in aTuple]
            pygame.display.flip()

            self.spritegroup.update()
            m = self.player.move(pygame.key.get_pressed())
            playser_oldrect = self.player.rect
            self.player.rect.move_ip(m['x'], 0)
            [(hits.reflect(), self.player.rect.move_ip(-m['x'], 0)) \
             for hits in self.collide(self.player, self.spritegroup, False)]
            self.player.rect.move_ip(0, m['y'])
            [self.player.rect.move_ip(0, -m['y']) \
             for hits in self.collide(self.player, self.spritegroup, False)]
            self.playergrp.update()
            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return

if __name__ == '__main__':
    main = Sprite3()
    # EOF
