import requests, json, re, os
import pandas as pd

def get_all_code():
    abspath = os.getcwd() 
    if not os.path.exists(abspath+'/dis_code.json'):
        url = 'https://j.i8tq.com/weather2020/search/city.js'
        resp = requests.get(url)
        with open('dis_code.json', 'w') as f:
            all_dis = resp.content.decode('utf-8').replace('var city_data = ', '')
            # dis = re.sub('"NAMECN":".*?"', '', all_dis)
            dis = json.loads(all_dis)
            json.dump(dis, f, ensure_ascii=False)
    with open(abspath+'/dis_code.json', 'r') as f:
        dis = json.loads(f.read())
    return dis

def get_dis_code():
    dis = get_all_code()
    provinece = input('输入省份或直辖市')
    city = input('输入城市')
    district = input('输入区')
    # provinece = '广东'
    # city = '汕头'
    # district = '潮阳'
    code = dis[provinece][city][district]['AREAID']
    return code

def weather_api():
    code = get_dis_code()
    # year = '2020'
    year = input('输入年份')
    month_str = ['0'+str(i) for i in range(1, 10)] + ['10','11','12']
    urls = [f'http://d1.weather.com.cn/calendar_new/{year}/{code}_{year}{month}.html' for month in month_str]
    return urls

