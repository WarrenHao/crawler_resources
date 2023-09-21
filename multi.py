from multiprocessing import Pool


def crwal(url):
    # 爬取网页的代码
    pass


if __name__ == '__main__':
    pool = Pool(processes=4)
    urls = []
    pool.map(crwal, urls)
    pool.close()
    pool.join()
