#
# version 1.0.0
# Author : soel <kshzg@naver.com>
# The number of characters in the blog list
# 
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utility.basic_utility import BasicUtility
from const.naver_crawling_const import NaverCrawlingConst

basicUtil = BasicUtility()
headers = {'User-Agent' : NaverCrawlingConst.HEADER_WINDOW_CHROME}

print(NaverCrawlingConst.SEARCH_URL_QUESTION)
url = input()
url = basicUtil.getMobileUrl(url)

soup = basicUtil.getSoup(url, headers)
contentCount = basicUtil.getBlogContentCountResult(url, soup)

print('\n본문 글자 수 : '+str(contentCount))