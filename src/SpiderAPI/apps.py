#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   apps.py
@Time    :   2019/03/27 15:34:17
@Author  :   hsp 
@Desc    :   None
'''

# here put the import lib

from django.apps import AppConfig


class SpiderAPIConfig(AppConfig):
    name = 'SpiderAPI'
    verbose_name = u"爬虫API"
