"""weibosystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from SpiderAPI.views import SpiderWeibo
from ScrapydAPI.views import ScrapydWeibo
from SnowNLPAPI.views import SnowNLPWeibo

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('spiderapi/', SpiderWeibo.SpiderAPI, name="spiderapi"),
    path('scrapydapi/', ScrapydWeibo.ScrapydAPI, name="scrapydapi"),
    path('snownlpapi/', SnowNLPWeibo.SnowNLPAPI, name="snownlpapi"),
    path('', TemplateView.as_view(template_name="index.html")),
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')),
]
