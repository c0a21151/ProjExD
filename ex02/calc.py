import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("", f"[{num}]ボタンがクリックされました")

root = tk.Tk()
root.title("電卓基本機能")
root.geometry("300x500")

r, c = 0, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=str(num), width="4", height="2", font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c =0

root.mainloop()