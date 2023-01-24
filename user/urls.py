from django.urls import re_path as url
from django.contrib import admin
from . import views
from django.urls import path,include


admin.site.site_title = '管理后台'
admin.site.site_header = '后台管理'

urlpatterns = [
    # url(r'^Register$', views.Register),  # 注册
    # url(r'^login$', views.login),  # 登陆
    path('register/',views.Register),

]
