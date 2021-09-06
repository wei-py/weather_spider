from Browser import Bro

curPath = __file__.replace('/broCookie.py', '')
cookiesFile = curPath + '/cookies.txt'


def getCookies():
    bro = Bro()
    headlessBro = bro.headlessBro()
    url = 'http://www.weather.com.cn/'
    headlessBro.get(url)
    headlessBro.refresh()
    c = headlessBro.get_cookies()
    cookies = {cookie['name']: cookie['value'] for cookie in c}
    result = ''
    for k in cookies:
        result += k + '=' + cookies[k] + '; '
    with open(cookiesFile, 'w') as f:
        f.write(result)
    return result


getCookies()
