#
# verseino 1.0.0
# Author: soel <kshzg@naver.com>
#
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utility.basic_utility import BasicUtility
from const.naver_crawling_const import NaverCrawlingConst


basicUtil = BasicUtility()
while True :
    headers = {'User-Agent': NaverCrawlingConst.HEADER_WINDOW_CHROME}

    print(NaverCrawlingConst.SEARCH_QUESTION)
    searchText = input()
    searchCount = basicUtil.getSearchCount(NaverCrawlingConst.RANK_RANGE_QUESTION)
    queryCount = basicUtil.getSplitCount(searchCount, NaverCrawlingConst.LIST_SPLIT_COUNT)

    viewUrlList = []
    searchCounting=0

    #Searched list in VIEW
    for i in range(queryCount):
        startNum = str(i * NaverCrawlingConst.LIST_SPLIT_COUNT + 1)
        searchUrl = basicUtil.getSearchUrl(searchText
                                            ,startNum
                                            ,NaverCrawlingConst.SEARCH_URL
                                            ,NaverCrawlingConst.VIEW_SEARCH_URL)

        soup = basicUtil.getSoup(searchUrl, headers)
        viewContents = soup.select(NaverCrawlingConst.VIEW_CONTENT_LIST_SELECTOR)

        for i in range(NaverCrawlingConst.LIST_SPLIT_COUNT):
            searchCounting += 1
            if(searchCounting>searchCount):
                break
            print(str(searchCounting)+'. 제목: '+viewContents[i].text+', URL: '+viewContents[i].get('href'))
            viewUrlList.append(viewContents[i].get('href')) #url list
    print()
    listCounting=0

    #The number of characters in the list
    for i in range(len(viewUrlList)):
        listCounting += 1
        url = viewUrlList[i]
        soup = basicUtil.getSoup(url, headers)
        contentCount = basicUtil.getViewContentCountResult(url, soup)
        print(str(listCounting)+NaverCrawlingConst.RESULT_OVERLAP_TEXT+str(contentCount))
    print()
    
    if(basicUtil.isProgramEnd()):
        break