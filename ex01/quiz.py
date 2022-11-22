import random
import datetime

def Q(q_lst):
    qes = random.choice(q_lst)
    print("問題：" + qes["q"])
    return qes["a"]

def A(a_lst):
    st = datetime.datetime.now()
    ans =input("答えるんだ：")
    ed = datetime.datetime.now()
    if ans in a_lst:
        print("正解！")
    else:
        print("出直してこい") 

    print("所要時間：" + str((ed-st).seconds) )

if __name__ == "__main__" :
    q_lst = [
        {"q":"ルフィの食べた悪魔の実は？", "a":["ゴムゴムの実", "ゴムゴム", "ごむごむ"]},
        {"q":"バギーの食べた悪魔の実は？", "a":["バラバラの実", "バラバラ", "ばらばら"]},
        {"q":"黒ひげの食べた悪魔の実は？", "a":["ヤミヤミの実", "ヤミヤミ", "やみやみ"]}
    ]

    a_lst = Q(q_lst)
    A(a_lst)