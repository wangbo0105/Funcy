#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/9/8 10:54 上午
# @Author   : wangbo
import jenkins

JENKINS_TOKEN = '112923e266381d424079937e8908294227'
jenkins_server_url = 'http://jenkins.mfwdev.com/'
user_id = 'wangbo4'
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=JENKINS_TOKEN)


def get_build_para(job_name):
    job_para = server.get_job_info(job_name)['actions'][0]['parameterDefinitions']
    para = {}
    for i in job_para:
        if 'choices' in i:
            para[i['name']] = i['choices']
        else:
            para[i['name']] = None
    return para


def get_build_url(job_name):
    return jenkins_server_url + 'job/' + job_name + '/' + get_last_build_number(job_name)


def start_build(job_name, parameters):
    build_obj = server.build_job(job_name, parameters=parameters)
    return build_obj


def is_job_exits(job_name):
    jobs = server.get_all_jobs()
    job_list = []
    for j in jobs:
        name = j['name']
        job_list.append(name)
    if job_name in job_list:
        return True
    else:
        return False


def get_last_build_number(job_name):
    if is_job_exits(job_name):
        return server.get_job_info(job_name)['lastBuild']['number']
    else:
        return None


# s = start_build('mini_automation', {"env": "online", "device": "MI9", "suite": "TC_*", "retry": 3})
# print(s)
#
# s1 = server.get_job_info('mini_automation')
# print(s1)
