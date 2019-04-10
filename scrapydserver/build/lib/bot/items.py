# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from ScrapydAPI.models import TweetsInfo, UserInfo, RelationshipsInfo, CommentInfo

class TweetsItem(DjangoItem):
    django_model = TweetsInfo

class InformationItem(DjangoItem):
    django_model = UserInfo

class RelationshipsItem(DjangoItem):
    django_model = RelationshipsInfo

class CommentItem(DjangoItem):
    django_model = CommentInfo
