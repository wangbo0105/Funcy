# 测开平台

## settings配置

```pythonregexp

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '$name',
        'USER': '$user',
        'PASSWORD': '$pwd',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

# Internationalization
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

## 部署流程

- 安装nginx

`
yum install nginx
`
- 安装uwsgi

`
pip3 install uwsgi
`
