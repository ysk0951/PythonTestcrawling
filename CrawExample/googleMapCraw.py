from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.co.kr/maps')
time.sleep(3)
driver.find_element_by_name('q').send_keys('서울대 입구 맛집')
driver.find_element_by_id('searchbox-searchbutton').click()
time.sleep(3)
# copy xpath //div[@data-result-index="1"]
# result = driver.find_element_by_xpath('//div[@data-result-index="1"]')
# print(result.text)
# time.sleep(3)

data = []
for i in range(1,21):
    driver.implicitly_wait(3)
    data_result = driver.find_element_by_xpath('//div[@data-result-index="%d"]'%i)
    data_result.click()
    driver.implicitly_wait(3)
    #썸네일 정보 가져오기
    try:
        title = driver.find_element_by_xpath('//div[@class="section-hero-header-title-description"]')
        print(title.text)
    except Exception:
        pass
    # 주소 가져오기
    # <button aria-label="주소: 서울특별시 관악구 봉천동 남부순환로226길 36 2층 " data-item-id="address" data-tooltip="주소 복사" ved="1i:0,t:36622,e:9,p:GbphX8XiBtHQ-gSgu5ho:98" jsaction="pane.wfvdle15;clickmod:pane.wfvdle15;focus:pane.focusTooltip;blur:pane.blurTooltip" jstcache="981" class="ugiz4pqJLAG__button" jsan="7.ugiz4pqJLAG__button,0.aria-label,0.data-item-id,0.data-tooltip,0.ved,0.jsaction,t--fmfwOkA_6s"><div jstcache="996" class="ugiz4pqJLAG__content"> <div jstcache="986" class="ugiz4pqJLAG__icon-container" jsan="7.ugiz4pqJLAG__icon-container,t-DLjTl110KM4"> <div jstcache="993" class="ugiz4pqJLAG__icon-outer" jsan="7.ugiz4pqJLAG__icon-outer"> <img role="presentation" jstcache="994" src="//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png" class="ugiz4pqJLAG__icon" jsan="7.ugiz4pqJLAG__icon,0.role,8.src"> </div> </div> <div aria-hidden="false" jstcache="987" class="ugiz4pqJLAG__text" jsan="7.ugiz4pqJLAG__text,0.aria-hidden"> <div jstcache="988" class="ugiz4pqJLAG__primary-text gm2-body-2" jsan="7.ugiz4pqJLAG__primary-text,7.gm2-body-2" style="font-family: Roboto, &quot;Noto Sans KR&quot;, Arial, sans-serif;">서울특별시 관악구 봉천동 남부순환로226길 36 2층</div> <div jstcache="989" style="display:none"></div> <div jstcache="990" style="display:none"></div> <div jstcache="991" class="ugiz4pqJLAG__secondary-text gm2-caption section-listitem-description" jsan="7.ugiz4pqJLAG__secondary-text,7.gm2-caption,7.section-listitem-description" style="font-family: Roboto, &quot;Noto Sans KR&quot;, Arial, sans-serif;"> </div> </div> </div><div jstcache="997" style="display:none"></div></button>
    try:
        add = driver.find_element_by_xpath('//button[@data-item-id="address"]')
        print("주소",add.text)
    except Exception:
        pass
    # 전화번호 가져오기
    # <button aria-label="전화: 02-873-5164 " data-item-id="phone:tel:+8228735164" data-tooltip="전화번호 복사" ved="1i:0,t:18491,e:12,p:GbphX8XiBtHQ-gSgu5ho:101" jsaction="pane.wfvdle17;clickmod:pane.wfvdle17;focus:pane.focusTooltip;blur:pane.blurTooltip" jstcache="981" class="ugiz4pqJLAG__button" jsan="7.ugiz4pqJLAG__button,0.aria-label,0.data-item-id,0.data-tooltip,0.ved,0.jsaction,t--fmfwOkA_6s"><div jstcache="996" class="ugiz4pqJLAG__content"> <div jstcache="986" class="ugiz4pqJLAG__icon-container" jsan="7.ugiz4pqJLAG__icon-container,t-DLjTl110KM4"> <div jstcache="993" class="ugiz4pqJLAG__icon-outer" jsan="7.ugiz4pqJLAG__icon-outer"> <img role="presentation" jstcache="994" src="//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png" class="ugiz4pqJLAG__icon" jsan="7.ugiz4pqJLAG__icon,0.role,8.src"> </div> </div> <div aria-hidden="false" jstcache="987" class="ugiz4pqJLAG__text" jsan="7.ugiz4pqJLAG__text,0.aria-hidden"> <div jstcache="988" class="ugiz4pqJLAG__primary-text gm2-body-2" jsan="7.ugiz4pqJLAG__primary-text,7.gm2-body-2" style="font-family: Roboto, &quot;Noto Sans KR&quot;, Arial, sans-serif;">02-873-5164</div> <div jstcache="989" style="display:none"></div> <div jstcache="990" style="display:none"></div> <div jstcache="991" class="ugiz4pqJLAG__secondary-text gm2-caption section-listitem-description" jsan="7.ugiz4pqJLAG__secondary-text,7.gm2-caption,7.section-listitem-description" style="font-family: Roboto, &quot;Noto Sans KR&quot;, Arial, sans-serif;"> </div> </div> </div><div jstcache="997" style="display:none"></div></button>
    try:
        tel = driver.find_element_by_xpath('//button[@data-tooltip="전화번호 복사"]')
        print("전화번호",tel.text)
    except Exception:
        pass
    # 웹 사이트 가져오기
    # <button aria-label="웹사이트: naturekitchen.co.kr " data-item-id="authority" data-tooltip="웹사이트 열기" ved="1i:0,t:3443,e:12,p:GbphX8XiBtHQ-gSgu5ho:415" jsaction="pane.wfvdle116;clickmod:pane.wfvdle116;focus:pane.focusTooltip;blur:pane.blurTooltip" jstcache="981" class="ugiz4pqJLAG__button" jsan="7.ugiz4pqJLAG__button,0.aria-label,0.data-item-id,0.data-tooltip,0.ved,0.jsaction,t--fmfwOkA_6s"><div jstcache="996" class="ugiz4pqJLAG__content"> <div jstcache="986" class="ugiz4pqJLAG__icon-container" jsan="7.ugiz4pqJLAG__icon-container,t-DLjTl110KM4"> <div jstcache="993" class="ugiz4pqJLAG__icon-outer" jsan="7.ugiz4pqJLAG__icon-outer"> <img role="presentation" jstcache="994" src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png" class="ugiz4pqJLAG__icon" jsan="7.ugiz4pqJLAG__icon,0.role,8.src"> </div> </div> <div aria-hidden="false" jstcache="987" class="ugiz4pqJLAG__text ugiz4pqJLAG__underline_on_hover" jsan="7.ugiz4pqJLAG__text,7.ugiz4pqJLAG__underline_on_hover,0.aria-hidden"> <div jstcache="988" class="ugiz4pqJLAG__primary-text gm2-body-2" jsan="7.ugiz4pqJLAG__primary-text,7.gm2-body-2" style="font-family: Roboto, &quot;Noto Sans KR&quot;, Arial, sans-serif;">naturekitchen.co.kr</div> <div jstcache="989" style="display:none"></div> <div jstcache="990" style="display:none"></div> <div jstcache="991" class="ugiz4pqJLAG__secondary-text gm2-caption section-listitem-description" jsan="7.ugiz4pqJLAG__secondary-text,7.gm2-caption,7.section-listitem-description" style="font-family: Roboto, &quot;Noto Sans KR&quot;, Arial, sans-serif;"> </div> </div> </div><div jstcache="997" style="display:none"></div></button>
    try:
        web = driver.find_element_by_xpath('//button[@data-item-id="authority"]')
        print("Web",web.text)
    except Exception:
        pass

    ## 뒤로 돌아가기
    #<button jstcache="1388" ved="1i:1,t:10452,e:0,p:BcFhX5WiE-Tv9APJpKToAw:380" jsaction="pane.place.backToList" class="section-back-to-list-button blue-link noprint" jsan="t-MoXyWTerhiw,7.section-back-to-list-button,7.blue-link,7.noprint,0.ved,0.jsaction"> <span jstcache="892">검색결과로 돌아가기</span> </button>
    back_btn = driver.find_element_by_xpath('//button[@jsaction="pane.place.backToList"]')
    back_btn.click()
    #뒤로가기 = dirver.back()
