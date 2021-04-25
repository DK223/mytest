from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome(chrome_options=option)

try:
    browser.get('https://job.10086.cn/personal/job/detail.html?id=3690')
    input1 = browser.find_element_by_id('descriptionDiv')
    input2 = browser.find_element_by_id('introductionDiv')
    input3 = browser.find_element_by_id('companySummaryDiv')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 2)
    # wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)
    print(input1.text)
    print(input2.text)
    print(input3.text)
    # input = browser.find_element_by_class_name()
finally:
    browser.close()
# from bs4 import BeautifulSoup
# import requests
# import argparse
#
#
# def get_title_html(html):
#     soup = BeautifulSoup(html, "html.parser")
#     # print(soup.a)
#     title_url_Date = soup.find('div', class_='noticeConJob').find_all('li')
#     for i in title_url_Date:
#         # print(i)
#         url = i.find('a')['href']
#         print(url)
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="spyder for 10086")
#     parser.add_argument('--host', type=str, default="job.10086.cn")
#
#     args = parser.parse_args()
#
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": 'zh-CN,zh;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Cookie':'oJyMxTj348NZO=5xyakXZdTMYguknsQuCzYKl72eVNyuQOctaaXu9WL_VEaBIc8Htc2y6RQhgmwP5yMsfawyTyEVqTmQAnSNNElgG; WT_FPC=id=23e4ce4af9d26920e2d1606032252420:lv=1606037541520:ss=1606037540750; oJyMxTj348NZP=5U4LBVm5_WcAqqqmT40gj_qwSwz7Bi.6d_3hGqgXxjyN3KccjNtUwOdIO5IK4S0YdxCmUvoOUecfQpm5V9M1R_vqNgX5yJpCeH04n__vhn5umGMIgXVcPFHBb91U2uDGk7qknw_AbH7jq9AjZEHwOmIML.ElyYgs6uUUlB899uAZtfQHxGZ0_HWL67f7_6b.jbCLbQ2Xt3p1AdYUvfXT33RVrKZOawORafKTmz6dQmeRBh4P7F1D._QR8wyLvfqxocFDqCEXrVw57Qx4REy8RMt0FTJV8d129jciXLpUcmA.pT8B4RZcMS_ef6MXcuAnwg',
#         "Connection": "keep-alive",
#         'Sec - Fetch - Site': 'same - origin',
#         'Sec - Fetch - Mode': 'navigate',
#         'Sec - Fetch - User': '?1',
#         'Sec - Fetch - Dest': 'document',
#         "Host": args.host,
#         "Referer": 'https://job.10086.cn/personal/society/',
#         "Upgrade-Insecure-Requests": '1',
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
#     }
#
#     url = 'https://job.10086.cn/personal/job/detail.html?id=47937'
#     r = requests.get(url,headers=headers).text
#     print(r)
#     # get_title_html(r)
