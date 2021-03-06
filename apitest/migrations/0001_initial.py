# Generated by Django 3.1 on 2020-08-11 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apitest_name', models.CharField(max_length=64, verbose_name='流程接口名称')),
                ('apitest_desc', models.CharField(max_length=64, null=True, verbose_name='描述')),
                ('apitest_owner', models.CharField(max_length=16, verbose_name='测试负责人')),
                ('apitest_result', models.BooleanField(verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': '流程场景接口',
                'verbose_name_plural': '流程场景接口',
            },
        ),
        migrations.CreateModel(
            name='ApiStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100, verbose_name='接口名称')),
                ('api_url', models.CharField(max_length=200, verbose_name='url地址')),
                ('api_step', models.CharField(max_length=100, null=True, verbose_name='测试步骤')),
                ('apitest_param', models.CharField(max_length=800, verbose_name='参数和值')),
                ('api_method', models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete')], default='get', max_length=200, null=True, verbose_name='请求方法')),
                ('api_result', models.BooleanField(max_length=200, verbose_name='预期结果')),
                ('api_response', models.CharField(max_length=5000, null=True, verbose_name='相应数据')),
                ('api_status', models.BooleanField(verbose_name='是否通过')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('ApiTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.apitest')),
            ],
        ),
    ]
