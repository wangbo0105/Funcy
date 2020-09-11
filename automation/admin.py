from django.contrib import admin
from .models import UIAutomation, MiniAutomationResult


# Register your models here.

class UIAutomationAdmin(admin.ModelAdmin):
    list_display = ['uia_name', 'uia_owner', 'create_time']


admin.site.register(UIAutomation, UIAutomationAdmin)


class MiniAutomationResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'mini_pro', 'build_version', 'build_time', 'build_result']


admin.site.register(MiniAutomationResult, MiniAutomationResultAdmin)
