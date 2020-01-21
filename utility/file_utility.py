#
# author : seol <kshzg26@gmail.com>
# file utility
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from const.naver_crawling_const import NaverCrawlingConst
import openpyxl as excel

class FileUtility:

    def makeDataFrametoCsv(self, dataFrame, startIndex, changeIndex):
        dataFrame.index += startIndex #1부터
        dataFrame.rename(index = {changeIndex : NaverCrawlingConst.TOP_RANK}, inplace = True) #first index rename
        print(NaverCrawlingConst.INPUT_FILE_NAME)
        save_name = input()
        # dataFrame.to_csv(save_name+'.csv', encoding='cp949')
        dataFrame.to_excel(save_name+'.xlsx')