#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2019/03/27 20:00:47
@Author  :   hsp 
@Desc    :   None
'''

from django.shortcuts import render
# from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, date, time, timedelta
from .models import Target, UserInfo, TweetsInfo, CommentWeiboInfo, CommentInfo, ImgInfo
from .spider import Weibo
from lxml import etree
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from src.SnowNLPAPI.snownlp import SnowNLP
from src.SnowNLPAPI.snownlp import sentiment
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter

from os import path
import jieba
import time
import matplotlib.pyplot as plt
import base64
import json
import requests
import traceback
import re


class SpiderWeibo:
    @csrf_exempt
    def SpiderAPI(request):
        res = {}
        if request.method == "POST":
            text = request.POST.get("weiboId")
            page = request.POST.get("page")
            if not page: #默认page 为1
                page = 1
            else:
                page = int(page) #get过来的page参数是字符串
            try:
                UserInfo.objects.get(_id = text)
                res['ok'] = "数据库已存在该用户，开始返回数据"
                res['data'] = serializers.serialize("json", UserInfo.objects.filter(_id=text))
                aritcles = TweetsInfo.objects.filter(UserInfo_id = text).order_by("-PubTime") #查询所有的数据
                paginator = Paginator(aritcles, 20) #对数据进行分页，每页20条
                print("=======================================")
                print(paginator.count,paginator.num_pages)
                pageData = paginator.page(page)
                res['total'] = paginator.count
                res['tweets'] = serializers.serialize("json",pageData)
                return HttpResponse(json.dumps(res))
            except UserInfo.DoesNotExist:
                print("数据库不存在该数据，开始爬虫")
                Target.objects.filter(id=1).update(uid=text)
                resp = list(Target.objects.values('uid', 'cookie', 'add_time'))
                uid = int(resp[0]["uid"])
                cookie = {"Cookie": resp[0]["cookie"]}
                wb = Weibo(uid,cookie)
                wb.get_userInfo()
                wb.get_weibo_info()
                qqq = TweetsInfo.objects.filter(Content='').delete()
                res['ok']= "数据库不存在该数据的爬虫"
                res['data'] = serializers.serialize("json", UserInfo.objects.filter(_id=text))
                aritcles = TweetsInfo.objects.filter(UserInfo_id = text).order_by("-PubTime") #查询所有的数据
                paginator = Paginator(aritcles, 20) #对数据进行分页，每页20条
                print("=======================================")
                print(paginator.count,paginator.num_pages)
                pageData = paginator.page(page)
                res['total'] = paginator.count
                res['tweets'] = serializers.serialize("json",pageData)
                return HttpResponse(json.dumps(res))

        # if request.method == "GET":
        #     text = request.GET.get("weiboId")
 
        #     print(li)
        #     return HttpResponse(json.dumps(li))

    @csrf_exempt
    def WordCloudAPI(request):
        res = {}
        if request.method == "GET":
            text = request.GET.get("weiboId")
            aritcles = TweetsInfo.objects.filter(UserInfo_id = text)
            content = ''
            for e in aritcles:
                content += e.Content.replace('转发','').replace('转发理由:','').replace('转发内容:', '').replace('原始用户:', '').replace('转发微博已被删除', '')
            content = re.sub("[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]", "", content)
            wordlist_after_jieba = jieba.cut(content, cut_all=False)
            wl_space_split = (" ".join(wordlist_after_jieba))
            filepath = path.dirname(__file__) + '\stopword.txt'
            stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
            minganfilepath = path.dirname(__file__) + '\mingan.txt'
            minganwords = [line.strip() for line in open(minganfilepath, 'r', encoding='utf-8').readlines()]
            c=Counter()
            outstr = ''
            for word in wl_space_split:
                if word not in stopwords:
                    if word != '\t'and'\n':
                        outstr += word 
            outstr = outstr.split(' ')
            while '' in outstr:
                outstr.remove('')
            for word in outstr:
                c[word] += 1
            cipin = list()
            li = list(c.items())
            li.sort(key=lambda x:x[1], reverse=True)
            mingancount = 0
            for (k, v) in li:
                if k in minganwords:
                    mingancount += 1
                cipin.append({"word":k,"count":v})
            res['mingan'] = mingancount/len(li)
            res['cipin'] = cipin
            qqq = TweetsInfo.objects.filter(sentiments='').delete()
            infos = TweetsInfo.objects.filter(UserInfo_id = text).values('sentiments')
            c = Counter()
            for word in infos:
                c[word['sentiments']] += 1
            li = list(c.items())
            li.sort(key=lambda x:x[0])
            res['tu'] = json.dumps(li)
            imgInfo = ImgInfo()
            imgInfo.UserInfo_id = text
            imgInfo.wordcloud = res
            try:
                ImgInfo.objects.get(UserInfo_id = text)
                print("数据库已存在该词频")
            except ImgInfo.DoesNotExist:
                print("开始保存数据")
                imgInfo.save()
                print("保存数据成功")
        return HttpResponse(json.dumps(res))

    @csrf_exempt
    def TweetsAPI(request):
        ret = {}
        if request.method == "POST":
            text = request.POST.get("weiboId")
            page = request.POST.get("page")
            print(text, page)
            if not page: #默认page 为1
                page = 1
            else:
                page = int(page) #get过来的page参数是字符串
            aritcles = TweetsInfo.objects.filter(UserInfo_id = text).order_by("-PubTime") #查询所有的数据
            paginator = Paginator(aritcles, 20) #对数据进行分页，每页20条
            print("=======================================")
            print(paginator.count,paginator.num_pages)
            pageData = paginator.page(page)
            ret['total'] = paginator.count
            ret['data'] = serializers.serialize("json",pageData)
            return HttpResponse(json.dumps(ret))
        if request.method == "GET":
            text = request.GET.get("weiboId")
            qqq = TweetsInfo.objects.filter(Content='').delete()
            all = TweetsInfo.objects.filter(UserInfo_id=text)
            for e in all:
                mm = ()
                s = SnowNLP(e.Content.replace('转发理由','').replace('转发内容', '').replace('原始用户', '').replace('转发微博已被删除', ''))
                for i in s.tags:
                    mm += i
                TweetsInfo.objects.filter(_id=e._id).update(tags=s.keywords(5))
                TweetsInfo.objects.filter(_id=e._id).update(pinyin=mm)
                TweetsInfo.objects.filter(_id=e._id).update(sentiments=str(s.sentiments))
                print(s.keywords(5))
            return HttpResponse("success")

    @csrf_exempt
    def getQuick(request):
        infos = UserInfo.objects.values("_id", "Image" ,"NickName")
        result = json.dumps(list(infos), cls=DjangoJSONEncoder)
        print(result)
        return JsonResponse(result, safe=False)

    @csrf_exempt
    def getComment(request):
        res = {}
        if request.method == "POST":
            text = request.POST.get("commentId")
            try:
                CommentWeiboInfo.objects.get(wb_id = text)
                res['ok'] = "数据库已存在该用户，开始返回数据"
                wbinfos = CommentWeiboInfo.objects.filter(wb_id=text)
                endTime = CommentInfo.objects.filter(CommentWeiboInfo_id=text).order_by("c_created_at")
                commentinfos = CommentInfo.objects.filter(CommentWeiboInfo_id=text).order_by("-c_like_num")
                res['data'] = serializers.serialize("json", wbinfos)
                res['info'] = serializers.serialize("json", commentinfos)
                for wbinfo in wbinfos:
                    start = wbinfo.wb_created_at
                for e in endTime:
                    end = e.c_created_at
                mid = (end - start)/10
                count1,count2,count3,count4,count5,count6,count7,count8,count9,count10 = 0,0,0,0,0,0,0,0,0,0
                c_content = ''
                for c in commentinfos:
                    c_content += c.c_text
                    if(c.c_created_at < start+mid):
                        count1 = count1 + 1
                    if(start+mid < c.c_created_at and c.c_created_at < start+2*mid):
                        count2 = count2 + 1
                    if(start+2*mid < c.c_created_at and c.c_created_at < start+3*mid):
                        count3 = count3 + 1
                    if(start+3*mid < c.c_created_at and c.c_created_at < start+4*mid):
                        count4 = count4 + 1
                    if(start+4*mid < c.c_created_at and c.c_created_at < start+5*mid):
                        count5 = count5 + 1
                    if(start+5*mid < c.c_created_at and c.c_created_at < start+6*mid):
                        count6 = count6 + 1
                    if(start+6*mid < c.c_created_at and c.c_created_at < start+7*mid):
                        count7 = count7 + 1
                    if(start+7*mid < c.c_created_at and c.c_created_at < start+8*mid):
                        count8 = count8 + 1
                    if(start+8*mid < c.c_created_at and c.c_created_at < start+9*mid):
                        count9 = count9 + 1
                    if(start+9*mid < c.c_created_at and c.c_created_at < start+10*mid):
                        count10 = count10 + 1
                c_content = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", c_content)
                wordlist_after_jieba = jieba.cut(c_content, cut_all=False)
                wl_space_split = (" ".join(wordlist_after_jieba))
                filepath = path.dirname(__file__) + '\stopword.txt'
                stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
                minganfilepath = path.dirname(__file__) + '\mingan.txt'
                minganwords = [line.strip() for line in open(minganfilepath, 'r', encoding='utf-8').readlines()]
                c=Counter()
                outstr = ''
                for word in wl_space_split:
                    if word not in stopwords:
                        if word != '\t'and'\n':
                            outstr += word 
                outstr = outstr.split(' ')
                while '' in outstr:
                    outstr.remove('')
                for word in outstr:
                    c[word] += 1
                cipin = list()
                li = list(c.items())
                li.sort(key=lambda x:x[1], reverse=True)
                mingancount = 0
                for (k, v) in li:
                    if k in minganwords:
                        mingancount += 1
                    cipin.append({"word":k,"count":v})
                res['mingan'] = mingancount/len(li)
                res['cipin'] = cipin
                # print('停用词前', wl_space_split)
                # print('停用词后', outstr)
                res['commentqushi'] = [
                    { 'date': json.dumps(start+mid, cls=JsonCustomEncoder), 'count': count1 },
                    { 'date': json.dumps(start+2*mid, cls=JsonCustomEncoder), 'count': count2 },
                    { 'date': json.dumps((start+3*mid), cls=JsonCustomEncoder), 'count': count3 },
                    { 'date': json.dumps((start+4*mid), cls=JsonCustomEncoder), 'count': count4 },
                    { 'date': json.dumps((start+5*mid), cls=JsonCustomEncoder), 'count': count5 },
                    { 'date': json.dumps((start+6*mid), cls=JsonCustomEncoder), 'count': count6 },
                    { 'date': json.dumps((start+7*mid), cls=JsonCustomEncoder), 'count': count7 },
                    { 'date': json.dumps((start+8*mid), cls=JsonCustomEncoder), 'count': count8 },
                    { 'date': json.dumps((start+9*mid), cls=JsonCustomEncoder), 'count': count9 },
                    { 'date': json.dumps((start+10*mid), cls=JsonCustomEncoder), 'count': count10 },
                    { 'date': json.dumps((start), cls=JsonCustomEncoder), 'count': max(count1, count2, count3, count4, count5, count6, count7, count8, count9, count10) }
                ]
                print(res['commentqushi'])
                return HttpResponse(json.dumps(res))
            except CommentWeiboInfo.DoesNotExist:
                resp = list(Target.objects.values('uid', 'cookie', 'add_time'))
                uid = int(resp[0]["uid"])
                cookie = {"Cookie": resp[0]["cookie"]}
                wb = Weibo(uid,cookie)
                print("数据库不存在该评论，正在爬虫生成")
                mm = wb.get_comment_info(text)
                res['ok'] = "数据库不存在该用户，爬虫返回数据"
                wbinfos = CommentWeiboInfo.objects.filter(wb_id=text)
                endTime = CommentInfo.objects.filter(CommentWeiboInfo_id=text).order_by("c_created_at")
                commentinfos = CommentInfo.objects.filter(CommentWeiboInfo_id=text).order_by("-c_like_num")
                res['data'] = serializers.serialize("json", wbinfos)
                res['info'] = serializers.serialize("json", commentinfos)
                for wbinfo in wbinfos:
                    start = wbinfo.wb_created_at
                for e in endTime:
                    end = e.c_created_at
                mid = (end - start)/10
                count1,count2,count3,count4,count5,count6,count7,count8,count9,count10 = 0,0,0,0,0,0,0,0,0,0
                c_content = ''
                for c in commentinfos:
                    c_content += c.c_text
                    if(c.c_created_at < start+mid):
                        count1 = count1 + 1
                    if(start+mid < c.c_created_at and c.c_created_at < start+2*mid):
                        count2 = count2 + 1
                    if(start+2*mid < c.c_created_at and c.c_created_at < start+3*mid):
                        count3 = count3 + 1
                    if(start+3*mid < c.c_created_at and c.c_created_at < start+4*mid):
                        count4 = count4 + 1
                    if(start+4*mid < c.c_created_at and c.c_created_at < start+5*mid):
                        count5 = count5 + 1
                    if(start+5*mid < c.c_created_at and c.c_created_at < start+6*mid):
                        count6 = count6 + 1
                    if(start+6*mid < c.c_created_at and c.c_created_at < start+7*mid):
                        count7 = count7 + 1
                    if(start+7*mid < c.c_created_at and c.c_created_at < start+8*mid):
                        count8 = count8 + 1
                    if(start+8*mid < c.c_created_at and c.c_created_at < start+9*mid):
                        count9 = count9 + 1
                    if(start+9*mid < c.c_created_at and c.c_created_at < start+10*mid):
                        count10 = count10 + 1
                c_content = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", c_content)
                wordlist_after_jieba = jieba.cut(c_content, cut_all=False)
                wl_space_split = (" ".join(wordlist_after_jieba))
                filepath = path.dirname(__file__) + '\stopword.txt'
                stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
                minganfilepath = path.dirname(__file__) + '\mingan.txt'
                minganwords = [line.strip() for line in open(minganfilepath, 'r', encoding='utf-8').readlines()]
                c=Counter()
                outstr = ''
                for word in wl_space_split:
                    if word not in stopwords:
                        if word != '\t'and'\n':
                            outstr += word 
                outstr = outstr.split(' ')
                while '' in outstr:
                    outstr.remove('')
                for word in outstr:
                    c[word] += 1
                cipin = list()
                li = list(c.items())
                li.sort(key=lambda x:x[1], reverse=True)
                mingancount = 0
                for (k, v) in li:
                    if k in minganwords:
                        mingancount += 1
                    cipin.append({"word":k,"count":v})
                res['mingan'] = mingancount/len(li)
                res['cipin'] = cipin
                # print('停用词前', wl_space_split)
                # print('停用词后', outstr)
                res['commentqushi'] = [
                    { 'date': json.dumps(start+mid, cls=JsonCustomEncoder), 'count': count1 },
                    { 'date': json.dumps(start+2*mid, cls=JsonCustomEncoder), 'count': count2 },
                    { 'date': json.dumps((start+3*mid), cls=JsonCustomEncoder), 'count': count3 },
                    { 'date': json.dumps((start+4*mid), cls=JsonCustomEncoder), 'count': count4 },
                    { 'date': json.dumps((start+5*mid), cls=JsonCustomEncoder), 'count': count5 },
                    { 'date': json.dumps((start+6*mid), cls=JsonCustomEncoder), 'count': count6 },
                    { 'date': json.dumps((start+7*mid), cls=JsonCustomEncoder), 'count': count7 },
                    { 'date': json.dumps((start+8*mid), cls=JsonCustomEncoder), 'count': count8 },
                    { 'date': json.dumps((start+9*mid), cls=JsonCustomEncoder), 'count': count9 },
                    { 'date': json.dumps((start+10*mid), cls=JsonCustomEncoder), 'count': count10 },
                    { 'date': json.dumps((start), cls=JsonCustomEncoder), 'count': max(count1, count2, count3, count4, count5, count6, count7, count8, count9, count10) }
                ]
                print(res['commentqushi'])
                return HttpResponse(json.dumps(res))

        if request.method == "GET":
            text = request.GET.get("commentId")
            qqq = CommentInfo.objects.filter(c_text='').delete()
            infos = CommentInfo.objects.filter(CommentWeiboInfo_id=text).values('c_text')
            sentimentslist = []
            for info in infos:
                m = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \” \? \@]", "", info['c_text'])
                if m:
                    s = SnowNLP(m)
                    sentimentslist.append(s.sentiments)
            # print(sentimentslist)
            c = Counter()
            for word in sentimentslist:
                c[word] += 1
            # qgnum = list()
            li = list(c.items())
            li.sort(key=lambda x:x[0])
            return HttpResponse(json.dumps(li))
            
    @csrf_exempt
    def getWeibo(request):
        infos = CommentWeiboInfo.objects.values("wb_id", "wb_userId", "wb_userName" ,"wb_user_profile_image_url", "wb_text")
        result = json.dumps(list(infos), cls=DjangoJSONEncoder)
        print(result)
        return JsonResponse(result, safe=False)

#日期转化代码
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):          
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)
