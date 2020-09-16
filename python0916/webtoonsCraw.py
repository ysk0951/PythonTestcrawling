# 네이버 웹툰 긁기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
html = requests.get(url)
soup = BeautifulSoup(html.text,'lxml')

# data = soup.find('div',{'class':'col_inner'}) # 월요일 기둥
# img_tag = data.find_all('img') #월요일의 모든 이미지 태그
# print(len(img_tag))            #월요일 만화갯수

# mon_title_list = []
# mon_img_list = []
# for i in img_tag:
#     mon_title_list.append(i.get('title'))
#     mon_img_list.append(i.get('src'))
#
# print(mon_img_list)
# print(mon_title_list)

#전체 리스트
data = soup.find_all('div',{'class':'col_inner'}) #기둥
daily_title = []
daily_img = []

for i in data :
    img_tags = i.find_all('img')
    title_list = []
    img_list=[]
    for j in img_tags:
        title_list.append(j.get('title'))
        img_list.append(j.get('src'))
    daily_title.append(title_list)
    daily_img.append(img_list)

print(daily_title)
print(daily_img)


#썸네일 이미지 저장
from urllib.request import urlretrieve
import os,errno, re
#저장할 폴더 생성
'''
OS 에서 작업해야할 경우
파이썬에서 제공하는 OS 패키지 import 하기.
os.path.isdir : 이미지 디렉토리가 있는지 검사
os.path.join : 현재 경로를 계산하여 입력으로 들어온
                텍스트를 합하여 새로운 경로 만듬
os.makedirs : 경로에 폴더생성

'''
try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.error != errno.EEXIST:


