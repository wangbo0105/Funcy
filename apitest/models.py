from django.db import models

from product.models import Product


# Create your models here.

class ApiTest(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=False)
    apitest_name = models.CharField('流程接口名称', max_length=64)
    apitest_desc = models.CharField('描述', max_length=64, null=True)
    apitest_owner = models.CharField('测试负责人', max_length=16)
    apitest_result = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '流程场景接口'

    def __str__(self):
        return self.apitest_name


class ApiStep(models.Model):
    ApiTest = models.ForeignKey('ApiTest', on_delete=models.CASCADE)
    api_name = models.CharField('接口名称', max_length=100)
    api_url = models.CharField('url地址', max_length=200)
    api_step = models.CharField('测试步骤', max_length=100, null=True)
    api_param = models.CharField('参数和值', max_length=800)
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'))
    api_method = models.CharField('请求方法', choices=REQUEST_METHOD, default='get', max_length=200, null=True)
    api_result = models.BooleanField('预期结果', max_length=200)
    api_response = models.CharField('响应数据', max_length=5000, null=True)
    api_status = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.api_name
