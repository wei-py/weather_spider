# coding=utf-8
import requests
import json
import re
import os


curPath = __file__.replace('/region.py', '')
cookiesFile = curPath + '/utils/cookies.txt'
regionFile = curPath + '/utils/regionCode.json'


def headerToDic(s):
    return {i.split(': ')[0].strip(): i.split(': ')[1].strip() if len(i.split(': ')) > 1 else '' for i in s.split('\n') if len(i.split(': ')) > 1}


class Area():
    def __init__(self):
        self.curPath = __file__.replace('/Area.py', '')
        self.cookiesFile = self.curPath + '/utils/cookies.txt'
        self.regionFile = self.curPath + '/utils/regionCode.json'
        self.json_file = self.curPath+'/utils/cityCode.json'

    def city_code(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                city_json = json.loads(f.read())
        else:
            url = 'https://j.i8tq.com/weather2020/search/city.js'
            data = requests.get(url).text.replace(
                'var city_data = ', '')
            print(data)
            print('请求city_data')
            city_json = json.loads(data)
            # 默认缓存json文件
            with open(self.json_file, 'w') as f:
                f.write(json.dumps(city_json))
        return city_json

    def regionAREAID(self):
        result = {}
        city_json = self.city_code()
        for provinece in city_json:
            for city in city_json[provinece]:
                for region in city_json[provinece][city]:
                    result[region] = city_json[provinece][city][region]
        with open(self.regionFile, 'w') as f:
            f.write(json.dumps(result))
        return result

    def getAREAID(self, city):
        if not os.path.exists(self.regionFile):
            self.regionAREAID()
            return self.getAREAID(city)
        else:
            with open(self.regionFile, 'r') as f:
                code = json.loads(f.read())[city]['AREAID']
        return code


city = Area()
code = city.getAREAID('通州')
print(code)
# 'http://d1.city.com.cn/calendar_new/2021/101280501_202109.html?_=1630936182942'
