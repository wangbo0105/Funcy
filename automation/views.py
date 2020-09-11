import os

from django.http import FileResponse, HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Funcy.settings import MEDIA_ROOT
from common import local_jenkins

# Create your views here.

from .models import UIAutomation, MiniAutomationResult

JENKINS_TOKEN = '112923e266381d424079937e8908294227'


@login_required()
def ui_automation_list(request):
    uia_list = UIAutomation.objects.all()
    username = request.session.get('user', '')
    return render(request, "automation/ui_automation.html", {"user": username, "uia_list": uia_list})


@login_required()
def ui_automation_detail(request, ui_id):
    uia_item = UIAutomation.objects.get(pk=ui_id)
    history_item = MiniAutomationResult.objects.all()
    username = request.session.get('user', '')
    build_item = local_jenkins.get_build_para(uia_item.job_name)
    return render(request, "automation/ui_automation_detail.html",
                  {"user": username, "uia_item": uia_item, "history_item": history_item, "build_item": build_item})


@login_required()
def build(request, ui_id):
    if request.POST:
        uia_item = UIAutomation.objects.get(pk=ui_id)
        build_item = local_jenkins.get_build_para(uia_item.job_name)
        build_args = {}
        for item in build_item:
            build_args[item] = request.POST.get(item)
        local_jenkins.start_build(uia_item.job_name, build_args)
        print(local_jenkins.get_last_build_number(uia_item.job_name))
        return redirect("/automation/ui/" + str(ui_id))


@login_required()
def report_down(request, ui_id, report_id):
    """
    下载压缩文件
    :param ui_id:
    :param report_id:
    :param request:
    :return:
    """
    file_name = str(MiniAutomationResult.objects.get(pk=report_id).report_file)

    file_path = os.path.join(MEDIA_ROOT, file_name)  # 下载文件的绝对路径

    if not os.path.isfile(file_path):  # 判断下载文件是否存在
        return HttpResponse("Sorry but Not Found the File")

    def file_iterator(file_path, chunk_size=512):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    try:
        # 设置响应头
        # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法
        response = StreamingHttpResponse(file_iterator(file_path))
        # 以流的形式下载文件,这样可以实现任意格式的文件下载
        response['Content-Type'] = 'application/octet-stream'
        # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
    except:
        return HttpResponse("Sorry but Not Found the File")

    return response
