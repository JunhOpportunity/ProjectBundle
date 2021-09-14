import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import webbrowser
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import tkinter.font as tkFont

# 어제 확진자 수 가져오는 함수
y_url = "http://ncov.mohw.go.kr/"
y_res = requests.get(y_url)
y_res.raise_for_status()

y_soup = BeautifulSoup(y_res.text, "lxml")
y_num = y_soup.find("span", attrs={"class":"data"}).get_text()
discount = int(y_num.replace(",",""))

# 주소 button 함수(button)
def gotosite():
    webbrowser.open("https://corona-live.com/")


##################################################################
root = Tk()
root.title("Today Covid-19 Live")
# root.configure(bg="#856ff8")

# 어제 확진자 수 프레임
yesterday_frame = LabelFrame(root, text="어제 확진자 수")
yesterday_frame.pack()
y_font = tkFont.Font(family="Arial", size=10)
yesterday_number_label = Label(yesterday_frame, width = 10, text="{}".format(y_num), font=y_font, bg="white", fg="blue")
yesterday_number_label.pack()

# 실시간 확진자 수 프레임
number = 0

number_frame = LabelFrame(root, text="실시간 확진자 수")
number_frame.pack(padx=10, pady=10)
fontStyle = tkFont.Font(family="Arial", size=30)
number_label = Label(number_frame, width = 10, text="{}".format(number), font=fontStyle, bg="white", fg="red")
number_label.pack(padx=10, pady=10)


# 버튼 두 개 프레임
button_frame = LabelFrame(root, text="새로고침 / 주소")
button_frame.pack(pady=10)
refresh_button = Button(button_frame, text="새로고침", bg="#87cefa")
refresh_button.pack(side="left", padx=4, pady=4)
address_button = Button(button_frame, text="주소", bg="#da70d6", command=gotosite)
address_button.pack(side="right", padx=4, pady=4)


root.resizable(False, False) # 창 크기 변경 불가
root.mainloop()

# 정보 가져오는 함수 

# url = "https://corona-live.com/"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
# str_num = soup.find("div", attrs={"class":"Layout__SBox-dxfASU hVceBj Layout__SFlex-dGOlJW Xdeos Layout__SRow-jktCWH hwJbaK DomesticStats__StatDelta-dMwrmN enKfW"})
# print(str_num.get_text())


