from gevent import monkey; monkey.patch_all()
import gevent
import time
from dataclasses import dataclass
from rich.progress import track
from typing import *


@dataclass
class GetContent:
    url: str
    method: str = 'GET'
    headers: dict = None
    data: dict = None


def crawler_with_time_obstacle(url):
    '''
    定义一个带有阻塞的爬虫
    '''
    time.sleep(0.5)
    content = GetContent(url)
    return content


if __name__ == '__main__':
    start = time.time()
    urls = [f'crawler_{i}' for i in range(30)]
    tasks = [gevent.spawn(crawler_with_time_obstacle, url) for url in urls]
    gevent.joinall(tasks)
    end = time.time()
    print(f'gevent爬虫耗时: {end - start}秒')

    start = time.time()
    for url in track(urls):
        crawler_with_time_obstacle(url)
    end = time.time()
    print(f'普通爬虫耗时: {end - start}秒')
