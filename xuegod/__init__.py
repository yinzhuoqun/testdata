from django.apps import AppConfig
import os

# 从Django1.7以后不再使用app_label，修改app相关需要使用AppConfig

verbose_app_name = u"测试账号管理"
default_app_config = 'xuegod.XuegodConfig'

def get_current_app_name(_file):
    return os.path.split((os.path.dirname(_file)))[-1]

class XuegodConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = verbose_app_name