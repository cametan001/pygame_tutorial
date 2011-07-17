#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
import gameutil as gu

class Block:
    def __init__(self, pos):
        self.image = gu.load_image('img/block.bmp')
        self.rect = pygame.Rect(pos, self.image.get_size())

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player:
    def __init__(self, pos):
        self.image = gu.load_image('img/char.bmp')
        self.rect = pygame.Rect(pos, self.image.get_size())

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Collide1:
    def __init__(self):
        self.screen = gu.init((200, 200), 'Colide test 1')
        self.block = Block((32, 64))
        self.player = Player((0, 0))

        self.clock = pygame.time.Clock()

        self.main()

    def main(self):                      # main loop
        while True:
            self.clock.tick(60)
            keyin = pygame.key.get_pressed()
            m = { 'x' : 0, 'y' : 0 }

            if keyin[K_LEFT]:
                m['x'] = -2
            elif keyin[K_RIGHT]:
                m['x'] = 2
            else:
                pass

            if self.block.rect.colliderect(self.player.rect.move(m['x'], 0)):
                if m['x'] < 0:
                    self.player.rect.left = self.block.rect.right
                elif m['x'] > 0:
                    self.player.rect.right = self.block.rect.left
                else:
                    pass
            else:
                self.player.rect.move_ip(m['x'], 0)

            if keyin[K_UP]:
                m['y'] = -2
            elif keyin[K_DOWN]:
                m['y'] = 2
            else:
                pass

            if self.block.rect.colliderect(self.player.rect.move(0, m['y'])):
                if m['y'] < 0:              # K_UP pressed
                    self.player.rect.top = self.block.rect.bottom
                elif m['y'] > 0:            # K_DOWN pressed
                    self.player.rect.bottom = self.block.rect.top
                else:
                    pass
            else:
                self.player.rect.move_ip(0, m['y'])

            self.screen.fill((0, 0, 0))          # clear screen
            self.block.draw(self.screen)         # draw block object
            self.player.draw(self.screen)        # draw player object

            pygame.display.flip()

            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return

if __name__ == '__main__':
    main = Collide1()
