#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/8/10 5:50 下午
# @Author   : wangbo

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.index),
    path('logout/', views.logout),
]
