# -*- utf-8 -*-
from datetime import datetime

from django.db import models

# Create your models here.
class Target(models.Model):
    uid = models.CharField(max_length=20, verbose_name=u"爬取用户")
    cookie = models.TextField(verbose_name=u"设置cookie")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"爬虫设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.uid)


class UserInfo(models.Model):
    """ 个人信息 """
    _id = models.CharField(max_length=20, verbose_name=u"用户id", primary_key=True)  # 用户ID
    Image = models.TextField(verbose_name=u"用户头像")  # 用户头像
    NickName = models.CharField(max_length=30, verbose_name=u"昵称") #昵称
    Gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female",verbose_name=u"性别") # 性别
    Province = models.CharField(max_length=30, verbose_name=u"所在省", blank=True)  # 所在省
    City = models.CharField(max_length=30, verbose_name=u"所在城市", blank=True)  # 所在城市
    BriefIntroduction = models.CharField(max_length=500, verbose_name=u"简介", blank=True)  # 简介
    Birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)  # 生日
    Constellation = models.CharField(max_length=30, verbose_name=u"星座", blank=True)  # 所在城市
    Num_Tweets = models.IntegerField(default=0, verbose_name=u'微博数')  # 微博数
    Num_Follows = models.IntegerField(default=0, verbose_name=u'关注数')  # 关注数
    Num_Fans = models.IntegerField(default=0, verbose_name=u'粉丝数', blank=True)  # 粉丝数
    SexOrientation = models.CharField(max_length=30, verbose_name=u"性取向", blank=True)  # 性取向
    Sentiment = models.CharField(max_length=30, verbose_name=u"感情状况", blank=True)  # 感情状况
    VIPlevel = models.CharField(max_length=30, verbose_name=u"会员等级", blank=True)  # 会员等级
    Authentication = models.CharField(max_length=30, verbose_name=u"认证", blank=True)  # 认证
    URL = models.CharField(max_length=30, verbose_name=u"首页链接", blank=True)  # 首页链接
    
    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}".format(self.NickName) 


class TweetsInfo(models.Model):
    """ 微博信息 """
    _id = models.CharField(max_length=50, verbose_name=u"微博ID", primary_key=True)  # 微博内容ID标签
    UserInfo = models.ForeignKey(UserInfo, verbose_name=u"用户信息", on_delete=models.CASCADE)  # 用户信息
    Content = models.TextField(verbose_name=u"微博内容")  # 微博内容
    PubTime = models.DateTimeField(verbose_name=u"发表时间", blank=True)  # 发表时间
    Co_oridinates = models.CharField(max_length=300, verbose_name=u"定位坐标", blank=True)  # 定位坐标
    Tools = models.CharField(max_length=300, verbose_name=u"发布工具", blank=True)  # 发布工具/平台
    Like = models.IntegerField(default=0, verbose_name=u'点赞数', blank=True)  # 点赞数
    Comment = models.IntegerField(default=0, verbose_name=u'评论数', blank=True)  # 评论数
    Transfer = models.IntegerField(default=0, verbose_name=u'转载数', blank=True)  # 转载数

    class Meta:
        verbose_name = u"微博信息"
        verbose_name_plural = verbose_name

class CommentWeiboInfo(models.Model):
    """ 评论信息 """
    wb_id = models.CharField(max_length=50, verbose_name=u"微博的ID", primary_key=True)
    wb_userId = models.CharField(max_length=50, verbose_name=u"微博用户的ID")
    wb_userName = models.CharField(max_length=50, verbose_name=u"微博用户的昵称")
    wb_user_profile_image_url = models.TextField(verbose_name=u"微博用户的头像")
    wb_created_at = models.DateTimeField(verbose_name=u"微博创建时间", blank=True)
    wb_source = models.TextField(verbose_name=u"微博来源", blank=True)
    wb_text = models.TextField(verbose_name=u"微博内容")
    wb_pic_ids = models.TextField(verbose_name=u"微博图片", blank=True)
    wb_reposts = models.IntegerField(default=0, verbose_name=u'转载数', blank=True)
    wb_comments = models.IntegerField(default=0, verbose_name=u'评论数', blank=True)

    class Meta:
        verbose_name = u"微博评论"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{0}".format(self.wb_userName) 

class CommentInfo(models.Model):
    CommentWeiboInfo = models.ForeignKey(CommentWeiboInfo, verbose_name=u"微博用户信息", on_delete=models.CASCADE)  # 用户信息
    c_id = models.CharField(max_length=50, verbose_name=u"评论的ID", primary_key=True)
    c_created_at = models.DateTimeField(verbose_name=u"评论创建时间", blank=True)
    c_source = models.TextField(verbose_name=u"评论的来源", blank=True)
    c_text = models.TextField(verbose_name=u"评论的内容", blank=True)
    c_like_num = models.IntegerField(default=0, verbose_name=u'评论点赞数', blank=True) 
    c_userId = models.CharField(max_length=50, verbose_name=u"评论用户的微博ID", blank=True)
    c_user_name = models.CharField(max_length=300, verbose_name=u"评论用户的微博昵称", blank=True)
    C_profile_image_url = models.TextField(verbose_name=u"评论用户的头像", blank=True)
    C_profile_url = models.TextField(verbose_name=u"评论用户的主页", blank=True)

    class Meta:
        verbose_name = u"评论详情"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "{0}".format(self.CommentWeiboInfo) 