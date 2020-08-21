#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/8/11 4:50 下午
# @Author   : wangbo
from django.urls import path
from .views import apistep_manage, apitest_manage

urlpatterns = [
    path('test/', apitest_manage),
    path('step/', apistep_manage)
]
