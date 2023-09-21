from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 清除selenium的javascript头
option = webdriver.ChromeOptions()
option.add_argument('disable-gpu')
option.add_experimental_option('excludeSwitches', ['enable-automation'])

url = 'https://music.163.com/#/song?id=65766'
browser = webdriver.Chrome(chrome_options=option)

browser.get(url)
iframe = browser.find_element(by=By.CLASS_NAME, value='g-iframe')
browser.switch_to.frame(iframe)

for page in range(1, 5):
   
    # class_name = 'cnt f-brk'
    # 1. 通过class name获取

    # 获取class_name对应的所有的text信息
    comments_divs = browser.find_elements(by=By.CSS_SELECTOR, value='.itm')
    for comments_div in comments_divs:
        print(comments_div.text)
        # elment = browser.find_element(by=By.CSS_SELECTOR, value='.cnt.f-brk').text
        # print(elment)
    # for elment in elments:
    #     print(elment.text)


    # 找到下一页按钮
    browser.find_element(by=By.CSS_SELECTOR, value='.zbtn.znxt').click()
    time.sleep(1)