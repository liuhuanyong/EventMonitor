#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: chenhe<hee0624@163.com>
# time: 2017-11-30
# version: 1.0

import re

def drop_null(arg):
    if isinstance(arg, str):
        arg = re.sub('\s', '', arg, flags=re.S)
        return arg
    elif isinstance(arg, list):
        new_list = []
        for i in arg:
            i = i.strip()
            if i:
                new_list.append(i)
            else:
                continue
        return new_list
    else:
        return arg

def drop_mutil_br(str):
    str = re.sub(r'<br>|</br>', '\n', str)
    str = re.sub(r'\n\s+', '\n', str)
    return str


def drop_mutil_blank(str):
    str = re.sub(r'\s{2,}', ' ', str)
    return str