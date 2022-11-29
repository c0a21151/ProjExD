import tkinter as tk
import tkinter.messagebox as tkm


# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    siki = entry.get() # 数式の文字列
    if num == "=":
        siki = siki.replace("×", "*")
        siki = siki.replace("÷", "/")
        res = eval(siki) # 数式文字列の評価
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
    elif num == "+/-": #プラスマイナス変換
        entry.insert(tk.END, "-")
    elif num == ".": #浮動小数点の追加
        f =siki[-1]
        if f == ".": #連続で押しても挿入されない
            pass
        else:
            #i = siki.rfind(".")
            entry.insert(tk.END, num)

    elif num == "AC": #オールクリア
        entry.delete(0, tk.END) 
    elif num == "C": #クリア
        entry.delete(0, tk.END) 
        siki =siki[:-1]
        entry.insert(tk.END, siki)
    else: # 「=」以外のボタン字
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

    
# 練習１
root = tk.Tk()
root.geometry("400x600")

# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

# 練習２
r, c = 1, 0
nums = ["C", "AC", " ", "÷", 7, 8, 9, "×", 4, 5, 6, "-", 1, 2, 3, "+", "+/-", 0, ".", "="]
for num in nums:
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%4 == 0:
        r += 1
        c = 0
    

root.mainloop()
