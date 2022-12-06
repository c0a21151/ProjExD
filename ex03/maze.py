import tkinter as tk
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, mx, my, tori
    
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 0: #移動先が道だったら
        tori1 = tk.PhotoImage(file="9.png")
        canvas.create_image(cx, cy, image=tori1, tag="kokaton9")

    if maze_lst[mx][my] == 1:  #移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
        tori2 = tk.PhotoImage(file="8.png")
        canvas.create_image(cx, cy, image=tori2, tag="kokaton8")

    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)

    if cx == ex and cy == ey: #こうかとんがりんごについたら
        label = tk.Label(root, text="おいしい!!", font=("", 100), fg="red")
        label.pack()

    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    label0 = tk.Label(root, text="こうかとんはりんごが食べたい", font=("", 20), fg="black")  #こうかとんをりんごへ誘導
    label0.pack()

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    #print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori0 = tk.PhotoImage(file="0.png")
    canvas.create_image(cx, cy, image=tori0, tag="kokaton0")  #こうかとんの初期画像
    ex, ey = mx*1500-150, my*900-150
    get = tk.PhotoImage(file="apple.PNG")  #ゴールはりんごの画像
    canvas.create_image(ex, ey, image=get, tag="apple")


    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    
    root.mainloop()