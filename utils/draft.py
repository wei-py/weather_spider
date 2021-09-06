from Browser import Bro
from requests_html import HTMLSession

# session = HTMLSession()


def get_resp():
    session = HTMLSession()
    url = 'https://j.i8tq.com/city2020/search/city.js'
    resp = session.get(url)
    return resp.text


print(get_resp())
