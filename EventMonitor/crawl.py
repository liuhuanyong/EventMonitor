#!/usr/bin/env python3
# coding: utf-8
# File: crawl.py.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-7-15
from scrapy import cmdline
projcet_name = 'eventspider'
event_list = ['江歌被害案', '红黄蓝幼儿园虐童','于欢杀死辱母者','白银连环杀人',
              '章莹颖失踪','杭州保姆纵火','榆林产妇坠楼','老虎咬人事件',
               '魏则西事件','雷洋涉“嫖娼”致死','如家酒店女子遇袭','罗一笑事件',
              '徐玉玉电信诈骗身亡']

for event in event_list:
    cmdline.execute("scrapy crawl {0} -a keyword={1}".format(projcet_name, event).split())