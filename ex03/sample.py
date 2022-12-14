import tkinter as tk
import tkinter.messagebox as tkm


def count_up():
    global tmr
    global jid

    label["text"] = tmr
    tmr = tmr+1
    jib = root.after(1000, count_up)


def key_down(event):
    global jid

    if jib is not None:  #カウントアップ中にキーが押されたら
        root.after_cancel(jid)
        jib = None

    key = event.keysym
    jid = root.after(1000, count_up)
    #root.after(1000, count_up)
    tkm.showinfo("キー押下", f"{key}キーが押されました")


if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text="-", font=("", 80))
    label.pack()

    tmr = 0
    jid = None
    #count_up()
    root.bind("<KeyPress>", key_down)

    root.mainloop()

    
    