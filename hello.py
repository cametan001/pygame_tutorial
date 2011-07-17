#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
# SCR_W, SCR_H = 200, 100                 # 表示ウィンドウのサイズ

# def main():
#     pygame.init()                       # pygameの初期化
#     screen = pygame.display.set_mode((SCR_W, SCR_H)) # 画面を作る
#     pygame.display.set_caption('Hello pygame')       # タイトル
#     pygame.display.flip()                            # 画面を片影

#     while True:
#         for event in pygame.event.get(): # イベントチェック
#             if event.type == QUIT:       # 終了が押された?
#                 return
#             elif (event.type == KEYDOWN and event.key == K_ESCAPE): # ESCが押された?
#                 return
#             else:
#                 pass

class Hello:
    def __init__(self):
        self.SCR = { 'W' : 200, 'H' : 100 } # 表示ウィンドウの大きさ
        self.main()

    def main(self):
        pygame.init()                   # pygameの初期化
        screen = pygame.display.set_mode((self.SCR['W'], self.SCR['H'])) # 画面を作る
        pygame.display.set_caption('Hello pygame') # タイトル
        pygame.display.flip()                      # 画面を反映

        while True:
            for event in pygame.event.get(): # イベントチェック
                if event.type == QUIT:       # 終了が押された?
                    return
                elif (event.type == KEYDOWN and event.key == K_ESCAPE): # ESCが押された?
                    return
                else:
                    pass

if __name__ == '__main__':
    main = Hello()
    # end of file
