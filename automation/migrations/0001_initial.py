# Generated by Django 3.1 on 2020-09-08 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UIAutomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uia_name', models.CharField(max_length=100, verbose_name='项目名称')),
                ('uia_desc', models.CharField(max_length=200, verbose_name='项目描述')),
                ('git_name', models.CharField(max_length=100, verbose_name='git项目名称')),
                ('git_url', models.CharField(max_length=200, verbose_name='git项目url')),
                ('git_repo', models.CharField(max_length=200, verbose_name='git项目地址')),
                ('job_name', models.CharField(max_length=200, verbose_name='job项目名称')),
                ('job_url', models.CharField(max_length=200, verbose_name='job项目地址')),
                ('uia_owner', models.CharField(max_length=20, verbose_name='项目负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': 'UI自动化',
                'verbose_name_plural': 'UI自动化',
            },
        ),
        migrations.CreateModel(
            name='MiniAutomationResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_version', models.CharField(default='', max_length=100, verbose_name='构建版本')),
                ('build_time', models.DateTimeField(auto_now=True, verbose_name='构建时间')),
                ('job_url', models.URLField(verbose_name='Job地址')),
                ('build_result', models.CharField(choices=[('0', '构建中'), ('1', '成功'), ('2', '失败')], max_length=1)),
                ('report_file', models.FileField(null=True, upload_to='report/mini/ui/')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='添加时间')),
                ('mini_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation.uiautomation')),
            ],
            options={
                'verbose_name': '小程序UI自动化',
                'verbose_name_plural': '小程序UI自动化',
                'ordering': ['-id'],
            },
        ),
    ]
