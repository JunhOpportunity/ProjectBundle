import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 스크래핑
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 현재 온도
live_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도", "") # replace를 통해 제거하고싶은 내용 제거
print(live_temp)

# 오늘 최고온도 최저온도
today_lowest_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온","")
today_highest_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("최고기온","")
print(today_highest_temp, today_lowest_temp)

# 오늘 오전 오후 구름 양
today_am_cloud = soup.find("span", attrs={"class":"rainfall"})

print(today_am_cloud.get_text())

cloud_list = soup.find_all("div", attrs={"class":"rainfall"})
# with open("listFile.html", "w", encoding="utf8") as f:  # 내가 원하는 종류의 새로운 파일 생성
#     f.write(cloud_list.text)

