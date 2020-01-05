#
# version 1.0.0
# Author : soel <kshzg@naver.com>
#
# TODO
# pip install bs4  
# pip install lxml
# pip install selenium
# pip install pandas
#
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

while True :
    def change_page(driver, page_num):
        page_num = (str)(page_num)
        element = driver.find_element_by_xpath('/html/body/app/layout/div/div[2]/div[2]/shrinkable-layout/search-layout/search-list/search-list-contents/div/div[2]/a['+page_num+']')
        driver.execute_script("arguments[0].click();", element)
        return driver

    def get_info_list(current_page, total_page):
        def find_tel(tels):
            tel_start_index = tels[i].text.find('0')
            tel = '번호 없음' if tel_start_index == -1 else tels[i].text[tel_start_index:]
            return tel

        time.sleep(3)
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        names = soup.select(
            'body > app > layout > div > div.container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar > div > div.ps-content > div > div > div > search-item-place > div > div.search_box > div.title_box > strong > span.search_title_text'
            )
        addresses = soup.select(
            'body > app > layout > div > div.container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar > div > div.ps-content > div > div > div > search-item-place > div > div.search_box > div:nth-child(3) > span'
            )
        tels = soup.select(
            'body > app > layout > div > div.container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar > div > div.ps-content > div > div > div > search-item-place > div > div.search_box > div:nth-child(2)'
            )

        for i in range(len(names)):
            tel = find_tel(tels)
            # print('업체명 :'+names[i].text+ ', 주소:'+addresses[i].text+ ', 번호:'+tel)
            search_info_list.append([names[i].text,addresses[i].text, tel])
        
        print('loading...('+(str)(current_page)+'/'+(str)(total_page)+')')
        return search_info_list


    print("지도에 검색할 단어를 입력하시오 >")
    searchText = input()
    print()

    # map_url = 'https://map.naver.com/search2/search.nhn?query='+searchText
    map_url = 'https://map.naver.com/v5/search/'+searchText
    search_info_list = []
    total_page = 5

    driver_path = '/usr/local/bin/chromedriver'

    # headers = 'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    headers = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument(headers)

    driver = webdriver.Chrome(driver_path, options=options)

    driver.get(map_url)
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3];},});")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    driver.implicitly_wait(5)

    search_info_list = get_info_list(1, total_page)

    current_page=2 #default

    while current_page<6 :
        driver = change_page(driver, current_page)
        search_info_list = get_info_list(current_page, total_page)
        current_page+=1


    data = pd.DataFrame(search_info_list)
    data.columns = ['업체명', '주소', '전화번호']
    data.head()

    print()
    print("파일명 입력 >")
    save_name = input()

    data.to_csv(save_name+'.csv', encoding='cp949')
    driver.quit()
    print()
    print('검색 결과 저장 완료 (파일 경로 : '+os.getcwd())
    print()

    is_process = "p"
    while is_process != 'y' and is_process != 'n' :
        print("계속 진행할거면 y, 종료할거면 n")
        is_process = input()
    if is_process == 'n':
        break