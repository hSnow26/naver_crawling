#
# verseino 1.0.0
# Author: soel <kshzg@naver.com>
#
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utility.basic_utility import BasicUtility
from utility.file_utility import FileUtility
from const.naver_crawling_const import NaverCrawlingConst
import pandas as pd


basicUtil = BasicUtility()
fileUtil = FileUtility()
while True :
    headers = {'User-Agent': NaverCrawlingConst.HEADER_WINDOW_CHROME}

    print(NaverCrawlingConst.SEARCH_KEYWORD_QUESTION)
    searchTexts = input()
    print(NaverCrawlingConst.FIND_RANK_QUESTION)
    keyword = input()

    searchCount = basicUtil.getSearchCount(NaverCrawlingConst.RANK_RANGE_QUESTION)
    splitCount = basicUtil.getSplitCount(searchCount, NaverCrawlingConst.LIST_SPLIT_COUNT)
    searchTextList = searchTexts.split(',')
    dataFrame = []
    for searchText in searchTextList:
        viewInfoList = []
        searchCounting=0

        searchText = searchText.strip() #양쪽 공백 제거
        
        print("\n검색어 : "+searchText)
        #검색한 VIEW 리스트
        for i in range(splitCount):
            startNum = str(i * NaverCrawlingConst.LIST_SPLIT_COUNT + 1)
            searchUrl = basicUtil.getSearchUrl(searchText
                                                ,startNum
                                                ,NaverCrawlingConst.SEARCH_URL
                                                ,NaverCrawlingConst.VIEW_SEARCH_URL)

            soup = basicUtil.getSoup(searchUrl, headers)

            viewContents = soup.select(NaverCrawlingConst.VIEW_CONTENT_LIST_SELECTOR)
            viewDates = soup.select(NaverCrawlingConst.VIEW_DATE_LIST_SELECTOR)

            for i in range(NaverCrawlingConst.LIST_SPLIT_COUNT):
                searchCounting += 1
                if(searchCounting>searchCount):
                    break
                print(str(searchCounting)+'. 제목: '+viewContents[i].text+', URL: '+viewContents[i].get('href')+ 'Date: '+viewDates[i].text)
                viewInfoList.append([viewContents[i].get('href'), viewContents[i].text, viewDates[i].text])
        print()
        counting=0
        #담은 리스트 들에서 키워드 검색
        resultList = []
        for viewInfo in viewInfoList:
            counting += 1
            url = viewInfo[0] #url
            title = viewInfo[1] #title
            soup = basicUtil.getSoup(url, headers)

            if (basicUtil.isExistKeywordResult(url, soup, title, keyword)):
                print(str(counting)+": "+str(viewInfo[2]))
                resultList.append(viewInfo[2]) #date
            else:
                print(str(counting))
                resultList.append('')
        print()
        dataFrame.append(pd.DataFrame({searchText : resultList})) #컬럼별 데이터 추가

    resultDataFrame = dataFrame[0]
    for i in range(len(searchTextList)):
        if(i+1<len(searchTextList)):
            resultDataFrame = pd.concat([resultDataFrame, dataFrame[i+1]], axis=1)
    fileUtil.makeDataFrametoCsv(resultDataFrame)

    if(basicUtil.isProgramEnd()):
        break