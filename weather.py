import requests, json, re
import pandas as pd



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


