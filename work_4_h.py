import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

# 名簿リストの作成。ここに名前を追加していく
name_list = []


# TODO 5. ボタンを押すと名前を追加してラベルに表示する関数を作成
# Pythonで改行する文字は→”\n” (“エミリー\nマック\nジョン\n”)
def names():
    name = ""
    name_out = ""
    name = entry1.get()
    name_list.append(name)
    for i in name_list:
        # print(i)
        name_out += f"{i}\n"
    label2.config(text=name_out)


def select():
    name_num = random.randint(0, len(name_list) - 1)
    label3.config(text=name_list[name_num])


# TODO 1. ラベル: 名前を入力してください
# 出力ラベルの作成
label1 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# TODO 2. エントリー: 名前を入力するための入力フィールド
# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# TODO 3. ボタン: ボタンを押すと配列に名前が追加される
button1 = tk.Button(window, text="追加", command=names)
button1.pack(pady=10)

# TODO 4. ラベル: 配列に追加された名前を表示する
# 出力ラベルの作成
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)


# ランダム選択
button2 = tk.Button(window, text="ランダム", command=select)
button2.pack(pady=10)

# 出力ラベルの作成
label3 = tk.Label(window, text="ランダム", bg=bg_color, fg=fg_color)
label3.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
