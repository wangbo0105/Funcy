#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/8/11 4:34 下午
# @Author   : wangbo

from django.urls import path
from .views import product_manage

urlpatterns = [
    path('', product_manage)
]
