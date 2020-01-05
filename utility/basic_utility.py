#
# author : seol <kshzg26@gmail.com>
# basic utility
# TODO
# pip install requests
# pip install bs4  
# pip install lxml
#

import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from const.naver_crawling_const import NaverCrawlingConst
from bs4 import BeautifulSoup

class BasicUtility:

    def isExistKeywordResult(self, url, soup, title, keyword):
        self.isIncludeKeyword = -1

        if(self.isExistKeywordByIsValidPostView(url, soup, title, keyword) != -1):
            return True

        if(self.isExistKeyword(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR2, title, keyword) != -1):
            return True
        
        if(self.isExistKeyword(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR3, title, keyword) != -1):
            return True

        if(self.isExistKeyword(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR4, title, keyword) != -1):
            return True

        if(self.isExistKeyword(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR5, title, keyword) != -1):
            return True

        if(self.isExistKeyword(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR6, title, keyword) != -1):
            return True
        
        if(self.isExistKeyword(soup, NaverCrawlingConst.CAFE_CONTENT_SELECTOR1, title, keyword) != -1):
            return True
        
        if(self.isExistKeyword(soup, NaverCrawlingConst.POST_CONTENT_SELECTOR1, title, keyword) != -1):
            return True

        return False
        

    def isExistKeyword(self, soup, selector, title, keyword):
        contents = soup.select(selector)
        for content in contents:
            # print(content.text.replace(" ", "").replace("\n",""))
            # content = title+content.text.replace(" ", "").replace("\n","")
            content = title+content.text
            self.isIncludeKeyword = content.find(keyword)
        return self.isIncludeKeyword


    def isExistKeywordByIsValidPostView(self, url, soup, title, keyword):
        if 'PostView' in url:
            contents = soup.select(NaverCrawlingConst.BLOG_POSTVIEW_CONTENT_SELECTOR)
        else:
            contents = soup.select(NaverCrawlingConst.BLOG_CONTENT_SELECTOR1)
        
        for content in contents:
            # print(content.text.replace(" ", "").replace("\n",""))
            # content = title+content.text.replace(" ", "").replace("\n","")
            content = title+content.text
            self.isIncludeKeyword = content.find(keyword)
        return self.isIncludeKeyword


    def getViewContentCountResult(self, url, soup):
        self.contentCount = 0

        if(self.getContentCountByIsValidPostView(url, soup) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR2) > 0):
            return self.contentCount
        
        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR3) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR4) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR5) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR6) > 0):
            return self.contentCount
        
        if(self.getContentCount(soup, NaverCrawlingConst.CAFE_CONTENT_SELECTOR1) > 0):
            return self.contentCount
        
        if(self.getContentCount(soup, NaverCrawlingConst.POST_CONTENT_SELECTOR1) > 0):
            return self.contentCount

        return "fali to bring (need join a cafe or daum blog or missed selector)"


    def getBlogContentCountResult(self, url, soup):
        self.contentCount = 0

        if(self.getContentCountByIsValidPostView(url, soup) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR2) > 0):
            return self.contentCount
        
        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR3) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR4) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR5) > 0):
            return self.contentCount

        if(self.getContentCount(soup, NaverCrawlingConst.BLOG_CONTENT_SELECTOR6) > 0):
            return self.contentCount
        
        return "fali to bring (daum blog or missed selector)"


    def getContentCount(self, soup, selector):
        contents = soup.select(selector)
        for content in contents:
            # print(content.text.replace(" ", "").replace("\n",""))
            self.contentCount += len(content.text.replace(" ", "").replace("\n",""))
        return self.contentCount


    def getContentCountByIsValidPostView(self, url, soup):
        if 'PostView' in url:
            contents = soup.select(NaverCrawlingConst.BLOG_POSTVIEW_CONTENT_SELECTOR)
        else:
            contents = soup.select(NaverCrawlingConst.BLOG_CONTENT_SELECTOR1)
        
        for content in contents:
            # print(content.text.replace(" ", "").replace("\n",""))
            self.contentCount += len(content.text.replace(" ", "").replace("\n",""))
        return self.contentCount


    def getSoup(self, url, headers):
        # HTTP GET Request
        req = requests.get(url, headers = headers)
        # HTML 소스 가져오기
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        return soup


    def getSearchCount(self, rankQuestion):
        searchCount = ''
        # isValid int
        while searchCount.isdecimal() is False:     
            print(rankQuestion)
            searchCount = input()
            if searchCount.isdecimal() is False:
                rankQuestion = "숫자를 입력하세요"

        return int(searchCount)


    def getSplitCount(self, searchCount, splitCount):
        queryCount = (searchCount//splitCount)
        if (searchCount%splitCount > 0):
            queryCount+=1
        return queryCount


    def getSearchUrl(self, searchText, startNum, url1, url2):
        return (url1+searchText+url2+startNum)


    def getMobileUrl(self, url):
        if not 'm.blog.naver.com' in url:
            url = url.replace('https://blog','https://m.blog')
        return url


    def isProgramEnd(self):
        isProcess = 'p'
        while isProcess is not 'y' and isProcess is not 'n' :
            print("계속 진행할거면 y, 종료할거면 n")
            isProcess = input()
        if isProcess is 'n':
            return True