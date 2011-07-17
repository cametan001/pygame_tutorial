#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os.path
import pygame
from pygame.locals import *

# gameutil.py
# game utility class

def init(size = (200, 100), title = 'non title'):
    """initialize all and make suface using pygame.init()"""
    pygame.init()
    scr = pygame.display.set_mode(size)
    scrRect = scr.get_rect()
    pygame.display.set_caption(title)
    return scr

def load_image(filename, ckey = None):
    """あらゆるイメージをロードし、imageオブジェクトを返す。
    
    filename:ファイル名
    ckey:Colorkey設定。-1だと画像の左上ピクセルの色を拾う。"""
    try:
        img = pygame.image.load( \
            os.path.join(os.path.dirname(__file__), filename))
    except pygame.error, message:
        print '画像を読み込めません', filename
        raise SystemExit, message
    img = img.convert()
    if ckey != None:
        if ckey == -1:
            ckey = img.get_at((0, 0))
        img.set_colorkey(ckey, RLEACCEL)
    return img

def exit_check(event, inkey=None):
    if event.type == QUIT:
        return True
    if inkey is not None:
        if event.type == KEYDOWN and event.key == inkey:
            return True
    return False

# if __name__ == '__main__':

#EOF
