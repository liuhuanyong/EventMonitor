# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class EventmonitorPipeline(object):
    def __init__(self):
        CUR = '/'.join(os.path.abspath(__file__).split('/')[:-2])
        self.news_path = os.path.join(CUR, 'news')
        if not os.path.exists(self.news_path):
            os.makedirs(self.news_path)

    '''处理数据流'''
    def process_item(self, item, spider):
        print(item)
        keyword = item['keyword']
        event_path = os.path.join(self.news_path, keyword)
        if not os.path.exists(event_path):
            os.makedirs(event_path)
        filename = os.path.join(event_path, item['news_date'] + '＠' + item['news_title'])
        self.save_localfile(filename, item['news_title'], item['news_time'], item['news_content'])
        return item

    '''将内容保存至文件当中'''
    def save_localfile(self, filename, title, pubtime, content):
        with open(filename, 'w+') as f:
            f.write('标题:{0}\n'.format(title))
            f.write('发布时间:{0}\n'.format(pubtime))
            f.write('正文:{0}\n'.format(content))
        f.close()
