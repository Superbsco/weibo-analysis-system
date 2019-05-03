from django.test import TestCase
import urllib
from os import path
import os


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
        pass
        # all = TweetsInfo.objects.filter(UserInfo_id=text)
        # for e in all:
        #     mm = ()
        #     s = SnowNLP(e.Content.replace('转发理由','').replace('转发内容', '').replace('原始用户', '').replace('转发微博已被删除', ''))
        #     for i in s.tags:
        #         mm += i
        #     TweetsInfo.objects.filter(_id=e._id).update(tags=s.keywords(5))
        #     TweetsInfo.objects.filter(_id=e._id).update(pinyin=mm)
        #     TweetsInfo.objects.filter(_id=e._id).update(sentiments=str(s.sentiments))
        #     print(s.keywords(5))
        # else:
        #     text = "输入微博Id错误，请重新输入！"
        #     res['ok'] = text
        # try:
        # resp = Target.objects.values('uid','cookie','add_time')
        # resp = json.dumps(resp,cls=JsonCustomEncoder)
        # resp = serializers.serialize("json", Target.objects.all().order_by("-id")[:1])
        # wb = Weibo(uid,cookie)
        # mm = wb.get_comment_info('4358934418168720')
        # mm = wb.get_weibo_info()
        # mm = wb.getTest()
        # except Exception as e:
        #     return HttpResponse('拉取数据库数据失败: %s' % e)

    @csrf_exempt
    def WordCloudAPI(request):
        # ImgInfo.objects.filter(UserInfo_id=text).update(wordcloud=res)
        # print("更新完毕~~")
        # wordlist_after_jieba = jieba.cut(content, cut_all=False)
        # wl_space_split = " ".join(wordlist_after_jieba)
        # backgroud_Image = plt.imread(path.dirname(__file__) + '\color.png')
        # '''设置词云样式'''
        # stopwords = STOPWORDS.copy()
        # stopwords.add("哈哈") #可以加多个屏蔽词
        # wc = WordCloud(
        #     width=770,
        #     height=1200,
        #     background_color='white',# 设置背景颜色
        #     # mask=backgroud_Image,# 设置背景图片
        #     font_path=path.dirname(__file__) + '\simkai.ttf',  # 设置中文字体，若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        #     max_words=600, # 设置最大现实的字数
        #     stopwords=stopwords,# 设置停用词
        #     max_font_size=400,# 设置字体最大值
        #     random_state=50,# 设置有多少种随机生成状态，即有多少种配色方案
        # )
        # wc.generate_from_text(wl_space_split)#开始加载文本
        # img_colors = ImageColorGenerator(backgroud_Image)
        # wc.recolor(color_func=img_colors)#字体颜色为背景图片的颜色
        # d = path.dirname(__file__)
        # wc.to_file(path.join(d, "wc.jpg"))
        # print('生成词云成功!')
        # with open(path.dirname(__file__) + '\wc.jpg', 'rb') as f:
        #     base64_data = base64.b64encode(f.read())
        #     url = base64_data.decode()
        pass

    @csrf_exempt
    def getComment(request):
        pass
        # if request.method == "GET":
        # text = request.GET.get("commentId")
        # resp = list(Target.objects.values('uid', 'cookie', 'add_time'))
        # uid = int(resp[0]["uid"])
        # cookie = {"Cookie": resp[0]["cookie"]}
        # wb = Weibo(uid,cookie)
        # print("数据库不存在该评论，正在爬虫生成")
        # mm = wb.get_comment_info(text)


      
# Create your tests here.
# with urllib.request.urlopen("https://wx2.sinaimg.cn/large/" + '893ea4cely1g2kbqkzuzyj21hc0u0q9p', timeout=30) as response, open("893ea4cely1g2kbqkzuzyj21hc0u0q9p.jpg", 'wb') as f_save:
#     f_save.write(response.read())
#     f_save.flush()
#     f_save.close()
# print (path.dirname(path.abspath("__file__")))
# print (path.pardir)
# print (path.join(path.dirname("__file__"),path.pardir))
# print (path.abspath(path.join(path.dirname("__file__"),path.pardir)))
# print (path.abspath(path.join(os.getcwd(), "../../webview/static/")))
filepath = path.abspath(path.join(os.getcwd(), "../../webview/static"))
wb_pic_ids = ["76643ed5gy1g2ha4hqv3tj20yi0orjx7","76643ed5gy1g2ha4hyn71j20u01400zc","76643ed5gy1g2ha4i709zj20u01hcq64","76643ed5gy1g2ha4icy5mj20rf1cbwgt"]
for wb_pic_id in wb_pic_ids:
    with urllib.request.urlopen("https://wx2.sinaimg.cn/large/" + wb_pic_id, timeout=30) as response, open(filepath +"/"+ wb_pic_id+".jpg", 'wb') as f_save:
        print("下载图片%s" % wb_pic_id)
        f_save.write(response.read())
        f_save.flush()
        f_save.close()