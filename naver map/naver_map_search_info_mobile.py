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
    print("지도에 검색할 단어를 입력하시오 >")
    searchText = input()

    map_url = 'https://map.naver.com/search2/search.nhn?query='+searchText

    driver_path = 'C:/Users/kshzg/_development/chromedriver'

    headers = 'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=828x1792')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument(headers)

    driver = webdriver.Chrome(driver_path, options=options)

    driver.get(map_url)
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3];},});")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    driver.implicitly_wait(5)
    time.sleep(1)



    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    names = soup.select(
        '#ct > div.search_listview._content._ctList > ul > li > div.item_info > a.a_item.a_item_distance._linkSiteview > div > strong'
        )
    addresses = soup.select(
        '#ct > div.search_listview._content._ctList > ul > li > div.item_info > div.wrap_bx_address._addressBox > div > p:nth-child(1)'
        )
    tels = soup.select(
        '#ct > div.search_listview._content._ctList > ul > li'
        )
    search_info_list = []

    for i in range(len(names)):
        search_info_list.append([names[i]. text,addresses[i].text, tels[i].get('data-tel')])


    data = pd.DataFrame(search_info_list)
    data.columns = ['업체명', '주소', '전화번호']
    data.head()

    print("파일명 입력 >")
    save_name = input()

    data.to_csv(save_name+'.csv', encoding='cp949')
    driver.quit()
    print()
    print('검색 결과 저장 완료 ('+os.getcwd()+'\\'+save_name+'.csv)')
    print()
    
    isProcess = 'p'
    while isProcess is not 'y' and isProcess is not 'n' :
        print("계속 진행할거면 y, 종료할거면 n")
        isProcess = input()
    if isProcess is 'n':
        break