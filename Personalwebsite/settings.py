from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-tclrz8rvtqu%!%*evvs-)@-#0h1g#tm5i6__g78@z&o7^nl*#w'
DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App_Blog.apps.AppBlogConfig',
    'App_Users.apps.AppUsersConfig',
    'APP_Comment.apps.AppCommentConfig',
    'App_Essay.apps.AppEssayConfig',
    'App_Manage.apps.AppManageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'App_Manage.middware.permission.Middleware'
]

ROOT_URLCONF = 'Personalwebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR / 'templates'))]
        ,
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

WSGI_APPLICATION = 'Personalwebsite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 3306,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 两个方案，目前本方案在部署之后能运行，能收集静态文件，但是有博主换成了方式二的部署
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static/'),
]
# 方式二
# STATIC_URL = '/static/'
# STATIC_ROOT = [
#     os.path.join(BASE_DIR, 'static'),
# ]


# 修改系统对于未登录的验证跳转地址
LOGIN_URL = '/users/login/'

# session相关的全局设置

SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）

SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）

SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）

SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）

SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）

SESSION_COOKIE_AGE = 14 * 24 * 3600  # Session的cookie失效日期（2周）（默认）

SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）

SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存（默认）

# 日志
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 不禁用已经存在的log实例，确定日志输出到文件或者终端
    # 定义一些日志的处理方式
    'handlers': {
        'console': {
            'level': "DEBUG",  # handler的日志级别
            'class': "logging.StreamHandler",
        },
    },

    'loggers': {  # 具体的与日志有关的信息
        'django.db.backends': {
            'handlers': ["console"],
            'propagate': True,  # 向上传导
            'level': "DEBUG",  # logger实例的日志级别
        },
    }
}
"""

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 发送邮件配置项
EMAIL_HOST = 'smtp.qq.com'  # 发送邮件的邮箱 的 SMTP服务器
EMAIL_PORT = 465  # smtp port
EMAIL_HOST_USER = ''  # email address
EMAIL_SELF_ATTR = ''
EMAIL_HOST_PASSWORD = ''  # pwd
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # default send email user
EMAIL_USE_SSL = True  # 是否使用SSL加密

# 同桌的你
ETERNAL_KEY = 'tenyuxue'

# 备案号
ICP_CODE = '鄂ICP备2021021476号-1'

# QQ登陆配置项
QQ_APP_ID = ''  # app_id
QQ_APP_KEY = ''  # APP_KEY - 应该写入到环境变量中
# QQ_APP_KEY = os.environ['QQ_APP_KEY']  # 环境变量读取方法
QQ_REDIRECT_URL = ''  # (本站)回调域
QQ_STATE = ''  # 自定义字符串原样带回

# 首页置顶文章ID配置
EXCLUDE_ARTICLE_ID_LIST = [5, 6]
