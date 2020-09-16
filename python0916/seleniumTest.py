'''
# 셀레늄 사용
1. 파일참에 selenium 모듈 추가
2. 크롬브라우저 버전에 맞는 크롬 드라이버 다운

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#드라이버 경로
driver = webdriver.Chrome('chromedriver.exe')
#webdriver.Ie('IEDriverServer.exe')
#webdriver.Firefox('FirefoxDriver.exe') 내장형

# url = "http://www.naver.com"
# driver.get(url)

#실행시간 중간에 멈추기
# time.sleep(1)
import time

'''
selenium으로 브라우저 Dom에 접근
# 리턴 타입 find
find_element_by_id
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
find_element_by_xpath               : xml문서 접근하기 위한 문법
find_element_by_link_text           : a 태그의 href 속성값을 이용
find_element_by_partial_link)text
find_element_by_name
# 리턴 타입 find all
find_elements_by_id
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
find_elements_by_xpath              : xml문서 접근하기 위한 문법
find_elements_by_link_text          : a 태그의 href 속성값을 이용
find_elements_by_partial_link)text
find_elements_by_name

#xpath : XML Path Language
W3C표준으로 XML문서의 구조를 통해 경로에 지정한 구문을 사용하여,
항목을 배치하고 처리하느 ㄴ언어

/ : 절대경로
// : 문서 내에서 검색
//@href : herf속성이 있는 모든 태그
//a[@href ='http//google.com']
(//a)[3] : 문서 내에서 세번째 위치하는 a 태그
(//table)[last()] 
(//a)[position() < 3] : 문서 내에서 처음 두개의 a 태그
//table/tr/*
//div[@*]
'''

url = "https://www.youtube.com/"
driver.get(url)
driver.implicitly_wait(3)

search = driver.find_element_by_xpath('//input[@id="search"]')
driver.implicitly_wait(3)
search.send_keys('펭수')#검색할 키워드 던지기
search.send_keys(Keys.ENTER)
driver.implicitly_wait(3)
# #more > yt-formatted-string 더보기 클릭하여 펼치기
more = driver.find_element_by_css_selector('#more > yt-formatted-string')
more.click()

#타이틀
# #video-title > yt-formatted-string
# titles = driver.find_elements_by_css_selector('#video-title > yt-formatted-string')
# for t in titles:
#     print(t.text)

#동영상 링크
# #thumbnail
thumbnails = driver.find_elements_by_css_selector("#thumbnail")
for thumb in thumbnails:
    print(thumb.get_attribute('href'))