#
# version 1.0.0
# author : seol <kshzg26@gmail.com>
# crawling const
#
class NaverCrawlingConst:
    SEARCH_URL = 'https://m.search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query='
    HEADER_WINDOW_CHROME = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    RESULT_OVERLAP_TEXT = '. 내용 글자 수: '
    SEARCH_QUESTION = "네이버에서 검색할 단어 >"
    SEARCH_KEYWORD_QUESTION = "네이버에서 검색할 단어 [다중 검색어 입력 시 쉼포(,)로 구분 => ex: 안산요가, 안산 필라테스, 안산 플라잉요가] >"
    SEARCH_URL_QUESTION = "naver blog url(모바일 url) :"
    RANK_RANGE_QUESTION = "출력할 개수 (ex: 1~15등까지라면 15를 입력) >"
    FIND_RANK_QUESTION = "랭킹을 알아보고 싶은 업체명 >"
    INPUT_FILE_NAME = "파일명 입력 >"
    LIST_SPLIT_COUNT = 10
    
    BLOG_SEARCH_URL = '&sm=tab_pge&srchby=all&st=sim&where=m_blog&start='
    BLOG_CONTENT_LIST_SELECTOR = '#addParemt > li.bx > div > a'
    BLOG_POSTVIEW_CONTENT_SELECTOR = '#_post_area > #ct > div._postView > div.post_ct > div.se_doc_viewer > div.se_component_wrap > div.se_component > div.se_sectionArea > div.se_editArea > div.se_viewArea > div.se_editView > div.se_textView > p.se_textarea'
    BLOG_CONTENT_SELECTOR1 = 'div > div > div.se-main-container > div.se-component > div.se-component-content > div.se-section > div.se-module > p.se-text-paragraph'
    BLOG_CONTENT_SELECTOR2 = '#viewTypeSelector > div'
    BLOG_CONTENT_SELECTOR3 = '#viewTypeSelector > p'
    BLOG_CONTENT_SELECTOR4 = '#viewTypeSelector > span > p'
    BLOG_CONTENT_SELECTOR5 = '#viewTypeSelector > div > p'
    BLOG_CONTENT_SELECTOR6 = '#viewTypeSelector'
    
    VIEW_SEARCH_URL = '&sm=tab_pge&srchby=all&st=sim&where=m_view&start='
    VIEW_CONTENT_LIST_SELECTOR = '#_view_review_body_html > div > div > panel-list > div:nth-child(1) > select-contents > more-contents > div > ul > li > div.total_wrap > a'
    VIEW_DATE_LIST_SELECTOR = '#_view_review_body_html > div > div > panel-list > div:nth-child(1) > select-contents > more-contents > div > ul > li > div.total_wrap > div.total_group > div.total_sub > span > span > span.etc_dsc_area > span'
    
    CAFE_CONTENT_SELECTOR1 = '#postContent'
    
    POST_CONTENT_SELECTOR1 = "#cont > div"
