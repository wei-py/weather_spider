from district import get_dis_code
from weather import get_weather
from concurrent.futures import ThreadPoolExecutor
from time import sleep

with ThreadPoolExecutor() as pool:
    futures = [pool.submit(get_dis_code), pool.submit(get_weather)]
    # pool.submit(get_dis_code)
    # sleep(3)
    # pool.submit(get_weather)