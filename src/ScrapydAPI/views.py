from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests

class ScrapydWeibo:
    def ScrapydAPI(request):
        url = 'http://localhost:6800/schedule.json'
        data = {'project':'bot', 'spider':'weibo_spider'}
        requests.post(url=url,data=data)
        # requrl = "http://localhost:6800/schedule.json?project=bot"
        # print(requests.get(requrl))
        requrl = "http://localhost:6800/listjobs.json?project=bot"
        

        return HttpResponse(requests.get(requrl))