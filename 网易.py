import requests
import pandas as pd
import json
from rich.progress import track
from Crypto.Cipher import AES

# window.asrsea(参数, 参数, 参数)

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

'''
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_65766",
    "threadId": "R_SO_4_65766"
    
}
'''

# 处理加密过程

def d_function_equal_to_arsea(d: str, e, f, g) -> str:
    '''
    :param d: 传入的数据(data)
    :param e: bvh7a(["流泪", "强"]) = '010001'
    :param f: bvh7a(Re1x.md) = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    :param g: bvh7a(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'
    
    '''
    ...

def a_function(a=16) -> str:
    '''
    :return: 生成16位随机字符串
    '''

    import random
    import math

    b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(a):
        e = math.floor(random.random())
        c += b[e]
    return c


def b_function(a, b) -> str:
    '''
    :param a: 传入的数据(data)
    :param b: 生成的16位随机字符串
    :return: 加密后的数据
    '''
    ...


def c_function(i, e, f):
    '''
    加密算法
    :param i: 随机数 = 's9TNIAsXBQKI1IJr'
    :param e
    :param f
    '''
    ...


def get_encSecKey():
    '''
    获取encSecKey
    :return: encSecKey = "458732d2cf956897990308f857e934cc5d1b2034dabe9abb480f5e6e5ecb3d8814d42a50ae20705cdafd00d2a9c4dfb0d4a0a1349e1fbc2c36d9914ca406d3a46fef6cc8132aac03a48c0bdce4bab3c5c5d7a107d0b8b34a6a9a511e6fcefa4093f9007bcbe7ec286b78003f80b7cb6cf0c7d3753090c82dd2ab9d3f98de51e3"
    '''
    ...


# 一个解密密钥对
rs_key_dict = {
    's9TNIAsXBQKI1IJr': '458732d2cf956897990308f857e934cc5d1b2034dabe9abb480f5e6e5ecb3d8814d42a50ae20705cdafd00d2a9c4dfb0d4a0a1349e1fbc2c36d9914ca406d3a46fef6cc8132aac03a48c0bdce4bab3c5c5d7a107d0b8b34a6a9a511e6fcefa4093f9007bcbe7ec286b78003f80b7cb6cf0c7d3753090c82dd2ab9d3f98de51e3'
}


# 常量
const_dict = {
    'd': '',
    'e': '010001',
    'f': '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7',
    'g': '0CoJUm6Qyw8W8jud',
}

'''
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c 
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }

'''

from base64 import b64encode

def format_16_bits(data: str) -> str:
    '''
    :param data: 传入的数据(data)
    :return: 16倍数长度的数据
    '''
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data: str, key) -> str:
    '''
    :param data: 传入的数据(data)
    :param key: 生成的16位随机字符串
    :return: 加密后的数据
    '''
    data = format_16_bits(data)
    
    iv = '0102030405060708'
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)

    # 加密为16倍数长度
    bs = aes.encrypt(data.encode('utf-8'))


    return str(b64encode(bs), 'utf-8')



def get_params(data: str) -> str:
    '''
    :param data: 传入的数据(data)
    :return: 加密后的参数
    '''
    frist = enc_params(data, const_dict['g'])
    return enc_params(frist, list(rs_key_dict.keys())[0])


data_list = list()
for i in track(range(5)):
    
    data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": f"{20 * i}",
    "orderType": "1",
    # "pageNo": f"{i+1}",
    "pageSize": "20",
    "rid": "R_SO_4_65766",
    "threadId": "R_SO_4_65766",
    "total": "false"}

    res = requests.post(url, data={
        'params':get_params(json.dumps(data)),
        'encSecKey' : list(rs_key_dict.values())[0]
    }).json()

    comments = res['data']['comments']
    for comment in comments:
        temp = dict()
        temp['nickname'] = comment['user']['nickname']
        temp['content'] = comment['content']
        data_list.append(temp)
        
        print(comment['user']['nickname'], comment['content'])
        print('\n')

data_df = pd.DataFrame(data_list)
data_df.to_csv('comments_网易云.csv', index=False, encoding='utf-8', seg='\t')
