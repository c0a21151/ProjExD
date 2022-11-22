import random
import datetime

def moji():
    for i in range(t_num):
        n = random.choice(moji_lst)
        t_lst.append(n)
        moji_lst.remove(n)
    
    print("対象文字：")
    for i in t_lst:
        print(i, end=" ")
    print()

    for i in range(k_num):
        n = random.choice(t_lst)
        k_lst.append(n)
        t_lst.remove(n)

    print("欠損文字：")
    for i in k_lst:
        print(i, end=" ")
    print()

    print("表示文字：")
    for i in t_lst:
        print(i, end=" ")
    print()


def toi():
    num = input("欠損文字はいくつあるでしょうか？：")
    if num == len(k_lst):
        print("正解です.それでは,具体的に欠損文字を1つずつ入力してください")
        for i in range(num):
            ans = input(str(i) + "つ目の文字を入力してください：")
            if ans in k_lst:
                continue
            else:
                print("不正解です.またチャレンジしてください")
                break
        

if __name__ == "__main__":
    t_num = 10
    k_num = 2
    most_num = 3
    moji_lst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]
    t_lst = []
    k_lst = []

    for i in range(most_num):
        moji()
        print()
        toi()
        print("-" * 50)

