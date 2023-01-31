from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^add_product$', views.add_product),  # 添加产品
]
