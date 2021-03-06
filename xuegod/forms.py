#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from django import forms
import re
from xuegod.models import *
from testfly.models import TestDevice


class Login(forms.Form):
    user_name = forms.CharField(max_length=32, label="您的名称")
    user_password = forms.CharField(max_length=32, label="您的密码")
    user_email = forms.EmailField(max_length=32, label="您的邮箱")

    def clean_user_name(self):
        # print( self.cleaned_data)
        # print(type(self.cleaned_data))
        user_name = self.cleaned_data["user_name"]
        if len(user_name) < 6:
            raise forms.ValidationError("您的名称长度不够 6 位")
        return user_name

    def clean_user_password(self):
        user_password = self.cleaned_data["user_password"]

        reg_s = re.compile(r'(?=.*?[a-zA-Z])(?=.*?[0-9])[a-zA-Z0-9~!@#$%&*_+-]{6,16}$')
        user_password_re = re.findall(reg_s, user_password)
        if len(user_password_re) == 0:
            raise forms.ValidationError("密码首位必须为字母，至少字母和数字组合，6-16个字符")

        # if len(user_password ) < 6:
        #     raise forms.ValidationError("您的密码长度不够 6 位")

        return user_password

        # def clean_user_email(self):
        #     user_email = self.cleaned_data["user_email"]
        #     if len(user_email) < 6:
        #         raise forms.ValidationError("您的邮箱长度不够 6 位")
        #     return user_email


class Ticket(forms.Form):
    ticket_type = (
        ('in', '内网'),
        ("out", "外网"),
    )
    # initial 是 Select 的默认值，即 Radio 的 checked，写 choice 的 value 值
    ticket_style = forms.CharField(max_length=32, label='获取模式', initial="in",
                                   widget=forms.RadioSelect(choices=ticket_type, attrs={'class': 'form-control'}))

    user_name = forms.CharField(max_length=32, label='用户账号',
                                widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="龙号")
    user_password = forms.CharField(max_length=32, label='登陆密码',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))


class DeviceId(forms.Form):
    api_type = (
        ("out", "外网"),
        ('in', '内网'),
    )
    api_model = forms.CharField(max_length=128, label='获取模式',
                                widget=forms.Select(choices=api_type, attrs={'class': 'form-control'}))
    device_id = forms.CharField(max_length=128, label='设 备 ID ',
                                widget=forms.Select(attrs={'class': 'form-control'}),  # 'size': '35'
                                help_text='<br>Android：📞*#06# 第一行的那一串数字<br>iOS:第三方登录后台可拿到机器码<br>'
                                          '如无机器名称，请到后台添加机器码')

    def __init__(self, *args, **kwargs):
        super(DeviceId, self).__init__(*args, **kwargs)
        # print(TestDevice.objects.filter(pk=30).values_list('device_machine_code', 'device_name'))
        self.fields['device_id'].widget.choices = TestDevice.objects.exclude(device_machine_code="").values_list('device_machine_code',
                                                                                               'device_name')


class RegisterCode(forms.Form):
    phone = forms.CharField(max_length=32, label='手机号码 ',
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            help_text='只支持手机注册')


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
