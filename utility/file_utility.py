#
# author : seol <kshzg26@gmail.com>
# file utility
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from const.naver_crawling_const import NaverCrawlingConst

class FileUtility:

    def makeDataFrametoCsv(self, dataFrame):
        dataFrame.index += 1 #1부터
        print(NaverCrawlingConst.INPUT_FILE_NAME)
        save_name = input()
        dataFrame.to_csv(save_name+'.csv', encoding='cp949')