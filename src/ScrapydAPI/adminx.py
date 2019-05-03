import xadmin

from xadmin import views
# here put the import lib
from .models import Target, UserInfo, TweetsInfo, RelationshipsInfo, CommentInfo


class TargetAdmin(object):
  list_display = ['uid', 'cookie', 'isScrapy', 'group', 'add_time']
  search_fields = ['uid', 'cookie', 'isScrapy', 'group', 'add_time']
  list_filter = ['uid', 'cookie', 'isScrapy', 'group', 'add_time']


class UserInfoAdmin(object):
  list_display = ['_id', 'nick_name', 'Image', 'gender', 'labels', 'province', 'city', 'brief_introduction', 'birthday', 'constellation',
                    'tweets_num', 'fans_num','follows_num', 'sex_orientation', 'sentiment', 'vip_level', 'authentication', 'person_url', 'crawl_time']
  search_fields = ['_id', 'nick_name', 'Image', 'gender', 'labels', 'province', 'city', 'brief_introduction', 'birthday', 'constellation',
                    'tweets_num', 'fans_num','follows_num', 'sex_orientation', 'sentiment', 'vip_level', 'authentication', 'person_url', 'crawl_time']
  list_filter = ['_id', 'nick_name', 'Image', 'gender', 'labels', 'province', 'city', 'brief_introduction', 'birthday', 'constellation',
                    'tweets_num', 'fans_num','follows_num', 'sex_orientation', 'sentiment', 'vip_level', 'authentication', 'person_url', 'crawl_time']


class TweetsInfoAdmin(object):
  list_display = ['user_id', '_id', 'content', 'created_at', 'weibo_url', 'like_num', 'comment_num', 'repost_num', 'crawl_time']
  search_fields = ['user_id', '_id', 'content', 'created_at', 'weibo_url', 'like_num', 'comment_num', 'repost_num', 'crawl_time']
  list_filter = ['user_id', '_id', 'content', 'created_at', 'weibo_url', 'like_num', 'comment_num', 'repost_num', 'crawl_time']


class RelationshipsInfoAdmin(object):
  list_display = ['_id', 'fan_id', 'followed_id', 'crawl_time']
  search_fields = ['_id', 'fan_id', 'followed_id', 'crawl_time']
  list_filter = ['_id', 'fan_id', 'followed_id', 'crawl_time']


class CommentInfoAdmin(object):
  list_display = ['_id', 'comment_user_id', 'weibo_url', 'content', 'created_at', 'crawl_time']
  search_fields = ['_id', 'comment_user_id', 'weibo_url', 'content', 'created_at', 'crawl_time']
  list_filter = ['_id', 'comment_user_id', 'weibo_url', 'content', 'created_at', 'crawl_time']


xadmin.site.register(Target, TargetAdmin)
xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(TweetsInfo, TweetsInfoAdmin)
xadmin.site.register(RelationshipsInfo, RelationshipsInfoAdmin)
xadmin.site.register(CommentInfo, CommentInfoAdmin)