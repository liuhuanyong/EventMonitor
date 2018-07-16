#!/usr/bin/env python3
# coding: utf-8
# File: news_spider.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-7-15

import scrapy
from lxml import etree
import urllib.request
import urllib.parse
from .extract_news import *
from EventMonitor.items import EventmonitorItem

class NewsSpider(scrapy.Spider):
    name = 'eventspider'
    def __init__(self, keyword):
        self.sogou_hompage = 'http://news.sogou.com/news?mode=0&manual=true&query=%D6%D0%D0%CB&sort=1&page=2'
        self.baidu_homepage = 'http://news.baidu.com/ns?word=title%3A%28%E4%B8%AD%E5%85%B4%29&pn=0&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'
        self.keyword = keyword
        self.parser = NewsParser()

    '''获取搜索页'''
    def get_html(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17"}
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        return html

    '''获取新闻列表'''
    def collect_newslist(self, html):
        selector = etree.HTML(html)
        urls = selector.xpath('//h3[@class="c-title"]/a/@href')
        return set(urls)

    '''采集主函数'''
    def start_requests(self):
        word = urllib.parse.quote_plus(self.keyword)
        for page_num in range(20, 800, 20):
            url = 'http://news.baidu.com/ns?word=title%3A%28'+word+'%29&pn=' + str(page_num) + '&cl=2&ct=0&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0'
            html_search = self.get_html(url)
            news_links = self.collect_newslist(html_search)
            print(news_links)
            for news_link in news_links:
                param = {'url': news_link}
                yield scrapy.Request(url=news_link, meta=param, callback=self.page_parser, dont_filter=True)

    '''对网站新闻进行结构化抽取'''
    def page_parser(self, response):
        data = self.parser.extract_news(response.text)
        if data:
            item = EventmonitorItem()
            item['keyword'] = self.keyword
            item['news_url'] = response.meta['url']
            item['news_time'] = data['news_pubtime']
            item['news_date'] = data['news_date']
            item['news_title'] = data['news_title']
            item['news_content'] = data['news_content']
            yield item
        return
