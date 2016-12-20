# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

class qsbk:
    # 初始化
    def __init__(self):
        self.page = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
        self.headers = {'User_Agent': self.user_agent}
        self.stories = []
        self.enable = False
    # 获取网页内容
    def getPage(self, page):
        try:
            url = 'http://www.qiushibaike.com/text/page/' + str(page)
            pageCode = requests.get(url, headers=self.headers)
            return pageCode

        except  requests.exceptions.RequestException as e:
            if hasattr(e, "reason"):
                print("连接糗事百科失败", e.reason)
                return None
    # 切割出段子
    def getPageStory(self, page):
        pageCode = self.getPage(page)
        if not pageCode:
            print("页面加载失败..")
            return None
        Soup = BeautifulSoup(pageCode.text, 'lxml')
        isStory = Soup.find('div', class_='col1').find_all("div", "content")
        pageStories = []
        for s in isStory:
            title = s.get_text()
            pageStories.append(title)
        return pageStories
    # 判断页数
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageStory(self.page)

                if pageStories:
                    self.stories.append(pageStories)
                    self.page += 1
    # 用户互动处理               
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            raw_input = input()
            self.loadPage()
            if raw_input == "Q":
                self.enable = False
                return
            print("第%d页\t%s" % (page, story))
    # 主程序
    def start(self):
        print("正在读取糗事百科，按回车查看新段子，Q退出")
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

spider = qsbk()
spider.start()

# 很粗糙，有空再添加一些东西进去
