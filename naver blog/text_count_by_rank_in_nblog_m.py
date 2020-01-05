#
# version 1.0.0
# Author: seol <kshzg26@gmail.com>
# The number of characters in the blog list (multiple)
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
    
    blogUrlList = []
    searchCounting=0

    #Searched list in Blog
    for i in range(queryCount):
        startNum = str(i * NaverCrawlingConst.LIST_SPLIT_COUNT + 1)
        searchUrl = basicUtil.getSearchUrl(searchText
                                            ,startNum
                                            ,NaverCrawlingConst.SEARCH_URL
                                            ,NaverCrawlingConst.BLOG_SEARCH_URL)

        soup = basicUtil.getSoup(searchUrl, headers)
        blogContents = soup.select(NaverCrawlingConst.BLOG_CONTENT_LIST_SELECTOR)

        for blogContent in blogContents:
            searchCounting += 1
            if(searchCounting>searchCount):
                break
            print(str(searchCounting)+'. 제목: '+blogContent.text+', URL: '+blogContent.get('href'))
            blogUrlList.append(blogContent.get('href')) #url list
    print()
    counting=0                
    
    #The number of characters in the list
    for i in range(len(blogUrlList)):
        counting += 1
        url = blogUrlList[i]
        soup = basicUtil.getSoup(url, headers)
        contentCount = basicUtil.getBlogContentCountResult(url, soup)
        print(str(counting)+NaverCrawlingConst.RESULT_OVERLAP_TEXT+str(contentCount))
    print()
    
    if(basicUtil.isProgramEnd()):
        break