from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .snownlp import SnowNLP
from .snownlp import sentiment

import re

class SnowNLPWeibo:
    def SnowNLPAPI(request):
        if request.method == "GET":
            text = request.GET.get("snownlp")
            print(text)
        s = SnowNLP(text)
        result = {}
        myset = set()
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z]")
        text = cop.sub('', text)
        for ch in text:
            if ch in myset:
                pass
            else:
                myset.add(ch)
        for ch in myset:
            result[ch]=text.count(ch)
        result = sorted(result.items(),key = lambda x:x[1],reverse = True)
        mm = {
            'sentiments': s.sentiments,
            'keywords' : s.keywords(3),
            'tf': result,
            'words': s.words,
            'sentences': s.sentences,
            'tf2': s.tf,
            'idf': s.idf,
            # 'sim': s.sim,
            # 'summary': s.summary
            # 'tags': s.tags
        }
        return JsonResponse(mm)
