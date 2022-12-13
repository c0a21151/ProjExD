import pygame as pg
import random
import sys
import time
import tkinter as tk
import tkinter.messagebox as tkm


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


"""
def restart():  #ウィンドウを閉じずに再スタートする
    # root = tk.Tk()
    # tkm.showinfo()
    key_dct = pg.key.get_pressed()
    if key_dct[pg.K_F1] == False: 
        if key_dct[pg.K_SPACE]:
            main()
        if key_dct[pg.K_KP_ENTER]:
            return
"""



def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    
    vx, vy = +3, +3

    st = time.time()
    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 2
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 2
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 2
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 2
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) 

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        # 練習８
        if tori_rct.colliderect(bomb_rct): #こうかとんが爆弾に当たったら
            ed =  time.time()

            vx = 0
            vy = 0

            tori_sfc2 = pg.image.load("fig/8.png")
            tori_sfc2 = pg.transform.rotozoom(tori_sfc2, 0, 2.0)
            tori_rct2 = tori_sfc2.get_rect()
            tori_rct2.center = tori_rct.centerx, tori_rct.centery
            # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
            scrn_sfc.blit(tori_sfc2, tori_rct)

            root = tk.Tk()
            root.withdraw()
            tkm.showinfo("gameover", f"こうかとんは{(ed-st):.2f}秒で爆弾に当たった \n 続けますか？")
            
            """
            #こうかとんが爆弾に当たったら逃げた時間と続けるか聞く
            #フォントの用意 
            font1 = pygame.font.SysFont("hg正楷書体pro", 150)
            font2 = pygame.font.SysFont(None, 50)
            #テキストの設定
            text = f"こうかとんは{(ed-st):.2f}秒で爆弾に当たった"
            text1 = font1.render(str(text), True, (0,0,255))
            text2 = font2.render("続けますか？　push key", True, (255,0,0))
            text3 = font2.render("Yes-SPACE", True, (255,0,0))
            text4 = font2.render("No-ENTER", True, (255,0,0))
            #テキストを描画
            scrn_sfc.blit(text1, (400,200))
            scrn_sfc.blit(text2, (500,300))
            scrn_sfc.blit(text3, (400,400))
            scrn_sfc.blit(text4, (400,500))
                
            pg.display.update() #描画処理を実行
            """

            # pg.time.wait(1000)

            # restart() 
            return()  
            
            
              

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
