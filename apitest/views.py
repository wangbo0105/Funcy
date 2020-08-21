from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ApiTest, ApiStep


# Create your views here.
@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()
    username = request.session.get('user', '')
    return render(request, "apitest_manage.html", {"user": username, "apitests": apitest_list})


@login_required
def apistep_manage(request):
    apistep_list = ApiStep.objects.all()
    username = request.session.get('user', '')
    return render(request, "apistep_manage.html", {"user": username, "apisteps": apistep_list})
