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
    if maze_lst[mx][my] == 0: 
        tori = tk.PhotoImage(file="9.png")
        canvas.create_image(cx, cy, image=tori, tag="kokaton")

    if maze_lst[mx][my] == 1:  #移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
        tori = tk.PhotoImage(file="8.png")
        canvas.create_image(cx, cy, image=tori, tag="kokaton")

    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)

    if cx == ex and cy == ey:
        label = tk.Label(root, text="おいしい!!", font=("", 100), fg="red")
        label.pack()

    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    label0 = tk.Label(root, text="こうかとんはりんごが食べたい", font=("", 20), fg="black")
    label0.pack()

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    #print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="0.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    ex, ey = mx*1500-150, my*900-150
    get = tk.PhotoImage(file="apple.PNG")
    canvas.create_image(ex, ey, image=get, tag="kokaton")


    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    
    root.mainloop()