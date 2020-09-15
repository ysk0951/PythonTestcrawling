'''
scrpaing : 정보를 추출하는 기술
crawling : 정기적으로 돌며 정부를 추출하는 기술
크롤러 : 알고리즘에 의해 인터넷을 탐색하는 프로그램

#웹구조
클라이언트 : 서비스 요청 프로그램. 웹브라우저
서버 : 서비스를 제공해주는 프로그램.

클라이언트가 서버에 데이터를 요청할때 크게 4가지 타입으로 나뉜다 CRUD
클라이언트와 서버는 CRUD 요청을, 헤더에 다른 키워드로 메서드르 정의함.

C > Post
R > Get
U > Put
D > Delete

#Header
요청헤더 : 클라이언트 -> 서버 요청할때 정보 포함된 헤더
    User-Agent(브라우저 정보),Method(요청 메서드),refered(요청 이전에 머물렀던 정보)
응답헤더 : 서버 -> 클라이언트 헤더
    Status-code(응답 코드)
일반헤더 : 양측에서 모두 사용되는 일반 정보 포함한 헤더
엔티티 : 메세지에 해당하는 정보를 포함한 헤더
        Content - type(entity-body의 미디어 타입)

#데이터 전송
리소스 경로 : REST API
쿼리스트링 : URL 뒤에

#웹페이지
HTML : 문서구조, 내용물을 넣기위한 언어
CSS : 문서에 디자인을 추가 하기 위한 언어
Javascript : 웹페이지에 기능을 추가 위한 언어(동적 효과)

##라이브러리
urllib : URL을 다루는 모듈패키지
    HTTP FTP 를 사용하여 데이터 다운가능
    urllib,request모듈은 웹사이트에 있는 데이터 접근하느 ㄴ기능을 제공함
    인증, 리다이렉트, 쿠키 같은 요청과 처리를 지원
'''

#라이브러리 임포트
from urllib.request import Request,urlopen
#요청
url = "https://www.naver.com"
req = Request(url)
page = urlopen(req)
#응답결과 출력
# print(page)
# print(page.code)
# print("="*50)
# print(page.headers)
# print("="*50)
# print(page.url)
# print(page.info().get_content_charset())
# print("="*50)
#html 꺼내기 : read() 함수 이용, html을 바이너리 형태로 가져옴
# print(page.read())

#Post요청
import urllib
data = {"key1":"value1","key2":"value2"}
data = urllib.parse.urlencode(data)#딕셔너리를 쿼리스트링 형태로 변환
data = data.encode("utf-8")
req_post = Request(url,data=data,headers={})
page = urlopen(req_post)
print(page)
print(page.url)

#Get요청
req_get = Request(url+"?key1=value1&key2=value2",None,headers={})
page = urlopen(req_get)
print(page)
print(page.url)

#파일다운로드
from urllib.request import urlretrieve
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
#저장할 이미지 경로 + 이름 : 파일 확장자 동일하게
name = "googleLogo.png"
#다운받기 : urlretrleve(다운받을데이터의 url, 저장할 파일경로_
urlretrieve(url,name)