## weibo-analysis-system 
`毕业设计`：微博用户情感分析系统`

为了方便后续的毕业论文的书写，这里详细从0开始记下每一个步骤：

### 1、准备工作：
① 预先使用安装好python3.6.3|Aanconda版

② 预先装好vue2.5.2版

③ 安装virtualenv虚拟环境

```python
pip install virtualenv
```

④ 安装virtualenvrapper方便进入虚拟环境，因为直接用virtualenv进入太麻烦了

```python
pip install virtualenvrapper-win
```

⑤ 接着安装虚拟环境：

```python
mkvirtualenv weibo-analysis-system
```

> 这里解释一下virtualenvrapper的命令：

> 创建基本环境：mkvirtualenv [环境名]

> 删除环境：rmvirtualenv [环境名]

> 激活环境：workon [环境名]

> 退出环境：deactivate

> 列出所有环境：workon 或者 lsvirtualenv -b

⑥ 进入python虚拟环境

```python
workon weibo-analysis-system
```

⑦ 安装包

```python
pip install requirements.txt #安装各种包
```

### 2、进入正题

① 创建Django项目

```python
django-admin startproject weibo-analysis-system
```

② 进入根目录创建一个APP作为后端API

```python
python manage.py startapp src
```

③ 进入weibo-analysis-system根目录安装vue

```
vue-cli webpack webview
```

④ 使用webpack打包vue.js

```
cd webview
```

```
npm install
```

```
npm run build
```

⑤ 修改weibosystem的urls，使得已进入django就是vue的主页

```python
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^api/', include('src.urls', namespace='api'))
]
```

⑥ 修改setting让django知道从哪里找index.html

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['webview/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

⑦配置静态文件搜索路径，即css+js在哪

```python
STATICFILES_DIRS = [             ## 添加静态文件路径
    os.path.join(BASE_DIR, "webview/dist/static"),
]
```

### 3、开发环境配置

因为使用了Django作为后端，每次修改了前端之后都要重新构建。
除了使用Django作为后端，还可以在dist目录下面运行以下命令(即: http server)来看效果：

```python
hs
```

但是问题依然没有解决，我想过检测文件变化来自动构建，但是构建是秒级的，
太慢了，所以我直接使用Vue.js的开发环境来调试。

```python
npm run dev
```

毫秒级，但是有个新问题，使用Vue.js的开发环境脱离了Django环境，访问Django写的API，
出现了跨域问题，有两种方法解决，一种是在Vue.js层上做转发（proxyTable），
另一种是在Django层注入header，这里我使用后者，
用Django的第三方包 django-cors-headers 来解决跨域问题。

进入虚拟环境安装

```python
pip install django-cors-headers
```

配置setting.py

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', #加这一句
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

settings.py 添加

```python
CORS_ORIGIN_ALLOW_ALL = True
```

### 4、额外说明

① 导入mysql

```python
import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'WeiboAnalysisSystem',
        'USER': 'root',
        'PASSWORD': 'Aa123hsp.',
        'HOST': '139.199.4.56'
    }
}
```

② django和数据库打交道

> migrate负责应用和取消应用迁移。

> makemigrations负责根据您对模型所做的更改创建新的迁移。

> sqlmigrate显示迁移的SQL语句。

> showmigrations列出项目的迁移及其状态。

至此，开发环境就搭建完成了。

### 5、系统介绍（2019.5.4毕设已完成，就不罗嗦其他了，直接介绍系统以及系统启动）：

待完善

###6、系统启动注意事项
1、获取Cookie方式，自行登录微博m站获取Cookie，实在不清楚，可以参考这里 https://blog.csdn.net/A_xiao_mili/article/details/77947802

2、启动前进入xadmin后台账号是`hsp` 密码是`admin123`设置爬虫API的爬虫设置的Cookie,即可

3、如需启动Scrapyd爬虫, 进入weibo-analysis-system\scrapydserver\bot\settings.py文件，找到Cookie,设置Cookie，保存。

然后执行scrapyd-deploy sina -p bot重新部署上去就好了（前提是启动了Scrpayd，不然部署失败）

（启动方式参考技术文档）







