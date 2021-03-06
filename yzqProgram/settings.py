# -*- coding: utf-8 -*-

"""
Django settings for yzqProgram project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, base64, socket

ADMIN_SITE_HEADER = "TestAuto"  # 站点头部
ADMIN_SITE_TITLE = "TestAuto"  # 站点标题

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jq!8zvuxk2e*xs-^m*%txw**sj8abk-o0)n%33_ow0wy5$3fn6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # nginx 、Apache 处理静态网页
# DEBUG = True  # django 自己处理静态网页

IP_LOCAL = ["192.168.66.55", "10.0.0.20", "169.254.111.198", ]  # 字母要大写才能被 django.conf 载入
if socket.gethostbyname(socket.gethostname()) in IP_LOCAL:
    ALLOWED_HOSTS = [
        "0.0.0.0", "localhost", "127.0.0.1", "testauto.iask.in"] + IP_LOCAL
else:
    ALLOWED_HOSTS = ['python3.cc', 'testauto.site']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',  # appname
    'xuegod',
    'testfly',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'yzqProgram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/')  # 设置模版路径
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yzqProgram.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

import json


def json_load():
    # pw_name = "alimysqlpw"
    # print(os.getcwd())
    with open(os.path.join(os.getcwd(), "alimysql.pw"), 'r') as f:
        # 如果是 Apache web服务器 需要把 .pw 文件放置在 Apache ServerRoot 指向的目录下
        pw_info = json.load(f)
        return pw_info

        # if pw_name in pw_info.keys():
        #     alimysqlpw = pw_info[pw_name]  # 导出变量值
        #     return alimysqlpw
        # else:
        #     # print("%s don't exists" % pw_info)
        #     return None


# from txt get password
all_pw = json_load()
if all_pw:
    if "alimysqlpw" in all_pw.keys():
        alimysqlpw = all_pw["alimysqlpw"]
    else:
        alimysqlpw = None
    if "qqemailpw" in all_pw.keys():
        qqemailpw = all_pw["qqemailpw"]
    else:
        qqemailpw = None

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'yzqdb',  # 库名
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'HOST': '192.168.235.145',
    #     # 'CHARSET':'utf-8',
    #
    # },

    "alimysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bdm232505473_db",
        "USER": "bdm232505473",
        "PASSWORD": base64.b64decode(alimysqlpw).decode(),
        "HOST": 'bdm232505473.my3w.com',
    },

}

DATABASES_ROUTERS = ['yzqProgram.database_router.DatabaseAppRouter']
DATABASES_APPS_MAPPPING = {

    'polls': 'default',
    'xuegod': 'alimysql',
    # 'xuegod': 'default',
    # 'django.contrib.admin':'alimysql',

}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# UTC 世界统一时间
# TIME_ZONE = 'UTC'

# 东八区的中国，西减东加
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


# 因为在运行 python manage.py collectstatic 的时候，
# STATICFILES_DIRS 中的文件夹中的静态文件会被复制到 STATIC_ROOT 中
# 把这些文件放到一起是为了用 nginx、apache 等部署的时候更方便
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_all')


# 静态文件的优先级是默认先找共用的，再找app下的
# 给静态文件变量赋值，告诉Django，静态文件在哪里
# STATIC_URL：设置的static file的起始url，这个只可以在template里面引用到。如果不喜欢static可以更改。
STATIC_URL = '/static/'

# STATICFILES_DIRS 除了各个app的static目录以外还需要管理的静态文件位置
# 其它存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
    os.path.join(BASE_DIR, 'testfly/static').replace('\\', '/'),

]

# upload folder
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# 样式？
# TINYMCE_DEFAULT_CONFIG = {
# 'theme': "advanced", # default value
# 'relative_urls': False, # default value
# 'plugins': 'table,spellchecker,paste,searchreplace',
# 'theme_advanced_buttons1': 'bold,italic,underline,bullist,numlist,link,unlink,styleselect,fontselect,fontsizeselect',
# 'width': '100%',
# 'height': 300,
# 'paste_text_sticky': True,
# 'paste_text_sticky_default': True,
# 'valid_styles': 'font-weight,font-style,text-decoration',
# 'fontsize_formats': "8pt 10pt 11pt 12pt 13pt 14pt 16pt 18pt 20pt 24pt 36pt",
# 'font_formats': "Andale Mono=andale mono,times;" +
#     "Arial=arial,helvetica,sans-serif;" +
#     "Arial Black=arial black,avant garde;" +
#     "Book Antiqua=book antiqua,palatino;" +
#     "Comic Sans MS=comic sans ms,sans-serif;" +
#     "Courier New=courier new,courier;" +
#     "Georgia=georgia,palatino;" +
#     "Helvetica=helvetica;" +
#     "Impact=impact,chicago;" +
#     "Symbol=symbol;" +
#     "Tahoma=tahoma,arial,helvetica,sans-serif;" +
#     "Terminal=terminal,monaco;" +
#     "Times New Roman=times new roman,times;" +
#     "Trebuchet MS=trebuchet ms,geneva;" +
#     "Verdana=verdana,geneva;" +
#     "Webdings=webdings;" +
#     "Wingdings=wingdings,zapf dingbats",}
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True



# 邮件配置
EMAIL_HOST = 'smtp.qq.com'  # SMTP地址
# qq 普通邮箱发送邮件服务器：smtp.qq.com，使用SSL，端口号587
# qq 企业邮箱 端口号25，SMTP协议默认端口是25
EMAIL_PORT = 587  # SMTP端口
EMAIL_HOST_USER = 'testauto@qq.com'  # 自己的邮箱
EMAIL_HOST_PASSWORD = qqemailpw  # 我的邮箱密码
EMAIL_SUBJECT_PREFIX = 'TestData'  # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false。与SSL是互相排斥的。
# EMAIL_USE_SSL = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false

# 管理员站点
# https://docs.djangoproject.com/en/1.11/ref/settings/
# 电子邮件的“From：”标头将是SERVER_EMAIL设置的值。
SERVER_EMAIL = 'testauto@qq.com'  # The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
