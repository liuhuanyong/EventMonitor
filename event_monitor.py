#!/usr/bin/env python3
# coding: utf-8
# File: word_monitor.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-5-28
import urllib.parse
import urllib.request
from lxml import etree
import extract_news


class NewsMonitor:
    def __int__(self):
        self.sogou_hompage = 'http://news.sogou.com/news?mode=0&manual=true&query=%D6%D0%D0%CB&sort=1&page=2'
        self.baidu_homepage = 'http://news.baidu.com/ns?word=title%3A%28%E4%B8%AD%E5%85%B4%29&pn=0&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'

    def get_html(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17"}
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        return html

    def get_news(self, html):
        selector = etree.HTML(html)
        urls = selector.xpath('//h3[@class="c-title"]/a/@href')
        print(len(urls))
        return urls

    def search_news(self, word):
        url_list = []
        word = urllib.parse.quote_plus(word)
        for page_num in range(20, 800, 20):
            news_url = 'http://news.baidu.com/ns?word=title%3A%28'+word+'%29&pn=' + str(page_num) + '&cl=2&ct=0&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'
            news_html = self.get_html(news_url)
            news_links = self.get_news(news_html)
            url_list += news_links
        return set(url_list)

    def collect_news(self, urls):
        for url in urls:
            try:
                data = extract_news.online_parse(url)
                print(data)
                try:
                    file_name = data['news_pubtime']
                    news_title = data['news_title']
                    news_content = data['news_content']
                    f = open('news/%s.txt'%(file_name +'@' + news_title), 'w+')
                    f.write(news_content)
                    f.close()
                except:
                    pass
            except:
                pass

def demo():
    news_monitor = NewsMonitor()
    word = '中兴'
    news_list = news_monitor.search_news(word)
    news_monitor.collect_news(news_list)
    f = open('news_list.txt', 'w+')
    for news in news_list:
        f.write(news + "\n")
    f.close()


demo()