#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/9/7 10:05 上午
# @Author   : wangbo


from django.urls import path, re_path
from automation import views

urlpatterns = [
    path('ui/', views.ui_automation_list, name="list"),
    path('ui/<int:ui_id>/', views.ui_automation_detail, name="detail"),
    path('ui/<int:ui_id>/download/<int:report_id>/', views.report_down, name="download"),
]
