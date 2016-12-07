# 用来查询深圳培训公司

import requests
from bs4 import BeautifulSoup

class chaxun:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
        self.headers = {'User-Agent':self.user_agent}

    def getPage(self):
        try:
            url = 'https://github.com/ZGWS88/TI/blob/master/List.txt'
            pageTxt = requests.get(url, headers=self.headers)
            return pageTxt

        except requests.exceptions.RequestException as r:
            if hasattr(r, 'reason'):
                print("连接github失败", r.reason)
                return None

    def getList(self):
        pageTxt = self.getPage()
        if not pageTxt:
            print("页面加载失败..")
            return None
        Soup = BeautifulSoup(pageTxt.text, 'lxml')
        isList = Soup.find('table', class_='highlight tab-size js-file-line-container').find_all("td", "blob-code blob-code-inner js-file-line")
        pageList = []
        for l in isList:
            title = l.get_text()
            pageList.append(title)
        return pageList

    def start(self):
        name = input("请输入需要查询的公司名：")
        isList = self.getList()
        if name in isList:
            print("培训公司：%s" %name)
            return
        else:
            print("不是培训公司")
            return

spider = chaxun()
spider.start()

