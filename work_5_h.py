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
str_list = ["明日は雨", "今日はいい天気"]
num = random.randint(0, len(str_list) - 1)
text = str_list[num]


def type():
    global text, num
    if text == entry1.get():
        num = random.randint(0, len(str_list) - 1)
        text = str_list[num]
        label1.config(text=text)
        entry1.delete(0, tk.END)


# 出力ラベルの作成
label1 = tk.Label(window, text=text, bg=bg_color, fg=fg_color)
label1.pack(pady=10)


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)


button1 = tk.Button(window, text="回答", command=type)
button1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
