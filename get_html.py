#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: chenhe<hee0624@163.com>
# time: 2017-11-30
# version: 1.0

import urllib
from urllib.parse import urlparse

import chardet
from fake_useragent import UserAgent


def get_html(url):
    ua = UserAgent()
    url_parse = urlparse(url)
    headers = {
        "User-Agent": ua.random,
        "Referer": "{}://{}".format(url_parse.scheme, url_parse.netloc),
    }
    request = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
    except Exception as e:
        print(e)
        return ''
    result = response.read()
    code_detect = chardet.detect(result)['encoding']
    if code_detect:
        html = result.decode(code_detect, 'ignore')
    else:
        html = result.decode("utf-8", 'ignore')
    return html


