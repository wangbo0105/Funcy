from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth


# Create your views here.

def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/')
            return response
        else:
            return render(request, 'autotest/login.html', {'error_msg': 'username or password error!'})
    return render(request, 'autotest/login.html')


def index(request):
    username = request.session.get('user')
    # 未登录用户跳转登录页
    if username is None:
        return render(request, 'autotest/login.html')
    else:
        return render(request, "autotest/index.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
