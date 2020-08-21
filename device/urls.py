#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/8/12 11:18 上午
# @Author   : wangbo
from django.urls import path
from device import views

urlpatterns = [
    path('', views.device)
]
