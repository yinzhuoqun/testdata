# -*- coding: utf-8 -*-
# Create your views here.


from django.shortcuts import render
from django.shortcuts import render_to_response

from xuegod.models import *
from xuegod.forms import *

from django.db import connection
from django.template import RequestContext  # csrf
from django.http import StreamingHttpResponse

from django import forms

import os, time
import collections  # 有序字典
import faker


# import random


def create(request):
    data = ""  # 前端表单传来的数据
    u = User(name=data, age=data, password=data)
    # u.save(using='mysql')
    u.save(using='alimysql')


def index(request):
    # 插入数据
    u = User(name="你们太牛了！", age="25", password="老子不跟你们玩了。。。")
    # u.save(using='mysql')  # using='mysql'settings database alias (name)
    # u.save(using='alimysql')  # using='mysql'settings database alias (name)
    print(locals())
    return render_to_response("index.html", locals())


def new_page(request, page):
    # u = User(name="if",age="21",password="range")
    # u.save()

    num = int(page)  # 1 2
    startnum = num - 1  # 0 1
    endnum = num  # 1 2
    if int(page) > 0:
        # data = User.objects.filter(id = 0) # 列表
        # data = User.objects.get(id=1) # 单个
        # data = User.objects.using('mysql').all()[startnum * 3:endnum * 3]  # 0:3 3:6
        # print( User.objects.using('alimysql'))
        data = User.objects.using('alimysql')[startnum * 3:endnum * 3]  # 0:3 3:6
        # data = User.objects.using('alimysql').all()[startnum * 3:endnum * 3]  # 0:3 3:6


    else:
        # data = User.objects.using('mysql')
        data = User.objects.using('alimysql')
        # data = User.objects.using('alimysql').all()
    # locals()返回一个包含当前作用域里面的所有变量和它们的值的字典
    return render_to_response("page.html", locals())


def login(request):
    if request.method == "POST" and request.POST:
        login_form = Login(request.POST)
        valid = login_form.is_valid()  # valid 判断是否有效
        if valid:
            show_data = login_form.cleaned_data
            print(type(show_data))
    else:
        login_form = Login()

    # return render_to_response("login.html",locals()) # no csrf
    return render(request, "login.html", locals())  # render,use csrf


def testid(request):
    return render(request, "test_id.html")


def show_testid(request):
    data = TestId.objects.using('alimysql').filter(user_flag=0)  # filter 列表 0是内网 1是外网
    data1 = TestId.objects.using('alimysql').filter(user_flag=1)
    # data = TestId.objects.all()
    return render(request, "test_id_new.html", locals())


def get_id():
    # filepath = r"I:\yzq\MyPythonTest\yzqProgram\static\app\idi.txt"
    filepath = r"I:\yzq\MyPythonTest\yzqProgram\static\app\ido.txt"
    with open(filepath, "r") as f:
        # content = f.read()
        # logging.info(content)
        id_list = []
        for info in f.readlines():
            info_list = info.replace('\n', '').split("|")
            id_list.append(info_list)
            # print(id_list)
    return id_list


# 修改数据库数据
def alter_testid(request):
    # users_info = get_id()
    # users_info = [['138695031','q1234567','14533331102','1']]  # filter 列表 0是内网 1是外网
    # users_info = [['137349241','q1234567','','0']]  # filter 列表 0是内网 1是外网
    # users_info = [['137349246','q1234567','13725548739','0']]  # filter 列表 0是内网 1是外网
    users_info = [['137349108', 'q1234567', '18676715509', '0']]  # filter 列表 0是内网 1是外网

    users_alter_info = []
    for user_info in users_info:
        if len(user_info) == 4:
            # user_id = user_info[0]
            # user_password = user_info[1]
            # user_note = user_info[2]
            # user_flag = user_info[3]
            user_alter_info = TestId(user_id=user_info[0],
                                     user_password=user_info[1],
                                     user_note=user_info[2],
                                     user_flag=user_info[3]
                                     )
        elif len(user_info) == 2:
            user_alter_info = TestId(user_id=user_info[0],
                                     user_password=user_info[1],
                                     user_flag="1"
                                     )

        elif len(user_info) == 3:
            user_alter_info = TestId(user_id=user_info[0],
                                     user_password=user_info[1],
                                     user_note=user_info[2],
                                     user_flag="1"
                                     )

        users_alter_info.append(user_alter_info)

        user_alter_info.save(using='alimysql')  # 保存到指定数据库

    # print(len(users_alter_info),users_alter_info)
    # 增加数据
    # user_alter_info = TestId(user_id="150132", user_password="111111")
    # user_alter_info = TestId(user_id="150131", user_password="111111", user_note="",user_flag="i")
    # user_alter_info.save(using='alimysql')
    # user_alter_info.save()

    # 删除数据
    # user_alter_info = TestId.objects.using("alimysql").get(id=4).delete()

    # print(locals())
    # return render_to_response("altertestid.html", locals())
    return render(request, "altertestid.html", locals())


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


def app_list(request):
    # app_path = os.path.join(os.path.abspath("static"), 'app') # 只能 django-debug 用
    # app_path = 'static/app' # 只能 django-debug 用
    app_path = r"I:/yzq/MyPythonTest/yzqProgram/static/app"  # django-debug 和 Apache-django 用
    img_save_path = r"I:/91UserData/ScreenCapture"
    app_save_path = app_path
    app_list = os.listdir(app_path)
    # print(app_list)
    app_dict = {}

    for app in app_list:
        # app_info_dict = {} # 无序字典
        app_info_dict = collections.OrderedDict()  # 有序字典

        app_unix_time = os.stat(os.path.join(app_path, app)).st_ctime
        app_create_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(app_unix_time))

        app_size = os.stat(os.path.join(app_path, app)).st_size
        if app_size > 1024 * 1024:
            app_info_dict["app_size"] = "%.2fMB" % (app_size / 1024 / 1024)
        else:
            app_info_dict["app_size"] = "%.2fKB" % (app_size / 1024)

        app_info_dict["app_create_time"] = app_create_time
        app_dict[app] = app_info_dict

    # print(app_list)
    # print(app_dict)
    # print(sorted(app_dict.items(), key=lambda item: item[1]["app_create_time"], reverse=True))
    app_dict = sorted(app_dict.items(), key=lambda item: item[1]["app_create_time"], reverse=True)  # 按时间倒序排列
    # print(app_dict)
    # for app in app_list:
    #     app_size = os.path.getsize(os.path.join(app_path, app))
    #     if app_size > 1024*1024:
    #         app_dict[app] = "%.2f MB"%(app_size / 1024 / 1024)
    #     else:
    #         app_dict[app] = "%.2f KB"%(app_size / 1024)
    # print(app_dict)

    # sorted

    if request.method == "POST":
        file = request.FILES.get("file", None)
        if not file:
            uploadfile_mes = "请选择文件"
        else:
            if file.name.endswith('.apk'):
                destination = open(os.path.join(app_save_path, file.name), 'wb+')
            else:
                destination = open(os.path.join(img_save_path, file.name), 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            uploadfile_mes = "上传成功"

    return render(request, "app.html", locals())


def test_report_platform_version(request, platform, version):
    title = "%s %s | TestReport" % (platform, version)

    # # print(test_report_info.project_name)
    # project_name = "X 项目"
    # test_version = "5.3.0"
    # test_platform = "iOS"
    # test_report_create_time = "2017/1/11"
    # test_way = "黑盒测试"
    # test_start_time = "2017/1/11"
    # test_end_time = "2017/1/11"
    #
    # bug_block = 12
    # bug_major = 1
    # bug_normal = 2
    # bug_trivial = 1
    # bug_total = bug_block + bug_major + bug_normal + bug_trivial
    #
    # bug_surplus_block = 12
    # bug_surplus_major = 1
    # bug_surplus_normal = 2
    # bug_surplus_trivial = 1
    # bug_surplus_total = bug_surplus_block + bug_surplus_major + bug_surplus_normal + bug_surplus_trivial
    #
    # fkr = faker.Faker()
    # # fkr.first_name()
    # # 返回一个随机假冒的firstname
    # # fkr.last_name()
    # # 返回一个随机假冒的lastname
    # # fkr.company()
    # # 返回一个随机假冒的company名称
    # # fkr.paragraphs()
    # # 返回一个随机生成的段落列表
    #
    # # 测试要点
    # test_points = fkr.paragraphs()
    # # 参与者
    # test_participants = [fkr.first_name() + "·" + fkr.last_name(), fkr.first_name() + "·" + fkr.last_name()]
    # # 测试风险
    # test_risks = [fkr.company(), fkr.company(), fkr.company()]
    # # 测试参考文档
    # test_docs = [fkr.company(), fkr.company(), fkr.company()]
    # test_cases = "/index"
    # test_conclusion = "正常发布上线"


    test_report_info = TestReport.objects.get(test_platform=platform, test_version=version)
    project_name = test_report_info.project_name
    # test_version = test_report_info.test_version
    test_version = version
    test_platform = platform
    # test_platform = test_report_info.test_platform
    test_cases = test_report_info.test_cases
    test_report_create_time = test_report_info.test_report_create_time
    test_way = test_report_info.test_way
    test_start_time = test_report_info.test_start_time
    test_end_time = test_report_info.test_end_time

    str_splist ="\n"
    test_docs = test_report_info.test_docs.split(str_splist)
    test_points = test_report_info.test_points.split(str_splist)
    test_risks = test_report_info.test_risks.split(str_splist)

    test_conclusion = test_report_info.test_conclusion

    bug_info = BugInfo.objects.get(test_platform=platform, test_version=version)
    bug_block = bug_info.bug_block
    bug_major = bug_info.bug_major
    bug_normal = bug_info.bug_normal
    bug_trivial = bug_info.bug_trivial
    bug_total = bug_block + bug_major + bug_normal + bug_trivial

    bug_surplus_info = BugSurplusInfo.objects.get(test_platform=platform, test_version=version)
    bug_surplus_block = bug_surplus_info.bug_surplus_block
    bug_surplus_major = bug_surplus_info.bug_surplus_major
    bug_surplus_normal = bug_surplus_info.bug_surplus_normal
    bug_surplus_trivial = bug_surplus_info.bug_surplus_trivial
    bug_surplus_total = bug_surplus_block + bug_surplus_major + bug_surplus_normal + bug_surplus_trivial

    test_participants_info = TestParticipants.objects.get(test_platform=platform, test_version=version)
    # for x in test_participants_info:
    #     print(x)
    # print(test_participants_info.test_participant1)

    test_participants = [test_participants_info.test_participant1,
                         ]
    if test_participants_info.test_participant2 != "":
        test_participants.append(test_participants_info.test_participant2)
    if test_participants_info.test_participant3 != "":
        test_participants.append(test_participants_info.test_participant3)
    if test_participants_info.test_participant4 != "":
        test_participants.append(test_participants_info.test_participant4)
    if test_participants_info.test_participant5 != "":
        test_participants.append(test_participants_info.test_participant5)
    if test_participants_info.test_participant6 != "":
        test_participants.append(test_participants_info.test_participant6)

    return render(request, 'test_report_platform_version.html', locals())


def test_report_platform(request, platform):
    test_platform = platform
    test_report_info = TestReport.objects.filter(test_platform=platform)
    # bug_info = BugInfo.objects.get(test_platform=platform, test_version=version)
    # bug_surplus_info = BugSurplusInfo.objects.get(test_platform=platform, test_version=version)
    # test_participants_info = TestParticipants.objects.get(test_platform=platform, test_version=version)
    # test_participants = [test_participants_info.test_participant1,
    #                      ]
    # if test_participants_info.test_participant2 != "":
    #     test_participants.append(test_participants_info.test_participant2)
    # if test_participants_info.test_participant3 != "":
    #     test_participants.append(test_participants_info.test_participant3)
    # if test_participants_info.test_participant4 != "":
    #     test_participants.append(test_participants_info.test_participant4)
    # if test_participants_info.test_participant5 != "":
    #     test_participants.append(test_participants_info.test_participant5)
    # if test_participants_info.test_participant6 != "":
    #     test_participants.append(test_participants_info.test_participant6)

    return render(request, 'test_report_platform.html', locals())


def test_report(request):
    title = "TestReport | TestData"
    test_report_info_android = TestReport.objects.filter(test_platform="Android")
    test_report_info_ios = TestReport.objects.filter(test_platform="iOS")

    return render(request, 'test_report.html', locals())
