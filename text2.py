#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
import gameutil as gu                   # 自作モジュール読み込み(同時に省略名設定)
import os

class Text2:
    def __init__(self):
        self.SCR = { 'W' : 200, 'H' : 100 } # 表示ウィンドウのサイズ
        self.main()

    def main(self):
        screen = gu.init((self.SCR['W'], self.SCR['H']), 'Font Practice 2')

        strjp = u"日本語表示テスト"

        # フォント名パスを作る
        udir = pygame.font.match_font('takaop')

        font = pygame.font.Font(udir, 24) # フォントを読み込む

        text = font.render(strjp, False, (255, 255, 255))

        while True:
            screen.blit(text, (0, 0))   # 文字を画面に貼り付ける
            pygame.display.flip()       # 画面を反映
            for event in pygame.event.get(): # イベントチェック
                if gu.exit_check(event, K_ESCAPE):
                    return
        
if __name__ == '__main__':
    main = Text2()
    # end of file
