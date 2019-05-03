from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import Target, UserInfo, TweetsInfo
from collections import Counter
from src.SnowNLPAPI.snownlp import SnowNLP
from src.SnowNLPAPI.snownlp import sentiment
from os import path
# Create your views here.
import requests
import json
import re
import jieba


class ScrapydWeibo:
    @csrf_exempt
    def ScrapydAPI(request):
        if request.method == "POST":
            ids = request.POST.get("weiboIds").split(',')
            cookies = request.POST.get("cookies")
            target_list_to_insert = list()
            for id in ids:
                target = Target()
                target.uid = id
                target.cookie = cookies
                try:
                    Target.objects.filter(isScrapy=0).update(cookie=cookies)
                    Target.objects.get(uid = target.uid)
                    print("该用户已存在数据库")
                except Target.DoesNotExist:
                    target_list_to_insert.append(target)
            Target.objects.bulk_create(target_list_to_insert)
            print(ids,cookies)
            url = 'http://localhost:6800/schedule.json'
            data = {'project':'bot', 'spider':'weibo_spider'}
            schedule = requests.post(url=url,data=data)
            return HttpResponse(schedule)
        if request.method == "GET":
            requrl = "http://localhost:6800/daemonstatus.json"
            result = requests.get(requrl)
            return HttpResponse(result)

    @csrf_exempt
    def CancelScrapyd(request):
        if request.method == "POST":
            jobId = request.POST.get("job")
            url = "http://localhost:6800/cancel.json"
            data = {'project':'bot', 'job': jobId}
            result = requests.post(url=url,data=data)
            return HttpResponse(result)

    @csrf_exempt
    def getLasted(request):
        infos = UserInfo.objects.values("_id", "Image" , "nick_name").order_by('crawl_time')
        user = json.dumps(list(infos), cls=DjangoJSONEncoder)
        targets = Target.objects.values("uid", "group")
        target = json.dumps(list(targets), cls=DjangoJSONEncoder)
        c=Counter()
        for word in targets:
            print(word['group'])
            c[word['group']] += 1
        li = list(c.items())
        li.sort(key=lambda x:x[0])
        result = {
            'user': user,
            'target': target,
            'count': json.dumps(li)
        }
        print(result)
        return JsonResponse(result, safe=False)

    @csrf_exempt
    def getGroupInfo(request):
        result = []
        if request.method == "POST":
            ids = request.POST.get("weiboIds").split(',')
            for id in ids:
                alluser = UserInfo.objects.filter(_id=id)
                # alltweets = TweetsInfo.objects.filter(user_id=id)
                result.append({
                    'user': serializers.serialize('json',alluser)
                    # 'alltweets': serializers.serialize('json',alltweets)
                })
            return JsonResponse(result, safe=False)
        
        if request.method == "GET":
            ids = request.GET.get("weiboIds").split(',')
            qqq = TweetsInfo.objects.filter(content='').delete()
            filepath = path.dirname(__file__) + '\stopword.txt'
            stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
            minganfilepath = path.dirname(__file__) + '\mingan.txt'
            minganwords = [line.strip() for line in open(minganfilepath, 'r', encoding='utf-8').readlines()]
            sentimentslist = []
            content = ''
            for id in ids:
                infos = TweetsInfo.objects.filter(user_id=id).values('content')
                for info in infos:
                    content += info['content']
                    m = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \” \? \@]", "", info['content'])
                    if m:
                        s = SnowNLP(m)
                        sentimentslist.append(s.sentiments)
            c0 = Counter()
            for word0 in sentimentslist:
                c0[word0] += 1
            li0 = list(c0.items())
            li0.sort(key=lambda x:x[0])
            content = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", content)
            wordlist_after_jieba = jieba.cut(content, cut_all=False)
            wl_space_split = (" ".join(wordlist_after_jieba))
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
            res = {
                "mingan": mingancount/len(li),
                "cipin": cipin[:200],
                "analy": li0
            }
            return JsonResponse(res, safe=False)