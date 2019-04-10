from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# -*- utf-8 -*-
from datetime import datetime

from django.db import models

# Create your models here.
class Target(models.Model):
    uid = models.CharField(max_length=20, verbose_name=u"爬取用户")
    cookie = models.TextField(verbose_name=u"设置cookie")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"爬虫初始"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.uid)


class UserInfo(models.Model):
    """ 个人信息 """
    _id = models.CharField(max_length=200, verbose_name=u"用户id", primary_key=True)  # 用户ID
    # Image = models.TextField(verbose_name=u"用户头像", blank=True)  # 用户头像
    nick_name = models.CharField(max_length=30, verbose_name=u"昵称") #昵称
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female",verbose_name=u"性别") # 性别
    labels = models.CharField(max_length=500, verbose_name=u"标签", blank=True)  # 所在省
    province = models.CharField(max_length=30, verbose_name=u"所在省", blank=True)  # 所在省
    city = models.CharField(max_length=30, verbose_name=u"所在城市", blank=True)  # 所在城市
    brief_introduction = models.CharField(max_length=500, verbose_name=u"简介", blank=True)  # 简介
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)  # 生日
    constellation = models.CharField(max_length=30, verbose_name=u"星座", blank=True)  # 所在城市
    tweets_num = models.IntegerField(default=0, verbose_name=u'微博数')  # 微博数
    fans_num = models.IntegerField(default=0, verbose_name=u'关注数')  # 关注数
    follows_num = models.IntegerField(default=0, verbose_name=u'粉丝数', blank=True)  # 粉丝数
    sex_orientation = models.CharField(max_length=30, verbose_name=u"性取向", blank=True)  # 性取向
    sentiment = models.CharField(max_length=30, verbose_name=u"感情状况", blank=True)  # 感情状况
    vip_level = models.CharField(max_length=30, verbose_name=u"会员等级", blank=True)  # 会员等级
    authentication = models.CharField(max_length=30, verbose_name=u"认证", blank=True)  # 认证
    person_url = models.CharField(max_length=30, verbose_name=u"首页链接", blank=True)  # 首页链接
    crawl_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.NickName) 


class TweetsInfo(models.Model):
    """ 微博信息 """
    _id = models.CharField(max_length=50, verbose_name=u"微博ID", primary_key=True)  # 微博内容ID标签
    user_id = models.CharField(max_length=200, verbose_name=u"用户信息")  # 用户信息
    content = models.TextField(verbose_name=u"微博内容")  # 微博内容
    created_at = models.DateTimeField(verbose_name=u"发表时间", blank=True)  # 发表时间
    weibo_url = models.TextField(verbose_name=u"weibo的URL", blank=True)
    # Co_oridinates = models.CharField(max_length=300, verbose_name=u"定位坐标", blank=True)  # 定位坐标
    # Tools = models.CharField(max_length=300, verbose_name=u"发布工具", blank=True)  # 发布工具/平台
    like_num = models.IntegerField(default=0, verbose_name=u'点赞数', blank=True)  # 点赞数
    comment_num = models.IntegerField(default=0, verbose_name=u'评论数', blank=True)  # 评论数
    repost_num = models.IntegerField(default=0, verbose_name=u'转载数', blank=True)  # 转载数
    crawl_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
    class Meta:
        verbose_name = u"微博信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.user_id) 

class RelationshipsInfo(models.Model):
    _id = models.CharField(max_length=50, verbose_name=u"用户关系ID", primary_key=True)
    fan_id = models.CharField(max_length=50, verbose_name=u"关注者的用户ID")
    followed_id = models.CharField(max_length=50, verbose_name=u"被关注者的用户ID")
    crawl_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户关系"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "{0}".format(self._id) 

class CommentInfo(models.Model):
    _id = models.CharField(max_length=50, verbose_name=u"评论的ID", primary_key=True)
    comment_user_id	= models.CharField(max_length=50, verbose_name=u"评论的用户ID")
    weibo_url = models.TextField(verbose_name=u"weibo的URL", blank=True)
    content = models.TextField(verbose_name=u"评论内容", blank=True)
    created_at = models.CharField(max_length=30, verbose_name=u"评论创建时间", blank=True)
    crawl_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"评论内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.comment_user_id) 