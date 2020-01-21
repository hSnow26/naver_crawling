#
# verseino 1.0.0
# Author: seol <kshzg26@gmail.com>
# Find keyword in searched 'View' list
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
    queryCount = basicUtil.getSplitCount(searchCount, NaverCrawlingConst.LIST_SPLIT_COUNT)
    searchTextList = searchTexts.split(',')
    dataFrame = []
    for searchText in searchTextList:
        viewInfoList = []
        searchCounting=0

        searchText = searchText.strip() #Both side white space remove
        
        print("\n검색어 : "+searchText)
        #Searched list in VIEW
        for i in range(queryCount):
            startNum = str(i * NaverCrawlingConst.LIST_SPLIT_COUNT + 1)
            searchUrl = basicUtil.getSearchUrl(searchText
                                                ,startNum
                                                ,NaverCrawlingConst.SEARCH_URL
                                                ,NaverCrawlingConst.VIEW_SEARCH_URL)

            soup = basicUtil.getSoup(searchUrl, headers)

            viewContents = soup.select(NaverCrawlingConst.VIEW_CONTENT_LIST_SELECTOR)
            # viewDates = soup.select(NaverCrawlingConst.VIEW_DATE_LIST_SELECTOR)

            for viewContent in viewContents:
                searchCounting += 1
                if(searchCounting>searchCount):
                    break
                category = basicUtil.getCategory(viewContent.get('href'))
                print(str(searchCounting)+'. 제목: '+viewContent.text+', URL: '+viewContent.get('href')+ ', '+category)
                viewInfoList.append([viewContent.get('href'), viewContent.text, category])
        print()
        counting=0
        
        #Searching keyword in viewInfoList
        resultList = []
        topRankFlag = 0
        topRankNum = NaverCrawlingConst.OUT_OF_RANK
        for viewInfo in viewInfoList:
            counting += 1
            url = viewInfo[0] #url
            title = viewInfo[1] #title
            soup = basicUtil.getSoup(url, headers)

            if (basicUtil.isExistKeywordResult(url, soup, title, keyword)):
                print(str(counting)+": "+str(viewInfo[2]))
                resultList.append(viewInfo[2]) #category

                #top rank check
                if(topRankFlag is 0):
                    topRankNum = counting
                    topRankFlag = 1
            else:
                print(str(counting))
                resultList.append('')
        print()

        # resultList.insert(0, topRankNum) #foward append
        resultList.append(topRankNum) #foward append
        dataFrame.append(pd.DataFrame({searchText : resultList})) #Add data by column

    resultDataFrame = dataFrame[0]
    for i in range(len(searchTextList)):
        if(i+1<len(searchTextList)):
            resultDataFrame = pd.concat(dataFrame, axis=1)
            # resultDataFrame = pd.concat([resultDataFrame, dataFrame[i+1]], axis=1)
    
    startIndex = 1 # first value
    fileUtil.makeDataFrametoCsv(resultDataFrame, startIndex, len(resultList))

    if(basicUtil.isProgramEnd()):
        break