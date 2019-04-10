#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2019/03/27 20:00:47
@Author  :   hsp 
@Desc    :   None
'''

# here put the import lib


# Create your views here.

from django.shortcuts import render
# from django.db.models import Q
from django.http import HttpResponse
from django.core import serializers
from datetime import date
from datetime import datetime
from .models import Target, UserInfo, TweetsInfo
from .spider import Weibo
from lxml import etree
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import traceback


class SpiderWeibo:
    @csrf_exempt
    def SpiderAPI(request):
        res = {}
        if request.method == "POST":
            text = request.POST.get("weiboId")
            try:
                UserInfo.objects.get(_id = text)
                res['ok'] = "数据库已存在该用户，开始返回数据"
                # UserInfo.objects.values("_id","Image","NickName","Gender","Province",
                # "City","BriefIntroduction","Birthday","Constellation","Num_Tweets","Num_Follows","Num_Fans",
                # "SexOrientation","Sentiment","VIPlevel","Authentication","URL")
                res['data'] = serializers.serialize("json", UserInfo.objects.filter(_id=text))
                # res['data'] = json.dumps(UserInfo.objects.all())
                print(res['data'])
            except UserInfo.DoesNotExist:
                print("数据库不存在该数据，开始爬虫")
                res['ok']= "数据库不存在该数据，开始爬虫"
        else:
            text = "输入微博Id错误，请重新输入！"
            res['ok'] = text
        # try:
        # resp = Target.objects.values('uid','cookie','add_time')
        # resp = json.dumps(resp,cls=JsonCustomEncoder)
        resp = list(Target.objects.values('uid', 'cookie', 'add_time'))
        uid = int(resp[0]["uid"])
        cookie = {"Cookie": resp[0]["cookie"]}
        # resp = serializers.serialize("json", Target.objects.all().order_by("-id")[:1])
        # wb = Weibo(uid,cookie)
        # mm = wb.get_comment_info('4358934418168720')
        # mm = wb.get_weibo_info()
        # mm = wb.getTest()

        return HttpResponse(json.dumps(res))
        # except Exception as e:
        #     return HttpResponse('拉取数据库数据失败: %s' % e)
        
    # def UserInfor(request):
        # ############### 添加数据 ###############
        # import random
        # product_list_to_insert = list()
        # for x in range(100):
        #     product_list_to_insert.append(Test(name='apollo'+str(x), age=random.randint(18,89)))
        # Test.objects.bulk_create(product_list_to_insert)
        # return render(request, 'index.html')

#日期转化代码
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):          
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        # elif isinstance(field, date):
        #     return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)
