import requests
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
# today_am_cloud = soup.find("span", attrs={"class":"rainfall"})
# today_am_next = today_am_cloud.next_element
# print(today_am_cloud.get_text())
# print(today_am_next.get_text())

# cloud_list = soup.find_all("div", attrs={"class":"rainfall"})
# print(cloud_list[1].get_text())
cloud_list = soup.find_all("span", class_="rainfall")
print(cloud_list[0].text)
print(cloud_list[1].text)

# 강수 확률 맨 뒤에 % 나오는 경우 % 없애는 방법 연구
print(type(cloud_list[0].text))
cl = cloud_list[0].text
print(cl[2])
clm = cl[:2]
print(clm) # 해결!

# 내일, 내일 모레 기온 스크래핑
temp_high_list = soup.find_all("span", class_="highest")
print("DD")
print(temp_high_list[1].text.replace("최고기온", ""))
print(temp_high_list[2].text.replace("최고기온", ""))

temp_low_list = soup.find_all("span", class_="lowest")
print(temp_low_list[1].text.replace("최저기온",""))
print(temp_low_list[2].text.replace("최저기온",""))

# 새로고침 버튼 구동 함수
def refresh():
    new_live_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재 온도", "")
    temperture_now.config(text="{}".format(new_live_temp))
