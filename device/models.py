from django.db import models


# Create your models here.

class Device(models.Model):
    device_name = models.CharField('设备名称', max_length=100)
    DEVICE_SYS = (('Android', 'Android'), ('IOS', 'IOS'))
    device_sys = models.CharField('设备系统', choices=DEVICE_SYS, max_length=100)
    device_version = models.CharField('系统版本', max_length=100)
    device_brand = models.CharField('设备品牌', max_length=200)
    device_owner = models.CharField('设备归属人', max_length=200)
    create_time = models.DateTimeField('添加时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = '设备'

    def __str__(self):
        return self.device_name
