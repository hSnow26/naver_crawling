#
# version 1.0.0
# Author : soel <kshzg@naver.com>
# 
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utility.basic_utility import BasicUtility
from const.naver_crawling_const import NaverCrawlingConst

basicUtil = BasicUtility()
headers = {'User-Agent' : NaverCrawlingConst.HEADER_WINDOW_CHROME}
# url = 'https://m.blog.naver.com/PostView.nhn?blogId=minic3000&logNo=220975837336&navType=tl'

print(NaverCrawlingConst.SEARCH_URL_QUESTION)
# url = input()
url = basicUtil.getMobileUrl(input())

soup = basicUtil.getSoup(url, headers)
contentCount = basicUtil.getBlogContentCountResult(url, soup)

print('\n본문 글자 수 : '+str(contentCount))