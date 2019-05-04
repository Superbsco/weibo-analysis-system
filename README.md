## weibo-analysis-system 
`毕业设计`：微博用户情感分析系统

### 1、系统介绍（2019.5.4毕设已完成）：

> extra_apps：xadmin后台管理系统

> scrapydserver：Scrapy爬虫

> src：django app里面写接口

> webview：前端Vue代码

> weibosystem：django wsgi/url等配置

#### 1、系统技术架构介绍

> 前端使用：vue-cli + vue + vuex + axios

> 后端使用：python + django + xadmin + request + scrapy + scrapyd + snownlp（模型已训练好，但并不是特别准确）

#### 2、系统功能介绍

> ① 输入微博oid，爬取个人微博信息，情感分析处理后并展示（oid获取方式，进入个人微博首页如： https://weibo.com/u/1797112632 ，其中`1797112632`就是oid。）有些用户自定义了域名，右击查看网页源代码，搜索`['oid']`即可找到oid。下图是本系统爬取个人信息界面：

![个人微博爬虫前端主界面](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/1.png?raw=true)

![个人微博爬虫前端信息展示](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/3.png?raw=true)

> ② 输入单条微博id，爬取个人微博信息（获取单条微博id的方式，打开微博客户端，随便找到一条微博，进入微博正文，点击右上角三个点，然后可以看到分享给微信好友，QQ好友等，在下面一栏有收藏等，往右边拖，找到复制链接，复制并粘贴出来。如 https://m.weibo.cn/1769965211/4366947749433348 ，其中`4366947749433348`就是单条微博id。）情感分析处理后并展示。本系统展示单条微博例子如下：

![单条微博爬虫前端信息展示](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/4.png?raw=true)

> ③ 输入微博id，或者多个微博id和Cookie启动持续爬虫。前提先运行Scrapyd服务。这个功能使用Scrpay爬虫，然后把数据存到Django的Model中。

![多用户爬虫启动](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/7.png?raw=true)

> ④ 独立出来的文本情感分析API，输入任意一段中文，返回情感分析值，词频，关键词。

![独立爬虫API](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/8.png?raw=true)

> ⑤ 数据库已爬虫的用户，其中持续爬虫模块点击进去就是③中的多用户爬虫，默认设置了组别是1，如需修改进入xadmin后台，修改即可，上面的点击个人账号，点击单条微博，也是进入信息展示界面。点击组别进入的多用户爬虫界面如下图：

![已爬虫用户](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/2.png?raw=true)

![多用户爬虫展示](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/5.png?raw=true)

> ⑥ xadmin后台管理系统

![xadmin后台管理系统](https://github.com/Superbsco/weibo-analysis-system/blob/master/pic/6.png?raw=true)

### 2、系统启动注意事项

[参考技术文档](https://github.com/Superbsco/weibo-analysis-system/blob/master/%E6%8A%80%E6%9C%AF%E6%96%87%E6%A1%A3%E8%AF%B4%E6%98%8E.md)

按照技术文档按照完了之后，workon进入虚拟环境：

####1、数据库自动生成，使用如下命令：

```python
python manage.py makgrations
python manage.py migrate
```

####2、初始化Cookies
爬虫之前一定要先进入xadmin后台，使用数据库自动生成后，xadmin的登录账号密码就没了，参考这里初始化账号：https://blog.csdn.net/a_little_snail/article/details/76984933 ，
然后重设Cookie，获取新浪微博Cookie，可参考 https://blog.csdn.net/A_xiao_mili/article/details/77947802 这里。




