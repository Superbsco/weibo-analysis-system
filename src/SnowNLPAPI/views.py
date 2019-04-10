from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .snownlp import SnowNLP
from .snownlp import sentiment


class SnowNLPWeibo:
    def SnowNLPAPI(request):
        if request.method == "GET":
            text = request.GET.get("snownlp")
        s = SnowNLP(text)
        mm = s.sentiments
        return HttpResponse(mm)
