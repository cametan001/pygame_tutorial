#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pygame
from pygame.locals import *
import gameutil as gu
import os.path

def load_sound(name):
    """ファイルから音声を読み込む"""
    class NoneSound:
        """音声ドライバがないとき用"""
        def play(self): pass

    # サウンドカードの初期化に失敗した場合、
    # playを呼んでも何もしないクラスを返す。
    # こうすることで、途中で止まることがなくなる。
    if not pygame.mixer:
        return NoneSound()

    try:                                # 読み込み失敗したらエラー処理
        sound = pygame.mixer.Sound(name)
    except pygame.error, msg:
        print 'サウンドが読み込めません', wav
        raise SystemExit, msg
    return sound

class soundOut:
    def __init__(self):
        self.screen = gu.init((200, 100), 'sound test')
        self.sound = load_sound( \
            os.path.join(os.path.dirname(__file__), 'sound/shot.wav'))
        self.main()

    def main(self):
        while True:
            self.screen.fill((0, 0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if gu.exit_check(event, K_ESCAPE):
                    return
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    self.sound.play()   # スペースキーが押されたら音を鳴らす
                else:
                    pass

if __name__ == '__main__':
    main = soundOut()
    # EOF
