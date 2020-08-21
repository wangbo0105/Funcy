from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Device


# Create your views here.
@login_required()
def device(request):
    device_list = Device.objects.all()
    username = request.session.get('user', '')
    return render(request, "device.html", {"user": username, "device_list": device_list})
