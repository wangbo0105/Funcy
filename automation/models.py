from django.db import models


# Create your models here.


class UIAutomation(models.Model):
    uia_name = models.CharField('项目名称', max_length=100)
    uia_desc = models.CharField('项目描述', max_length=200)
    git_name = models.CharField('git项目名称', max_length=100)
    git_url = models.CharField('git项目url', max_length=200, null=True)
    git_repo = models.CharField('git项目地址', max_length=200)
    uia_owner = models.CharField('项目负责人', max_length=20)
    create_time = models.DateTimeField('添加时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = 'UI自动化'

    def __str__(self):
        return self.uia_name


class MiniAutomationResult(models.Model):
    mini_pro = models.ForeignKey('UIAutomation', on_delete=models.CASCADE)
    build_version = models.CharField('构建版本', max_length=100)
    build_time = models.DateTimeField('构建时间')
    case_num = models.IntegerField('用例数量')
    fail_num = models.IntegerField('失败用例数量')
    RESULT_CHOICES = (
        ('1', '通过'),
        ('2', '失败'),
    )
    build_result = models.CharField(max_length=1, choices=RESULT_CHOICES)
    report_file = models.FileField(upload_to='report/mini/ui/')
    create_time = models.DateTimeField('添加时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '小程序UI自动化'
        ordering = ['-id']

    def __str__(self):
        return self.build_result
