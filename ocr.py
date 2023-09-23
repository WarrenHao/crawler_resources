

import pandas as pd
import requests
import re
import random
from rich.progress import track
import time

cookie = ''

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': cookie
}

all_data = pd.read_csv('./最终数据1569家基本信息.csv')
all_codes = all_data['股票代码'].tolist()

# 随机选取50个股票代码
codes = random.sample(all_codes, 50)
all_list = []
for code in track(codes):
    time.sleep(0.5)

    url = f'https://www.qcc.com/web/search?key={code}'

    res = requests.get(url, headers=headers)

    href = re.findall(r'<div class="cname" data-v-525e50fd><a href="(.*?)" title="手机版" target="_blank" data-v-525e50fd>', res.text)
    all_list.append(href[0])

with open('./all_href.txt', 'w', encoding='utf-8') as f:
    for href in all_list:
        f.write(href + '\n')