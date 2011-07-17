#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os.path
import pygame
from pygame.locals import *

class moveImage:
    def __init__(self):
        self.SCR = { 'W' : 200, 'H' : 100 } # 表示ウィンドウの大きさ
        self.main()

    def main(self):
        pygame.init()                   # pygameの初期化
        screen = pygame.display.set_mode((self.SCR['W'], self.SCR['H'])) # 画面を作る
        pygame.display.set_caption('Hello pygame') # タイトル

        image = pygame.image.load( \
            os.path.join(os.path.dirname(__file__), 'img/char.bmp')) # 絵を読み込む
        image = image.convert()                                  # 環境にあわせ最適化
        imagerect = image.get_rect()                             # imageのrectを取得
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)              # keep the 60 fps
            screen.fill((0, 0, 0))      # 画面のクリア
            screen.blit(image, imagerect) # 絵を画面に貼り付ける
            pygame.display.flip()         # 画面を反映
            imagerect.x += 1              # 画像を移動
            for event in pygame.event.get(): # イベントチェック
                if event.type == QUIT:       # 終了が押された?
                    return
                elif (event.type == KEYDOWN and event.key == K_ESCAPE): # ESCが押された?
                    return
                else:
                    pass

if __name__ == '__main__':
    main = moveImage()
    # end of file
