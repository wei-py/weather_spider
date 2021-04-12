<<<<<<< HEAD
import requests, json, re, requests_html
import pandas as pd
from district import weather_api
from openpyxl import Workbook
=======
import requests, json, re
>>>>>>> c47277cfa765dd4018c4dc2a052d634227ccbfd1
import pandas as pd



<<<<<<< HEAD
def get_weather(urls):
    session = requests_html.HTMLSession()
    data = {}
    for url in urls:
        resp = session.get(url)
        test = resp.content.decode('utf-8').replace('var fc40 = ', '')
        weather_list = json.loads(test)
        # print(weather_list)
        for weather in weather_list:
        #     # date hgl hmax hmin nl nlyf
            data[weather['date']] = {'温度min':weather['hmin'], '温度max':weather['hmax'],'空气质量':weather['hgl'],'农历':weather['nlyf']+weather['nl']}
    excel = pd.DataFrame(data).T
    excel.to_excel('weather.xlsx')
    print(excel.T)
    # with open('weather.json', 'a+') as f:
    #     json.dump(data, f, ensure_ascii=False)

urls = weather_api()
get_weather(urls)
=======
def get_weather():
    with open('dis_code.json', 'r') as f:
        all_dis = re.sub(', "NAMECN": ".*?"', '', f.read())
        all_dis = json.loads(all_dis)

    # provinece = input('输入省份或直辖市')
    # city = input('输入城市')
    # district = input('输入区')
    year = '2020'
    provinece = '广东'
    city = '汕头'
    district = '潮阳'
    code = all_dis[provinece][city][district]['AREAID']
    print(code)
    urls = [f'http://d1.weather.com.cn/calendar_new/{year}/{code}_{year}{month}.html' for month in range(1, 13)]
    for url in urls:
        resp = requests.get(url)
        print(url)
        with open('weather.json', 'a+') as f:
            test = resp.content.decode('utf-8').replace('var fc40 = ', '')
            test = json.loads(test)[0]
            print(type(test))
            json.dump(test, f, ensure_ascii=False)


>>>>>>> c47277cfa765dd4018c4dc2a052d634227ccbfd1
