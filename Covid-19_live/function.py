import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import webbrowser

# 정보 가져오는 함수 
# 코로나 라이브에서 도저히 데이터를 가져올 수 없었다. 이 프로젝트는 여기까지.
url = "https://corona-live.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
str_num = soup.find("div", attrs={"class":"Layout__SBox-dxfASU"})
print(str_num)

# 어제 확진자 수 가져오는 함수
y_url = "http://ncov.mohw.go.kr/"
y_res = requests.get(y_url)
y_res.raise_for_status()

y_soup = BeautifulSoup(y_res.text, "lxml")
y_num = y_soup.find("span", attrs={"class":"data"}).get_text()
discount = int(y_num.replace(",",""))
print(discount)

