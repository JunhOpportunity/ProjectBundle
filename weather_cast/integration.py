import requests
from bs4 import BeautifulSoup
import time
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import tkinter.font as tkFont

# 스크래핑
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 내일, 내일모레 최고 온도&최저 온도
temp_high_list = soup.find_all("span", class_="highest")
temp_low_list = soup.find_all("span", class_="lowest")

# 현재 온도
live_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도", "") # replace를 통해 제거하고싶은 내용 제거


# 오늘 최고온도 최저온도
today_lowest_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
today_highest_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")


# 오늘 오전 오후 구름 양
cloud_list = soup.find_all("span", class_="rainfall")
today_am_c = cloud_list[0].text
today_pm_c = cloud_list[1].text
tomorrow_am_c = cloud_list[2].text
tomorrow_pm_c = cloud_list[3].text
aft_tomorrow_am_c = cloud_list[4].text
aft_tomorrow_pm_c = cloud_list[5].text

# 새로고침 버튼 함수
def refresh():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    new_live_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도", "")
    temperture_now.config(text="{}".format(new_live_temp))
    print("새로고침")

####################################################################


root = Tk()
root.title("Weather Cast!")
root.geometry("320x310")

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
tem_now = live_temp
temperture_font = tkFont.Font(family="", size=20)
temperture_now = Label(now_frame, text="{}".format(tem_now), bg="white", fg="blue",font=temperture_font)
temperture_now.pack(padx=5, pady=5)

# 오늘 최고 온도 & 최저 온도 & 오전 구름 & 오후 구름
today_max_tem = today_highest_temp
today_min_tem = today_lowest_temp
today_am_cloud = today_am_c
today_pm_cloud = today_pm_c
# 온도
today_etc_frame = LabelFrame(today_frame, text="ETC")
today_etc_frame.pack(side="right")
max_min_tem_label = Label(today_etc_frame, text="Temperture MIN : {}ºC | MAX : {}ºC".format(today_min_tem, today_max_tem))
# 구름
cloud_label = Label(today_etc_frame, text="Cloud AM : {} | PM : {}".format(today_am_cloud, today_pm_cloud))

max_min_tem_label.pack(padx=5)
cloud_label.pack(padx=5)

# 달 관측 가능한가?
# 9/22 today_pm_c_m 은 today_pm_c를 인덱스 0부터 1까지 자른 것인데, today_pm_c이 0% 또는 100%가 나올 경우 오류가 발생하기 때문에 코드를 수정하였다.
today_pm_c_m = today_pm_c[:2]
if (today_pm_c == "0%"):
    moon_answer_icon = "◎"
elif(today_pm_c == "100%" ):
    moon_answer_icon = "Ｘ"
elif(int(today_pm_c_m) <= 30 ):
    moon_answer_icon = "◎"
elif (int(today_pm_c_m) & int(today_pm_c_m) <=60):
    moon_answer_icon = "△"
elif (int(today_pm_c_m) > 60 ):
    moon_answer_icon = "Ｘ"

moon_frame = LabelFrame(root, text="Can We Observe the Moon?")
moon_frame.pack(pady=10)
moon_answer = Label(moon_frame, text="Answer : {}  (◎/△/Ｘ)".format(moon_answer_icon))
moon_answer.pack(padx=76)

# 날씨 요약
summery_frame = LabelFrame(root, text="Summary")
summery_frame.pack(pady=10)
# 오늘
summery_today_w_frame = LabelFrame(summery_frame, text="Today")
summery_today_w_frame.pack(side="left")
s_t_am_c = Label(summery_today_w_frame, text="Am Cloud : {}".format(today_am_cloud))
s_t_pm_c = Label(summery_today_w_frame, text="Pm Cloud : {}".format(today_pm_cloud))
s_t_t = Label(summery_today_w_frame, text="{}ºC/{}ºC".format(today_min_tem, today_max_tem))
s_t_am_c.pack()
s_t_pm_c.pack()
s_t_t.pack()
# 내일
tomorrow_am_cloud = tomorrow_am_c
tomorrow_pm_cloud = tomorrow_pm_c
tom_min_tem = temp_low_list[1].text.replace("최저기온", "")
tom_max_tem = temp_high_list[1].text.replace("최고기온", "")
summery_tomorrow_w_frame = LabelFrame(summery_frame, text="Tomorrow")
summery_tomorrow_w_frame.pack(side="left")
s_tom_am_c = Label(summery_tomorrow_w_frame, text="Am Cloud : {}".format(tomorrow_am_cloud))
s_tom_pm_c = Label(summery_tomorrow_w_frame, text="Pm Cloud : {}".format(tomorrow_pm_cloud))
s_tom_t = Label(summery_tomorrow_w_frame, text="{}ºC/{}ºC".format(tom_min_tem, tom_max_tem))
s_tom_am_c.pack()
s_tom_pm_c.pack()
s_tom_t.pack()
#모레
aft_tomorrow_am_cloud = aft_tomorrow_am_c
aft_tomorrow_pm_cloud = aft_tomorrow_pm_c
aft_tom_min_tem = temp_low_list[2].text.replace("최저기온", "")
aft_tom_max_tem = temp_high_list[2].text.replace("최고기온", "")
summery_aft_tomorrow_w_frame = LabelFrame(summery_frame, text="After Tomorrow")
summery_aft_tomorrow_w_frame.pack(side="left")
s_a_t_am_c = Label(summery_aft_tomorrow_w_frame, text="Am Cloud : {}".format(aft_tomorrow_am_cloud))
s_a_t_pm_c = Label(summery_aft_tomorrow_w_frame, text="Pm Cloud : {}".format(aft_tomorrow_pm_cloud))
s_a_t_t = Label(summery_aft_tomorrow_w_frame, text="{}ºC/{}ºC".format(aft_tom_min_tem, aft_tom_max_tem))
s_a_t_am_c.pack()
s_a_t_pm_c.pack()
s_a_t_t.pack()

refresh_button = Button(root, text="Refresh", command=refresh, bg="cornflowerblue")
refresh_button.pack()

root.resizable(False, False)
root.mainloop()

