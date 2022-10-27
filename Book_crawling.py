# yes24 홈페이지에서 국내 한국소설 판매량이 높은 순서대로 데이터를 가져오는 프로그램
# 추출할 키워드
# 도서명(good_name), 저자(good_auth), 출판사(good_pub), 출간일(good_date), 가격(yes_b)

import bs4  # 웹 크롤링 라이브러리

import urllib.request  # url 요청  

# 웹 크롤링 함수
def getBookInfo(book_tag):    # 데이터를 가져오는 형식들
    name = book_tag.find("div", {"class" : "goods_name"})   
    bookName = name.find("a").text    # div 영역의 goods_name 이라는 이름의 text를 저장
    auths = book_tag.find("span", {"class" : "goods_auth"})
    bookAuth = auths.find("a").text   # span 영역의 goods_auth 이라는 이름의 text를 저장
    bookPub = book_tag.find("span", {"class" : "goods_pub"}).text  # span 영역의 goods_pub 이라는 이름의 text를 저장
    bookDate = book_tag.find("span", {"class" : "goods_date"}).text  # span 영역의 goods_date 이라는 이름의 text를 저장
    bookPrice = book_tag.find("em", {"class" : "yes_b"}).text  # em 영역의 yes_b 이라는 이름의 text를 저장

    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

# 전역 변수

url = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="  
page = 1

# 메인 코드 작성
while(True):
    try:    # 예외처리문
        bookUrl = url + str(page)
        page = page + 1
        
        htmlObject = urllib.request.urlopen(bookUrl)          # URL 설정
        webPage = htmlObject.read()                           # URL 읽어오기
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')  # 데이터를 읽어올 형식

        tag = bsObject.find('ul', {'class' : 'clearfix'})  # 해당된 태그의 정보를 불러오기위한 태그 설정
        all_books = tag.findAll('div', {'class' : 'goods_info'}) # 

        for book in all_books:      # url에서 가져온 데이터 출력
            print(getBookInfo(book))

    except:  # 데이터를 전부다 읽으면 에러
        break  # 반복문 탈출


