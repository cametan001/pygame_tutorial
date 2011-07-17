#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
import gameutil as gu                   # 自作モジュール読み込み(同時に省略名設定)

class Text1:
    def __init__(self):
        self.SCR = { 'W' : 200, 'H' : 100 }
        self.main()

    def main(self):
        screen = gu.init((self.SCR['W'], self.SCR['H']), 'Font Practice 1')
        font = pygame.font.Font(None, 32) # フォントを読み込む

        # テキスト表示用Surfaceを作る
        # render(text, antialias, color)
        # antialias(アンチエイリアス)はなめらか表示にするかどうかの意味
        text = font.render('Hello, pygame!', False, (255, 255, 255))

        while True:
            screen.blit(text, (0, 0))   # 文字を画面に貼り付ける
            pygame.display.flip()       # 画面を反映
            for event in pygame.event.get(): # イベントチェック
                if gu.exit_check(event, K_ESCAPE):
                    return
                
if __name__ == '__main__':
    main = Text1()
