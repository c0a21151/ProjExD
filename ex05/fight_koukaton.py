import pygame as pg
import random
import sys
import time


class Screen:
    def __init__ (self, title, wh, img_path):
        # 練習１
        pg.display.set_caption(title)  #"逃げろ！こうかとん"
        self.sfc = pg.display.set_mode(wh)  #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)  #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)  #"fig/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)  #2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy  #900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Shot:  #弾
    def __init__(self, vxy, scr:Screen, kkt:Bird):
        self.sfc = pg.Surface((20, 20))
        pg.draw.rect(self.sfc, "black",   (0, 0, 10, 10))
        self.rct = self.sfc.get_rect()
        self.rct.centerx = kkt.rct.centerx 
        self.rct.centery = kkt.rct.centery - 10 
        self.vx, self.vy = vxy
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
          
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    timebgin = time.time()  #時間取得

    # 練習1
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/3.png", 2.0, (900, 400))
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    kkt.update(scr) 

    # 練習５
    bkd_lst = []
    bkd_color = ["red", "blue", "green", "yellow", "gold", "silver"]  #爆弾の色
    for i in bkd_color:  #爆弾の色リスト分爆弾を作る
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1])
        size = random.choice([10, 15])
        bkd = Bomb(i, size, (vx, vy), scr)
        bkd_lst.append(bkd)
    bkd.update(scr)

    tama_lst = []

    sht = True  #フラグをTrue (Trueの時弾が発射できる)

    # 練習２
    while True:
        scr.blit()  #scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr) 
        for i in bkd_lst:
            i.update(scr) 
            if kkt.rct.colliderect(i.rct):
                return

        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_SPACE]:  #SpaceKeyが押されたときshtがTrueなら弾を発射
            if sht == True:
                tama = Shot((0, 5), scr, kkt)
                tama_lst.append(tama)
                sht = None  #フラグをNone
            
        for i in tama_lst:
            i.update(scr)

        timeend = time.time()  #時間取得
        if timeend-timebgin>2:  #弾発射から時間が2秒以上経過していたらshtをTrueにする
            sht = True  #フラグをTrue
            timebgin = time.time()  #時間取得

        for i in tama_lst:  #弾が爆弾に当たったとき
            for n in bkd_lst:
                if i == n:
                    del i
                    del n  

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

