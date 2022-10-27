from multiprocessing import BoundedSemaphore
import bs4    # 웹크롤링 라이브러리
import urllib.request
import csv    # csv파일 라이브러리
import time
import datetime

# 날씨 정보 웹 크롤링 프로젝트

url = "https://news.nate.com/weather?areaCode=11B20303"

csvName = 'csv/paju_weather.csv'  # csv 파일 경로
with open(csvName, 'w', newline='') as csvFp:   # csv파일 쓰기모드로 열기
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])  # 맨위에 헤더 쓰기

nateUrl = "https://news.nate.com/weather?areaCode=11B20303"  # 날씨 URL
timer = 1

while True:
    htmlObject = urllib.request.urlopen(nateUrl)  # URL 요청
    webpage = htmlObject.read()  # 요청한 데이터 읽기
    bsObject = bs4.BeautifulSoup(webpage, 'html.parser')  # 데이터를 html형식으로 읽기
    tag = bsObject.find('div', {'class':'right_today'})
    temper = tag.find('p', {'class':'celsius'}).text   # 온도
    humi = tag.find('p', {'class':'humidity'}).text    # 습도
    rain = tag.find('p', {'class':'rainfall'}).text    # 강수량
    wind = tag.find('p', {'class':'wind'}).text  # 풍향

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')  # 년, 월, 일
    hhmmss = now.strftime('%H-%M-%S')  # 시, 분, 초

    weather_list = [yymmdd, hhmmss, temper, humi, rain, wind]  # 리스트형식으로 저장
    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(weather_list)  # 웹크롤링한 데이터를 csv에 쓰기
        print(weather_list)
    
    time.sleep(600) #10분마다 실행
    timer = timer + 1

    if (timer == 12):  #만약 실행한지 2시간이 지나면
        break


