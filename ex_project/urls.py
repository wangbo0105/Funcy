#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/9/8 5:11 下午
# @Author   : wangbo
from django.urls import path
from ex_project import views

urlpatterns = [
    path('', views.get_jenkins_job),
]
