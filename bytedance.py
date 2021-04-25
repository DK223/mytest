import requests as re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import InvalidSessionIdException
import os
chrome_opts=webdriver.ChromeOptions()
chrome_opts.add_argument("--headless")
chromedriver = 'chromedriver.exe'
os.environ['webdriver.chrome.driver'] = chromedriver

browser = webdriver.Chrome(chrome_options=chrome_opts)
# browser = webdriver.Chrome()

def main():
    t1 = time.time()
    sum_num = 0
    #打开本地存储的网页
    html_url = "https://job.bytedance.com/society/position?keywords=&category=6704216853931100430%2C6704217437631416580%2C6704219199050352903%2C6709824273306880267%2C6850051246221429006%2C6863074795655792910&location=&project=&type=&job_hot_flag=&current=1&limit=1000"
    # html = re.get(html_url)
    # print(html)
    # file = open('加入字节跳动.html','r',encoding='utf-8')
    # bs = BeautifulSoup(file, "html.parser")

    #获取详情页链接#
    browser.get(html_url)
    # print(browser)

    hrefs = []
    elements = browser.find_element_by_class_name('listItems__1q9i5')
    for ele in elements.find_elements_by_xpath('a'):
        href = ele.get_attribute('href')
        hrefs.append(href)
    # print(elements.get_attribute('href'))
    # for ele in elements:
    # urls = elements.find_elements_by_xpath("[@href]")
    # for url in urls:

        # print(ele.get_attribute("href"))
    #infos存放每条职位的预览页信息，hrefs存放每条职位的详情页链接
    # infos = bs.find('div',class_='listItems__1q9i5').find_all('a')

    # for info in infos:
    #     hrefs.append(info.get("href"))
    print("一共有%d条职位"%len(hrefs))


    station_list=[]

    for i in range(len(hrefs)):
        station = {}
        url=hrefs[i]
        try:
            browser.get(url)

            wait = WebDriverWait(browser, 10)
            # print(browser.page_source)
            # 网页的刷新需要时间，爬虫速度快于刷新速度会报出找不到元素的错误，所以加上一个wait,等待，直到找到元素。
            wait.until(lambda driver: driver.find_element_by_class_name("job-header.sofiaBold"))
            # class里面不能有空格，出现空格的时候用 . 代替
            station['岗位名称'] = browser.find_element_by_class_name("job-header.sofiaBold").text
            station['职位描述'] = browser.find_elements_by_class_name("block-content")[0].text
            station['职位要求'] = browser.find_elements_by_class_name("block-content")[1].text

            s = browser.find_element_by_class_name("job-info")

            # print(s.text.split('\n'))
            station['工作地点'] = s.text.split('\n')[0]
            station['岗位分类'] = s.text.split('\n')[1]
            station['招聘类型'] = s.text.split('\n')[2]



            # print(station)
            station_list.append(station)
            print(station_list[i])  # 打印每一个url爬下来的信息，而不是所有的，这样看的时候方便一点
            sum_num += 1
            # browser.back()
        except Exception as e:  # 添加了一个报错信息，这个应该影响不大，用原来的应该也行。
            print(url)
            print(e)
    print('sum_num:', sum_num)
    t2 = time.time()
    print('time:',t2-t1)



if __name__ == "__main__":
    main()