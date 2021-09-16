import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("Weather Cast!")
root.geometry("320x300")

# # 맨 위 타이틀 만들기
# title_font = tkFont.Font(size=20)
# title_label = Label(root, text="일기 예보입니다~!", font=title_font)
# title_label.pack(padx=5, pady=5)

# 맨 위 오늘 날씨 프레임
today_frame = LabelFrame(root, text="Today Weather")
today_frame.pack(pady=10)

# 현재 온도
now_frame = LabelFrame(today_frame, text="LIVE")
now_frame.pack(side="left")
tem_now = 0
temperture_font = tkFont.Font(family="", size=20)
temperture_now = Label(now_frame, text="{}".format(tem_now), bg="white", fg="blue",font=temperture_font)
temperture_now.pack(padx=5, pady=5)

# 오늘 최고 온도 & 최저 온도 & 오전 구름 & 오후 구름
today_max_tem = 0
today_min_tem = 0
today_am_cloud = 0
today_pm_cloud = 0
# 온도
today_etc_frame = LabelFrame(today_frame, text="ETC")
today_etc_frame.pack(side="right")
max_min_tem_label = Label(today_etc_frame, text="Temperture MAX : {}ºC | MIN : {}ºC".format(today_max_tem, today_min_tem))
# 구름
cloud_label = Label(today_etc_frame, text="Cloud AM : {}% | PM : {}%".format(today_am_cloud, today_pm_cloud))

max_min_tem_label.pack(padx=5)
cloud_label.pack(padx=5)

# 달 관측 가능한가?
if (today_pm_cloud <= 30):
    moon_answer_icon = "◎"
elif (today_pm_cloud > 30 & today_pm_cloud <=60):
    moon_answer_icon = "△"
elif (today_pm_cloud > 60):
    moon_answer_icon = "Ｘ"

moon_frame = LabelFrame(root, text="Can We Observe the Moon?")
moon_frame.pack(pady=10)
moon_answer = Label(moon_frame, text="Answer : {}(◎/△/Ｘ)".format(moon_answer_icon))
moon_answer.pack(padx=76)

# 날씨 요약
summery_frame = LabelFrame(root, text="Summary")
summery_frame.pack(pady=10)
# 오늘
summery_today_w_frame = LabelFrame(summery_frame, text="Today")
summery_today_w_frame.pack(side="left")
s_t_am_c = Label(summery_today_w_frame, text="Am Cloud : {}%".format(today_am_cloud))
s_t_pm_c = Label(summery_today_w_frame, text="Pm Cloud : {}%".format(today_pm_cloud))
s_t_t = Label(summery_today_w_frame, text="{}ºC/{}ºC".format(today_min_tem, today_max_tem))
s_t_am_c.pack()
s_t_pm_c.pack()
s_t_t.pack()
# 내일
tomorrow_am_cloud = 1
tomorrow_pm_cloud = 1
tom_min_tem = 1
tom_max_tem = 1
summery_tomorrow_w_frame = LabelFrame(summery_frame, text="Tomorrow")
summery_tomorrow_w_frame.pack(side="left")
s_tom_am_c = Label(summery_tomorrow_w_frame, text="Am Cloud : {}%".format(tomorrow_am_cloud))
s_tom_pm_c = Label(summery_tomorrow_w_frame, text="Pm Cloud : {}%".format(tomorrow_pm_cloud))
s_tom_t = Label(summery_tomorrow_w_frame, text="{}ºC/{}ºC".format(tom_min_tem, tom_max_tem))
s_tom_am_c.pack()
s_tom_pm_c.pack()
s_tom_t.pack()
#모레
aft_tomorrow_am_cloud = 2
aft_tomorrow_pm_cloud = 2
aft_tom_min_tem = 2
aft_tom_max_tem = 2
summery_aft_tomorrow_w_frame = LabelFrame(summery_frame, text="After Tomorrow")
summery_aft_tomorrow_w_frame.pack(side="left")
s_a_t_am_c = Label(summery_aft_tomorrow_w_frame, text="Am Cloud : {}%".format(aft_tomorrow_am_cloud))
s_a_t_pm_c = Label(summery_aft_tomorrow_w_frame, text="Pm Cloud : {}%".format(aft_tomorrow_pm_cloud))
s_a_t_t = Label(summery_aft_tomorrow_w_frame, text="{}ºC/{}ºC".format(aft_tom_min_tem, aft_tom_max_tem))
s_a_t_am_c.pack()
s_a_t_pm_c.pack()
s_a_t_t.pack()


root.resizable(False, False)
root.mainloop()