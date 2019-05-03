#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   adminx.py
@Time    :   2019/03/27 14:21:20
@Author  :   hsp 
@Desc    :   None
'''
import xadmin
from xadmin import views
# here put the import lib
from .models import Target, UserInfo, TweetsInfo, CommentWeiboInfo, CommentInfo, ImgInfo


class TargetAdmin(object):
  list_display = ['uid', 'cookie', 'add_time']
  search_fields = ['uid', 'cookie', 'add_time']
  list_filter = ['uid', 'cookie', 'add_time']


class UserInfoAdmin(object):
  list_display = ['_id', 'Image', 'NickName', 'Gender', 'Province', 'City', 'BriefIntroduction', 'Birthday', 'Constellation',
                    'Num_Tweets', 'Num_Follows','Num_Fans', 'SexOrientation', 'Sentiment', 'VIPlevel', 'Authentication', 'URL']
  search_fields = ['_id', 'Image', 'NickName', 'Gender', 'Province', 'City', 'BriefIntroduction', 'Birthday', 'Constellation',
                    'Num_Tweets', 'Num_Follows','Num_Fans', 'SexOrientation', 'Sentiment', 'VIPlevel', 'Authentication', 'URL']
  list_filter = ['_id', 'Image', 'NickName', 'Gender', 'Province', 'City', 'BriefIntroduction', 'Birthday', 'Constellation',
                    'Num_Tweets', 'Num_Follows','Num_Fans', 'SexOrientation', 'Sentiment', 'VIPlevel', 'Authentication', 'URL']


class TweetsInfoAdmin(object):
  list_display = ['UserInfo', '_id', 'Content', 'PubTime', 'Co_oridinates', 'Tools', 'Like', 'Comment', 'Transfer','Content', 'tags', 'pinyin', 'sentiments', 'crawl_time']
  search_fields = ['UserInfo__NickName', '_id', 'Content', 'PubTime', 'Co_oridinates', 'Tools', 'Like', 'Comment', 'Transfer','Content', 'tags', 'pinyin', 'sentiments', 'crawl_time'] 
  list_filter = ['UserInfo', '_id', 'Content', 'PubTime', 'Co_oridinates', 'Tools', 'Like', 'Comment', 'Transfer','Content', 'tags', 'pinyin', 'sentiments', 'crawl_time']

class CommentWeiboInfoAdmin(object):
  list_display = ['wb_id', 'wb_userId', 'wb_userName', 'wb_user_profile_image_url', 'wb_created_at', 'wb_source', 
                    'wb_text', 'wb_pic_ids', 'wb_reposts', 'wb_comments', 'wb_like']
  search_fields =  ['wb_id', 'wb_userId', 'wb_userName', 'wb_user_profile_image_url', 'wb_created_at', 'wb_source', 
                    'wb_text', 'wb_pic_ids', 'wb_reposts', 'wb_comments', 'wb_like']
  list_filter =  ['wb_id', 'wb_userId', 'wb_userName', 'wb_user_profile_image_url', 'wb_created_at', 'wb_source', 
                    'wb_text', 'wb_pic_ids', 'wb_reposts', 'wb_comments', 'wb_like']

class CommentInfoAdmin(object):
    list_display = ['CommentWeiboInfo', 'c_id', 'c_created_at', 'c_source', 'c_text', 
                    'c_like_num', 'c_userId', 'c_user_name', 'C_profile_image_url', 'C_profile_url']
    search_fields =  ['CommentWeiboInfo__wb_userName', 'c_id', 'c_created_at', 'c_source', 'c_text', 
                    'c_like_num', 'c_userId', 'c_user_name', 'C_profile_image_url', 'C_profile_url']
    list_filter = ['CommentWeiboInfo', 'c_id', 'c_created_at', 'c_source', 'c_text', 
                    'c_like_num', 'c_userId', 'c_user_name', 'C_profile_image_url', 'C_profile_url']

class ImgInfoAdmin(object):
    list_display = ['UserInfo', 'wordcloud']    
    search_fields =  ['UserInfo__NickName', 'wordcloud']
    list_filter = ['UserInfo', 'wordcloud'] 

class BaseSetting(object):
  enable_themes = True
  use_bootswatch = True


class GlobalSettings(object):
  site_title = u"微博用户情感分析系统后台"
  site_footer = u"微博用户情感分析系统"
  menu_style = "accordion"


xadmin.site.register(Target, TargetAdmin)
xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(TweetsInfo, TweetsInfoAdmin)
xadmin.site.register(CommentWeiboInfo, CommentWeiboInfoAdmin)
xadmin.site.register(CommentInfo, CommentInfoAdmin)
xadmin.site.register(ImgInfo, ImgInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)