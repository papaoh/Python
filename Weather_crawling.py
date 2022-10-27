from multiprocessing import BoundedSemaphore
import bs4
import urllib.request
import csv
import time
import datetime

# 날씨 정보 웹 크롤링 프로젝트

url = "https://news.nate.com/weather?areaCode=11B20303"

csvName = 'csv/paju_weather.csv' 
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])

nateUrl = "https://news.nate.com/weather?areaCode=11B20303"
timer = 1

while True:
    htmlObject = urllib.request.urlopen(nateUrl)
    webpage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webpage, 'html.parser')
    tag = bsObject.find('div', {'class':'right_today'})
    temper = tag.find('p', {'class':'celsius'}).text
    humi = tag.find('p', {'class':'humidity'}).text
    rain = tag.find('p', {'class':'rainfall'}).text
    wind = tag.find('p', {'class':'wind'}).text

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H-%M-%S')

    weather_list = [yymmdd, hhmmss, temper, humi, rain, wind]
    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(weather_list)
        print(weather_list)
    
    time.sleep(600) #10분마다 실행
    timer = timer + 1

    if (timer == 12):  #만약 실행한지 2시간이 지나면
        break

