import multiprocessing
from gevent_case import GetContent, crawler_with_time_obstacle
import time
from rich.progress import track


if __name__ == '__main__':
    urls = [f'crawler_{i}' for i in range(30)]
    # 使用多进程完成爬虫任务
    start = time.time()
    processes = [multiprocessing.Process(target=crawler_with_time_obstacle, args=(url,)) for url in urls]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = time.time()
    print(f'多进程爬虫耗时: {end - start}秒')


    start = time.time()
    for url in track(urls):
        crawler_with_time_obstacle(url)
    end = time.time()
    print(f'普通爬虫耗时: {end - start}秒')
   
