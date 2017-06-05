# -*- coding: utf-8 -*-
# Create your views here.


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from xuegod.models import *
from xuegod.forms import *

from django.db import connection
from django.template import RequestContext  # csrf
from django.http import StreamingHttpResponse

from django import forms

import os, time, socket
import collections  # 有序字典
# import faker
# import uuid
import requests, re


# import random


def create(request):
    data = ""  # 前端表单传来的数据
    u = User(name=data, age=data, password=data)
    # u.save(using='mysql')
    u.save(using='alimysql')


def index(request):
    # 插入数据
    # u = User(name="你们太牛了！", age="25", password="老子不跟你们玩了。。。")
    # u.save(using='mysql')  # using='mysql'settings database alias (name)
    # u.save(using='alimysql')  # using='mysql'settings database alias (name)
    # print(locals())

    urls = HomePage.objects.filter(url_status="1")
    # for info in urls:
    #
    #     print(info)
    #     print(info.url,info.url_name)
    urls_data = urls.filter(url_type="data").order_by('url_order')
    urls_cs = urls.filter(url_type="cs").order_by('url_order')
    urls_cl = urls.filter(url_type="cl").order_by('url_order')
    urls_appinfo = urls.filter(url_type="appinfo").order_by('url_order')
    urls_other = urls.filter(url_type="other").order_by('url_order')

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

        # user_alter_info.save(using='alimysql')  # 保存到指定数据库

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
    # print(os.getcwd())
    show_path = r'media/app'
    # print(os.path.abspath("."))

    # os.getcwd() 拿到的是 Apache 下 http.conf 里的 ServerRoot 路径
    # app_path = os.path.join(os.getcwd(), show_path).replace('\\', '/')
    # app_path = os.path.join(os.path.abspath('.'), show_path).replace('\\', '/')
    app_path = r"I:\yzq\MyPythonTest\yzqProgram\media\app".replace('\\', '/')

    # print(app_path)
    ip_local = ["192.168.66.55", "169.254.111.198"]
    if socket.gethostbyname(socket.gethostname()) not in ip_local:
        show_path = r'media/upload'
        app_path = img_save_path = os.path.join(os.getcwd(), show_path).replace('\\', '/')
        # app_path = img_save_path = os.path.join(os.path.abspath('.'), show_path).replace('\\', '/')
    else:
        img_save_path = r"I:/91UserData/ScreenCapture"  # 192.168.66.55
    app_save_path = app_path
    # print(app_save_path)
    # print(img_save_path)
    app_list = os.listdir(app_path)
    app_dict = {}

    for app in app_list:
        # app_info_dict = {} # 无序字典
        app_info_dict = collections.OrderedDict()  # 有序字典, 需要导入 collections

        app_unix_time = os.stat(os.path.join(app_path, app)).st_ctime
        app_create_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(app_unix_time))

        app_size = os.stat(os.path.join(app_path, app)).st_size
        if app_size > 1024 * 1024:
            app_info_dict["app_size"] = "%.2fMB" % (app_size / 1024 / 1024)
        else:
            app_info_dict["app_size"] = "%.2fKB" % (app_size / 1024)

        app_info_dict["app_create_time"] = app_create_time
        app_dict[app] = app_info_dict

    # 按时间倒序排列
    app_dict = sorted(app_dict.items(), key=lambda item: item[1]["app_create_time"], reverse=True)

    # token = ''
    # postToken = str(uuid.uuid4())
    # if request.method == "GET":
    #     # token = str(uuid.uuid4())  # 采用随机数
    #     token = "allow"
    #     # 在服务端session中添加key认证，避免用户重复提交表单
    #     request.session['postToken'] = token
    #
    #     return render(request, "app.html", locals())

    if request.method == "POST" and request.POST:
        # 检测session中Token值，判断用户提交动作是否合法
        #  RemovedInDjango19Warning: `request.REQUEST` is deprecated, use `request.GET` or `request.POST` instead.
        # token = request.REQUEST.get('postToken', default=None)
        # print('token', token)
        # # 获取用户表单提交的Token值
        # user_token = request.POST['postToken']
        # print('user_token', user_token)

        # if user_token == token:

        file = request.FILES.get("file", None)
        if not file:
            uploadfile_msg = "请选择文件"
            return render(request, "app.html", locals())
        else:
            if file.name.endswith('.apk'):
                destination = open(os.path.join(app_save_path, file.name), 'wb+')
            else:
                destination = open(os.path.join(img_save_path, file.name), 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            uploadfile_msg = "上传成功，即将跳转..."

            # 表单POST提交成功，重置服务端中存在的Token值，避免重复提交
            # token = str(uuid.uuid4())  # 采用随机数
            # 在服务端session中添加key认证，避免用户重复提交表单
            # request.session['postToken'] = "allow"
            # if "postToken" in request.session:  # keyError
            #     del request.session['postToken']
            return render(request, "app_temp.html", locals())
            # return HttpResponseRedirect("/temp")
            # else:
            #     if "postToken" in request.session:  # keyError
            #         del request.session['postToken']
            #     return render(request, "app.html", locals())

    return render(request, "app.html", locals())


def test_change_env(request):
    return render(request, "test_change_env.html", locals())


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

    str_splist = "\n"
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

    return render(request, 'test_report_platform_version.html', locals())


def test_report_platform(request, platform):
    test_platform = platform
    test_report_info = TestReport.objects.filter(test_platform=platform)

    return render(request, 'test_report_platform.html', locals())


def test_report(request):
    title = "TestReport | TestData"
    test_report_info_android = TestReport.objects.filter(test_platform="Android")
    test_report_info_ios = TestReport.objects.filter(test_platform="iOS")

    return render(request, 'test_report.html', locals())


def resume(request):
    info = Resume.objects.filter(name="yinzhuoqun")
    if info:
        phone_mobile = info[0].phone
    else:
        phone_mobile = "18679600250"
    return render(request, 'resume_yzq.html', locals())


# 读取网页
def get_html(url, ref=None):
    import urllib.request, random
    ref = url  # 网页来源
    agent_list = [
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0']
    header = {
        'Referer': '%s' % ref,
        'User-Agent': '%s' % random.choice(agent_list)
    }

    # page = urllib.request.build_opener() # 法 1
    # page.addheaders = [header]
    # html = page.open(url).read()

    page = urllib.request.Request(url, data=None, headers=header)  # 法 2
    html = urllib.request.urlopen(page).read().decode()
    # print(html)
    return html


# 获取 app 信息
def get_app_info(url):
    import re
    soft_id = re.findall("soft_id/(\d+)?", url)[0]
    info = get_html(url)
    apk_icon_url = re.findall('<dt><img src="(.*?)" width="72" height="72"', info)[0]
    apk_name = re.findall('<h2 id="app-name"><span title="(.*?)">', info)[0]
    re_url = re.compile('class="js-downLog dbtn %s-btn normal"(.*?\.apk)' % soft_id)
    apk_download_url = re.findall(re_url, info)[0].split("=&url=")[1]
    apk_version = re.findall('<td><strong>版本：</strong>(.*?)<', info)[0]
    apk_version_code = re.findall("<!--versioncode:(\d+)-->", info)[0]
    apk_updatetime = re.findall('<strong>更新时间：</strong>(.*?)</td>', info)[0]
    apk_size = re.findall(' <span class="s-3">(\d+.\d+M)</span>', info)[0]
    apk_imgs = re.findall('<div id="scrollbar" data-snaps="(.*?)">', info)
    apk_img = (apk_imgs[0] if len(apk_imgs) else "").split(",")
    re_readme = re.compile('更新内容】</b><br/>(.*?)</div>', re.S)
    apk_update_readme1 = re.findall(re_readme, info)[0].split("<br />\r\n")
    apk_update_readme = [readme.strip() for readme in apk_update_readme1 if readme != ""]
    app_info = collections.OrderedDict()
    app_info = {
        "apk_channel_url": url,
        "apk_name": apk_name,
        "apk_icon_url": apk_icon_url,
        "apk_size": apk_size,
        'apk_url': apk_download_url,
        "apk_imgs": apk_img,
        "apk_version": apk_version, "apk_version_code": apk_version_code,
        "apk_updatetime": apk_updatetime,
        "apk_update_readme": apk_update_readme}

    # print(app_info)
    return app_info


def app_info(request):
    url = "http://zhushou.360.cn/detail/index/soft_id/847609"
    # url = "http://zhushou.360.cn/detail/index/soft_id/2981222"
    # url = "http://zhushou.360.cn/detail/index/soft_id/2751"
    # url = "http://zhushou.360.cn/detail/index/soft_id/3581"
    # print(get_html(url))
    info = get_app_info(url)
    return JsonResponse(info)


def show_appinfo(request):
    return render(request, "appinfo.html", locals())


def qqbot_start(request):
    import subprocess, sys
    my_command = "python I:\yzq\MyPythonTest\qqbot\qqbot_test.py"
    try:
        # sub_process = subprocess.Popen(my_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # out = sub_process.stdout.read().decode()
        # print(out)
        # with open("I:\yzq\MyPythonTest\qqbot\qqbot_log.txt", "ab+") as f:
        #     f.write(str(out))
        info = {"code": 200, "msg": "success"}
    except Exception as e:
        print(e)
        info = {"code": 400, "msg": "failed"}

    return JsonResponse(info)


def get_ticket(url_ticket, userid, password):
    body_ticket = u'username=%s&password=%s' % (userid, password)  # 床号，密码
    try:
        post_info = requests.post(url_ticket, data=body_ticket).text
        p = re.compile(r'ticket":"(.*?)"},"code')
        ticket_list = re.findall(p, post_info)
        # print('ticket =', ticket_list)
        body_info = {"ticket": '%s' % ticket_list[0]}

    except Exception as err:
        body_info = {"ticket": err}

    # return JsonResponse(body_info)
    return body_info


def show_ticket(request):
    url_ticket_in = r'http://192.168.2.175:8080/account/basic/ticket'  # 内网
    url_ticket_out = r'http://192.168.199.126:8080/account/basic/ticket'  # 外网
    url_login_in = r"http://192.168.2.171:8080/account/basic/login"
    url_login_out = r"https://apinyx.chuangshangapp.com/account/basic/login"

    if request.method == "POST" and request.POST:
        ticket_form = Ticket(request.POST)
        valid = ticket_form.is_valid()  # valid 判断是否有效
        if valid:
            form_data = ticket_form.cleaned_data
            # print(type(form_data), form_data)
            ticket_style = form_data["ticket_style"]
            userid = form_data["user_name"]
            password = form_data["user_password"]

            # userid = "137349027"
            # password = "q1234567"
            hearder = {"username": userid, "password": password}
            if ticket_style == "in":
                get_ticket_info = get_ticket(url_ticket_in, userid, password)
                get_ticket_info["userinfo"] = requests.post(url_login_in, data=hearder).text

            else:
                get_ticket_info = get_ticket(url_ticket_out, userid, password)
                get_ticket_info["userinfo"] = requests.post(url_login_out, data=hearder).text

            title = "Ticket %s | TestData" % ticket_style
    else:
        ticket_form = Ticket()

    return render(request, "ticket.html", locals())


def device_unlock(request):
    url_api_in = 'http://192.168.2.175:8080/inner/manage/user/untie/device'  # 内网
    url_api_out = 'http://192.168.199.126:8080/inner/manage/user/untie/device'  # 外网

    if request.method == "POST" and request.POST:
        device_form = DeviceId(request.POST)
        valid = device_form.is_valid()  # valid 判断是否有效
        if valid:
            form_data = device_form.cleaned_data
            api_model = form_data["api_model"]
            device_id = form_data["device_id"]
            body = {'machine_code': device_id}
            if api_model == "in":
                device_unlock_info = requests.post(url_api_in, body).text
            else:
                device_unlock_info = requests.post(url_api_out, body).text

            title = "Device Unlock %s | TestData" % api_model

    else:
        device_form = DeviceId()

    return render(request, "device_unlock.html", locals())


def register_code(request):
    # url_api_in = 'http://192.168.2.175:8080/inner/manage/user/untie/device'  # 内网

    title = "Register Code | TestData"
    if request.method == "POST" and request.POST:
        data_form = RegisterCode(request.POST)
        valid = data_form.is_valid()  # valid 判断是否有效
        if valid:
            form_data = data_form.cleaned_data
            phone = form_data["phone"]
            url_api_out = 'http://guojia.api.l99.com/cgi-bin/vericode.py?mobilePhone=%s&appid=CS' % phone
            data = requests.get(url_api_out).text
    else:
        data_form = RegisterCode()

    return render(request, "register_code.html", locals())
