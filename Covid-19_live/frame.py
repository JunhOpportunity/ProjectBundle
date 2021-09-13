import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("Today Covid-19 Live")
root.geometry("400x150")
# root.configure(bg="#856ff8")

# 확진자 수 프레임
number = 0

number_frame = LabelFrame(root, text="확진자 수")
number_frame.pack()
fontStyle = tkFont.Font(family="Arial", size=30)
number_label = Label(number_frame, width = 10, text="{}".format(number), font=fontStyle, bg="white", fg="red")
number_label.pack(padx=10, pady=10)


# 버튼 두 개 프레임
button_frame = LabelFrame(root, text="새로고침 / 주소")
button_frame.pack()
refresh_button = Button(button_frame, text="새로고침", bg="#87cefa")
refresh_button.pack(side="left", padx=4, pady=4)
address_button = Button(button_frame, text="주소", bg="#da70d6")
address_button.pack(side="right", padx=4, pady=4)


root.resizable(False, False) # 창 크기 변경 불가
root.mainloop()