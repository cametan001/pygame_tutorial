#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""Joystick easy control class"""

import pygame
from pygame.locals import *
import gameutil as gu

# Define Constant Valiable
# Digital input
J = { 'LEFT' : 0, \
      'RIGHT' : 1, \
      'DOWN' : 2, \
      'UP' : 3, \
      # Digital button input
      'BTN' : [x for x in range(20)] }

class Joystick:
    accuracy = 4
    def __init__(self, id = 0, mode = 0):
        joystick = pygame.joystick      # short name
        joystick.init()
        if not joystick.get_init():
            print "Initialize error:"
            self.sticknum = 0
        else:
            self.sticknum = joystick.get_count()
            self._setup(id)
        self._mode = mode

    def ChangeStick(id):
        if id < self.sticknum:
            return self._setup(id)
        else:
            return False

    def _setup(self, id):
        try:
            self.stick = pygame.joystick.Joystick(id)
        except pygame.error, message:
            print "Joystick ID Error: %d" % id
            raise SystemExit, message
        self.stick.init()
        return self.stick.get_init()

    def get_button(self):
        return tuple( \
            [self.stick.get_button(i) for i in range(self.stick.get_bumbuttons())] \
            )

    def get_axis(self):
        if self._mode != 0:
            return tuple( \
                [round(self.stick.get_axis(i), self.accuracy) \
                 for i in range(self.stick.get_numaxes())])
        else:
            return tuple( \
                self._get_arrow( \
                    [ i == 1 and round(self.stick.get_axis(i), self.accuracy) or \
                      -round(self.stick.get_axis(i), self.accuracy)
                      for i in range(self.stick.get_numaxes()) if i < 2]))

    def get_hat(self):
        return tuple(self._get_arrow(self.stick.get_hat(0)))
        
    def _get_arrow(self, inputpos):
        inputs = []
        for h in inputpos:
            if h < 0:
                inputs + [1, 0]
            elif h > 0:
                inputs + [0, 1]
            else:
                inputs + [0, 0]
        return inputs

class JS:
    def _init__(self):
        self.screen = gu.init((600, 300), 'Joystick test')
        self.mychar = gu.load_image('img/char.bmp', -1)
        self.myrect = self.mychar.get_rect()

        self.joy = Joystick(0)

        self.clock = pygame.time.Clock()

        self.main()

    def main(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0)) # clear screen
            self.screen.blit(self.mychar, self.myrect) # blit my character
            pygame.display.flip()                      # flit all display
            keyin = self.joy.get_hat(), self.joy.get_asix() # get input joystic

            if keyin[0][J['LEFT']] or keyin[1][J['LEFT']]:
                self.myrect.move_ip(-1, 0)
            elif keyin[0][J['RIGHT']] or keyin[1][J['RIGHT']]:
                self.myrect.move_ip(1, 0)
            elif keyin[0][J['UP']] or keyin[1][J['UP']]:
                self.myrect.move_ip(0, -1)
            elif keyin[0][J['DOWN']] or keyin[1][J['DOWN']]:
                self.myrect.move_ip(0, 1)
            else:
                pass

            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return
            
if __name__ == '__main__':
    main = JS()
