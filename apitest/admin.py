from django.contrib import admin
from .models import ApiTest, ApiStep


# Register your models here.

class ApiStepAdmin(admin.TabularInline):
    list_display = [
        'api_name', 'api_url', 'api_param', 'api_method', 'api_result', 'api_status', 'create_time'
    ]
    model = ApiStep
    extra = 1


class ApiTestAdmin(admin.ModelAdmin):
    list_display = [
        'apitest_name', 'apitest_owner', 'apitest_result', 'create_time'
    ]
    inlines = [ApiStepAdmin]


admin.site.register(ApiTest, ApiTestAdmin)
