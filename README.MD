# 测开平台

## bootstrap设置
```npm
npm install bootstrap@4.5.0
npm install jquery@3.5.1
npm install popper.js@1.16.0
```

## settings配置

```python

DEBUG = False
ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '/static/'),
# )
```

## 部署流程
1. 安装 Nginx
```bash
yum install nginx
```
2\. 安装 uwsgi
```bash
pip3 install uwsgi
```
3\. 本地运行django

```bash
python3 manage.py runserver 0.0.0.0:8000 --insecure
```
4\. 服务端部署【暂时】
```bash

sudo fuser -k 8000/tcp

uwsgi -d --ini uwsgi.ini

nginx -s reload
```
