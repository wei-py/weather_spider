import requests
import json
import re
import requests_html
import pandas as pd
from district import weather_api
from openpyxl import Workbook

# 'http://d1.city.com.cn/calendar_new/2021/101280501_202109.html?_=1630936182942'


def get_weather(urls):
    session = requests_html.HTMLSession()
    data = {}
    for url in urls:
        resp = session.get(url)
        test = resp.content.decode('utf-8').replace('var fc40 = ', '')
        weather_list = json.loads(test)
        for weather in weather_list:
            data[weather['date']] = {'温度min': weather['hmin'], '温度max': weather['hmax'],
                                     '空气质量': weather['hgl'], '农历': weather['nlyf']+weather['nl']}
    excel = pd.DataFrame(data).T
    excel.to_excel('weather.xlsx')
    print(excel.T)
    # with open('weather.json', 'a+') as f:
    #     json.dump(data, f, ensure_ascii=False
    # )


urls = weather_api()
get_weather(urls)
