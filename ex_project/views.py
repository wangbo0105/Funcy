from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from common import local_jenkins


@csrf_exempt
def get_jenkins_job(request):
    job_name = request.GET.get('job_name')
    print(job_name)
    dic = {}
    num = local_jenkins.get_last_build_number(job_name)
    if request.method == 'GET':
        dic['number'] = num
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
