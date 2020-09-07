from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import UIAutomation, MiniAutomationResult


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
    return render(request, "automation/ui_automation_detail.html",
                  {"user": username, "uia_item": uia_item, "history_item": history_item})


@login_required()
def mini_ui_automation_result(request, ui_id, report_id):
    result_item = MiniAutomationResult.objects.get(report_file=report_id)
    username = request.session.get('user', '')
    return render(request, result_item.report_file.url, {"user": username, "result_item": result_item})
