#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
import gameutil as gu                   # 自作モジュール読み込み(同時に省略名設定)

class Text3:
    def __init__(self):
        self.SCR = { 'W' : 200, 'H' : 100 } # 表示ウィンドウの大きさ
        self.main()

    def main(self):
        screen = gu.init((self.SCR['W'], self.SCR['H']), 'Font Practice 3')

        strjp = u"日本語文字列\n改行のテスト"

        # フォント名パス
        udir = pygame.font.match_font('takaop')

        font = pygame.font.Font(udir, 24) # フォントを読み込む

        strlist = strjp.split("\n")      # 改行文字で分割したリストを作る
        y = 0                            # 貼り付けるy座標初期値
        for s in strlist:
            text = font.render(s, False, (255, 255, 255))
            screen.blit(text, (0, y))
            y += text.get_rect().h      # 文字の高さ分、下にずらして改行
        
        while True:
            pygame.display.flip()       # 画面を反映
            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return

if __name__ == '__main__':
    main = Text3()
    # end of file
