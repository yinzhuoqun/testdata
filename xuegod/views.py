# -*- coding: utf-8 -*-
# Create your views here.


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.conf import settings

from xuegod.models import *
from xuegod.forms import *

from django.db import connection
from django.template import RequestContext  # csrf
from django.http import StreamingHttpResponse

import os, time, socket
import collections  # 有序字典
# import faker
# import uuid
import requests
import re, random, json
from ipware.ip import get_ip


# import random

def page_not_found(request):
    return render_to_response("404_1.html")


def server_error(request):
    return render_to_response("500_2.html")


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
    url_login_in = r"http://192.168.2.171:8080/account/basic/login"
    url_login_out = r"https://apinyx.chuangshangapp.com/account/basic/login"

    headers = {
        "User-Agent": r"com.l99.bed/5.7.1(Android OS 5.0.2,MI 2S)"
    }

    proxies = {
        "http": "192.168.66.51:80",
    }
    machine_code_list = ["863121026886804", "867886022015683", "353440060156719"]

    data_ticket = {
        # "username": userid,
        # "password": password,
        "machine_code": random.choice(machine_code_list),
        "local_name": '深圳',
        "market": "chuangshang_yingyongbao",
        "client:": "key:BedForAndroid",
        "version:": "1.0",
        "lat": "22.541304",
        "lng": "113.948919",

    }

    # data = TestId.objects.using('alimysql').filter(user_flag=0)  # filter 列表 0是内网 1是外网
    # data1 = TestId.objects.using('alimysql').filter(user_flag=1)  # 外网
    # for field in data1:
    #     data_ticket['username'] = str(field.user_id)
    #     data_ticket['password'] = field.user_password
    #     # login_result = requests.post(url_login_in, headers=headers, data=data_ticket).json()  # 内网
    #     login_result = requests.post(url_login_out, headers=headers, data=data_ticket).json()  # 外网
    #     login_result = {'code': 1000}  # test
    #     if login_result['code'] == 1000:
    #         user_note_old = \
    #             TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).values("user_note")[0][
    #                 "user_note"]
    #         if user_note_old.find("，账号屏蔽") + user_note_old.find("，密码错误") + user_note_old.find("，账号不存在") > -1:
    #             user_note_new = user_note_old.replace("，密码错误", "").replace("，账号屏蔽", "").replace("，账号不存在", "")
    #             TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).update(
    #                 user_note=user_note_new)
    #             # print(data_ticket['username'], login_result['data']['user']['name'])
    #     elif login_result['code'] == 11026:  # 密码错误
    #         user_note_old = \
    #             TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).values("user_note")[0][
    #                 "user_note"]
    #         TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).update(
    #             user_note="%s，密码错误" % user_note_old)
    #         print(data_ticket['username'], login_result['msg'])
    #     elif login_result['code'] == 11004:  # 账号屏蔽
    #         user_note_old = \
    #             TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).values("user_note")[0][
    #                 "user_note"]
    #         TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).update(
    #             user_note="%s，账号屏蔽" % user_note_old)
    #         print(data_ticket['username'], login_result['msg'])
    #     elif login_result['code'] == 11002:  # 账号不存在
    #         user_note_old = \
    #             TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).values("user_note")[0][
    #                 "user_note"]
    #         TestId.objects.using("alimysql").filter(user_id=data_ticket["username"]).update(
    #             user_note="%s，账号不存在" % user_note_old)
    #         print(data_ticket['username'], login_result['msg'])
    #     elif login_result['code'] == 11001:  # ip 受限
    #         print(data_ticket['username'], login_result['msg'])
    #     else:
    #         # print(data_ticket['username'], login_result['msg'])
    #         print(data_ticket['username'], login_result['code'], login_result['msg'])

    if request.method == "POST" and request.POST:
        check_id = request.POST.get("check_id", None)
        if check_id:
            check_type = TestId.objects.using("alimysql").filter(pk=check_id).values("user_flag")
            if check_type.exists():
                user_id = TestId.objects.using("alimysql").filter(pk=check_id).values("user_id")[0]["user_id"]
                data_ticket['username'] = str(user_id).strip()
                user_password = TestId.objects.using("alimysql").filter(pk=check_id).values("user_password")[0][
                    "user_password"]
                data_ticket['password'] = user_password.strip()
                user_note_old = TestId.objects.using("alimysql").filter(pk=check_id).values("user_note")[0][
                    "user_note"]
                if check_type[0]["user_flag"] == "0":
                    login_result = requests.post(url_login_in, headers=headers, data=data_ticket).json()
                    if login_result['code'] == 11026:  # 密码错误
                        if user_note_old.find("，密码错误") < 0:
                            TestId.objects.using("alimysql").filter(pk=check_id).update(
                                user_note="%s，密码错误" % user_note_old)
                    elif login_result['code'] == 11004:  # 账号屏蔽
                        if user_note_old.find("，账号屏蔽") < 0:
                            TestId.objects.using("alimysql").filter(pk=check_id).update(
                                user_note="%s，账号屏蔽" % user_note_old)
                    else:
                        TestId.objects.using("alimysql").filter(pk=check_id).update(
                            user_note=user_note_old.replace("，密码错误", "").replace("，账号屏蔽", "").replace("，账号不存在", ""))
                else:
                    login_result = requests.post(url_login_out, headers=headers, data=data_ticket).json()
                    if login_result['code'] == 11026:  # 密码错误
                        if user_note_old.find("，密码错误") < 0:
                            pass
                            # TestId.objects.using("alimysql").filter(pk=check_id).update(
                            #     user_note="%s，密码错误" % user_note_old)
                    elif login_result['code'] == 11004:  # 账号屏蔽
                        if user_note_old.find("，账号屏蔽") < 0:
                            TestId.objects.using("alimysql").filter(pk=check_id).update(
                                user_note="%s，账号屏蔽" % user_note_old)
                    else:
                        TestId.objects.using("alimysql").filter(pk=check_id).update(
                            user_note=user_note_old.replace("，密码错误", "").replace("，账号屏蔽", "").replace("，账号不存在", ""))
            else:
                msg = "测试账号库中未检测到账号"

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


def dd_text_post(url, msg, atMoblies, atAll="flase"):
    body = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "atMobiles": atMoblies,
            "isAtAll": atAll
        }
    }
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.post(url, headers=headers, data=json.dumps(body))
    # print(r.text)
    return r.text


def ip_location(query_ip):
    appcode = 'f832858116c44a348db4f65376e3f46d'
    url = 'http://saip.market.alicloudapi.com/ip?ip=%s' % query_ip
    headers = {'Authorization': 'APPCODE %s' % appcode}
    location_info = requests.get(url, headers=headers).json()
    try:
        if location_info["showapi_res_body"]["ret_code"] == 0:
            location = '%s %s %s %s' % (location_info["showapi_res_body"]["country"],
                                        location_info["showapi_res_body"]["region"],
                                        location_info["showapi_res_body"]["city"],
                                        location_info["showapi_res_body"]["isp"])
        else:
            location = "局域网或未知区域"
    except Exception as e:
        location = "IP 地址归属地识别失败"

    return location


def app_list(request):
    # print(os.getcwd())
    show_path = r'media/app'
    # print(os.path.abspath("."))

    # os.getcwd() 拿到的是 Apache 下 http.conf 里的 ServerRoot 路径
    # app_path = os.path.join(os.getcwd(), show_path).replace('\\', '/')
    # app_path = os.path.join(os.path.abspath('.'), show_path).replace('\\', '/')
    app_path = r"I:\yzq\MyPythonTest\yzqProgram\media\app".replace('\\', '/')
    ip = get_ip(request)
    ip_local = ["192.168.66.55", "169.254.111.198"]
    # ip_local = []  # test
    form_dd_show = True  #
    url_ddbots_use = [{'url_nickname': ''}]
    if socket.gethostbyname(socket.gethostname()) not in ip_local:
        show_path = r'media/upload'
        app_path = img_save_path = os.path.join(os.getcwd(), show_path).replace('\\', '/')
        # app_path = img_save_path = os.path.join(os.path.abspath('.'), show_path).replace('\\', '/')
        form_dd_show = False
    else:
        img_save_path = r"I:/91UserData/ScreenCapture"  # 192.168.66.55
        at_names = Resume.objects.filter(phone_status="1").exclude(ip="0.0.0.0").values("name")
        at_names_select = Resume.objects.filter(phone_status="0", phone_status_select="1").exclude(ip=ip).values("name")
        # url_ddbot = HomePage.objects.filter(url_type="dd").values("url_nickname")
        url_ddbot = HomePage.objects.filter(url_type="dd").values("url_nickname")
        if settings.DEBUG == True:
            url_ddbot_obj = HomePage.objects.filter(url_type="dd", url_status_use="1", id=29).values(
                "url_nickname")
            # print(url_ddbot_obj)
            if url_ddbot_obj.exists():
                url_ddbots_use = url_ddbot_obj

        else:
            url_ddbot_obj = HomePage.objects.filter(url_type="dd", url_status_use="1").values("url_nickname")
            if url_ddbot_obj.exists():
                url_ddbots_use = url_ddbot_obj
            url_ddbots_select = HomePage.objects.filter(url_type="dd", url_status="1", url_status_use="0").values(
                "url_nickname").order_by("url_order")
            # print(url_ddbots_use)
            # print(url_ddbots_select)

    app_save_path = app_path
    # print(app_save_path)
    # print(img_save_path)
    app_list = [name for name in os.listdir(app_path) if os.path.isfile(os.path.join(app_path, name))]  # 不包含文件夹
    # app_list = os.listdir(app_path)  # 包含文件夹

    app_dict = {}
    for app in app_list:
        # app_info_dict = {} # 无序字典
        app_info_dict = collections.OrderedDict()  # 有序字典, 需要导入 collections
        # os.stat().st_ctime st_atime (访问时间), st_mtime (修改时间), st_ctime（搜索创建时间）
        app_unix_time = os.stat(os.path.join(app_path, app)).st_mtime
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

    # 是否显示上传表单
    forms_show_status = "1"  # 默认打开
    forms_show_obj = Resume.objects.filter(ip="0.0.0.0")
    if forms_show_obj.exists():
        forms_show_status = forms_show_obj.values("phone_status_select")[0]["phone_status_select"]
    if forms_show_status == "1":
        web_title = "上传下载文件 | TestData"
    else:
        web_title = "下载文件 | TestData"

    # token = ''
    # postToken = str(uuid.uuid4())
    # if request.method == "GET":
    #     # token = str(uuid.uuid4())  # 采用随机数
    #     token = "allow"
    #     # 在服务端session中添加key认证，避免用户重复提交表单
    #     request.session['postToken'] = token
    #
    #     return render(request, "app.html", locals())
    # ip = get_ip(request)
    # # ip = "192.168.66.65" # test
    # ipinfo = Resume.objects.filter(ip=ip)
    # if ipinfo.exists():
    #     print(ipinfo.values("phone")[0]["phone"])
    # print(ipinfo.values("ip", "phone"))


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
        #  print(dir(file))
        # ['DEFAULT_CHUNK_SIZE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__',
        #  '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__',
        #  '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__',
        #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_get_closed',
        #  '_get_name', '_get_size', '_get_size_from_underlying_file', '_name', '_set_name', '_set_size', '_size',
        #  'charset', 'chunks', 'close', 'closed', 'content_type', 'content_type_extra', 'encoding', 'field_name', 'file',
        #  'fileno', 'flush', 'isatty', 'multiple_chunks', 'name', 'newlines', 'open', 'read', 'readinto', 'readline',
        #  'readlines', 'seek', 'size', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
        if not file:
            uploadfile_msg = "请选择文件"
            return render(request, "app.html", locals())
        else:
            uploadfile_status = "1"
            uploadfile_obj = Resume.objects.filter(ip="0.0.0.0")  # 从ip为 0.0.0.0 的上传使用状态来判断是否禁止上传文件
            if uploadfile_obj.exists():
                uploadfile_status = uploadfile_obj.values("phone_status")[0]["phone_status"]  # 是否禁止上传文件
            if uploadfile_status == "1":
                if file.name.endswith(('.apk', '.json')):
                    destination = open(os.path.join(app_save_path, file.name), 'wb+')
                else:
                    destination = open(os.path.join(img_save_path, file.name), 'wb+')
                try:
                    for chunk in file.chunks():
                        destination.write(chunk)
                    destination.close()
                except Exception as e:
                    uploadfile_msg = "上传失败，即将跳转上一页..."

                finally:
                    uploadfile_msg = "上传成功，即将跳转..."
                    # three_url_ddbot = "https://oapi.dingtalk.com/robot/send?access_token=a11467840d64d7ae39f0eb48c471d3973c701e13b29c10bbceca17c188b8e376"
                    # qa_url_ddbot = "https://oapi.dingtalk.com/robot/send?access_token=09d43b3b9fcb66e962a1c7bad06401ab831439c7809f12b511159c6ca2e15a11"
                    # csdev_url_ddbot = "https://oapi.dingtalk.com/robot/send?access_token=400e0e7bb9cca3ca33c086d24c7ead6a07929bf1cfa724d9a48fdff48fb93f53"
                    # print(dir(request.POST))
                    # ['__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__',
                    #  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
                    #  '__getstate__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
                    #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
                    #  '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
                    #  '_assert_mutable', '_encoding', '_iteritems', '_iterlists', '_itervalues', '_mutable',
                    #  'appendlist', 'clear', 'copy', 'dict', 'encoding', 'fromkeys', 'get', 'getlist', 'items', 'keys',
                    #  'lists', 'pop', 'popitem', 'setdefault', 'setlist', 'setlistdefault', 'update', 'urlencode',
                    #  'values']

                    if request.POST.get("dd_send", None):
                        dd_send = request.POST['dd_send']  # 是否发送钉钉群消息
                    else:
                        dd_send = "False"  # 是否发送钉钉群消息
                    # ip = get_ip(request)  # 请求IP
                    url_request = request.get_host()  # 服务器地址
                    file_size = file.size
                    if file_size > 1024 * 1024:
                        file_size = "%.2fMB" % (file_size / 1024 / 1024)
                    else:
                        file_size = "%.2fKB" % (file_size / 1024)
                    if file.name.endswith('.apk') and dd_send == "True":
                        at_moblies = []
                        if file.name.lower().find("chuangshang") + file.name.lower().find(
                                "l99") + file.name.lower().find("bed") > -3:
                            # 选择网页添加 @的人
                            at_names_select_enable = request.POST.getlist("at_names_select_button", [])
                            # print(at_names_select_enable, type(at_names_select_enable))
                            at_names_select = Resume.objects.filter(phone_status="0", phone_status_select="1").exclude(
                                ip=ip).values("name")
                            for name in at_names_select_enable:
                                at_names_select_one = at_names_select.filter(name=name).values("phone")
                                if at_names_select_one.exists():
                                    at_moblies.append(at_names_select_one.values("phone")[0]["phone"])

                            # 选择手机使用状态为必定使用的人
                            ip_use = Resume.objects.filter(phone_status="1").order_by('phone_order')
                            # print(ip_use.values("phone", "ip"))
                            for ip_phone in ip_use.values("phone", "ip"):
                                at_moblies.append(ip_phone["phone"])
                            if ip is not None:
                                ipinfo = Resume.objects.filter(phone_status_select="1", ip=ip)
                                if ipinfo.exists():
                                    at_moblies.append(ipinfo.values("phone")[0]["phone"])
                                at_moblies = sorted(set(at_moblies), key=at_moblies.index)  # @的人去重
                            apk_url = "http://%s/%s/%s" % (url_request, show_path, file.name)
                            msg_updata = request.POST.get("msg_updata", None)
                            msg_upload_success = "Android 有新包啦：%s\n%s" % (apk_url, msg_updata)

                            url_ddbots_select = HomePage.objects.filter(url_type="dd", url_status="1",
                                                                        url_status_use="0").values("url_nickname")
                            # print(url_ddbots_select)
                            url_ddbots_select_name = request.POST.getlist("url_nickname_select_button", [])
                            # print("url_ddbots_select_name", url_ddbots_select_name)

                            url_ddbots_all = []
                            for nickname in url_ddbots_select_name:
                                url_ddbots_select_one = url_ddbots_select.filter(url_nickname=nickname).values(
                                    "url_nickname")
                                if url_ddbots_select_one.exists():
                                    url_ddbots_all.append(url_ddbots_select_one.values("url")[0]["url"])
                            # print("url_ddbots_all", url_ddbots_all)
                            # print(url_ddbots_use)
                            for nickname in url_ddbots_use:
                                # print("nickname", nickname)
                                url_ddbots_one = HomePage.objects.filter(url_type="dd", url_status_use="1",
                                                                         url_nickname=nickname["url_nickname"]).values(
                                    "url_nickname")
                                if url_ddbots_one.exists():
                                    url_ddbots_all.append(url_ddbots_one.values("url")[0]["url"])
                            # url_ddbots_all.append(three_url_ddbot)
                            # print("url_ddbots_all", url_ddbots_all)
                            if len(url_ddbots_all) == 0:
                                # msg_upload_success = "File: %s\nSize：%s\nUserIP: %s（%s）\nServer: %s" % (
                                #     file.name, file_size, ip, ip_location(ip), url_request)
                                url_ddbot_obj = HomePage.objects.filter(url_type="dd", id=29).values("url")
                                if url_ddbot_obj.exists():
                                    my_url_ddbot = url_ddbot_obj[0]["url"]
                                    dd_text_post(my_url_ddbot, msg_upload_success, atMoblies=["18679600250"],
                                                 atAll="false")

                            url_ddbots_all = sorted(set(url_ddbots_all), key=url_ddbots_all.index)  # 保持排序去重
                            # print("url_ddbots_all", url_ddbots_all)
                            for url_ddbot in url_ddbots_all:
                                dd_text_post(url_ddbot, msg_upload_success, atMoblies=at_moblies, atAll="false")
                        else:
                            msg_upload_success = "File: %s\nSize：%s\nUserIP: %s（%s）\nServer: %s" % (
                                file.name, file_size, ip, ip_location(ip), url_request)
                            url_ddbot_obj = HomePage.objects.filter(url_type="dd", id=29).values("url")
                            if url_ddbot_obj.exists():
                                my_url_ddbot = url_ddbot_obj[0]["url"]
                                dd_text_post(my_url_ddbot, msg_upload_success, atMoblies=["18679600250"],
                                             atAll="false")
                    else:
                        msg_upload_success = "File: %s\nSize：%s\nUserIP: %s（%s）\nServer: %s" % (
                            file.name, file_size, ip, ip_location(ip), url_request)

                        url_ddbot_obj = HomePage.objects.filter(url_type="dd", id=29).values("url")
                        if url_ddbot_obj.exists():
                            my_url_ddbot = url_ddbot_obj[0]["url"]
                            dd_text_post(my_url_ddbot, msg_upload_success, atMoblies=["18679600250"],
                                         atAll="false")

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
            else:
                uploadfile_msg = "管理员禁止上传"
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
    info = Resume.objects.filter(name="尹卓群")
    if info:
        phone_mobile = info[0].phone
        email = info[0].email
    else:
        phone_mobile = "18679600250"
        email = "yinzhuoqun@vip.qq.com"

    cuurent_date = time.localtime(time.time())  # 获取当前时间
    year_time = cuurent_date.tm_year
    age = year_time - 1990  # 年龄

    work_experience = year_time - 2011  # 工作经验时长

    return render(request, 'resume_yzq.html', locals())


# 读取网页
def get_html(url, ref=None):
    import urllib.request
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
    html = urllib.request.urlopen(page)
    if html.code == 200:
        return html.read().decode()
    else:
        return None


# 获取 app 信息
def get_app_info(url):
    import re
    soft_id = re.findall("soft_id/(\d+)?", url)[0]

    info = get_html(url)
    if info:
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
        get_app_info = collections.OrderedDict()
        get_app_info = {
            "apk_channel_url": url,
            "apk_name": apk_name,
            "apk_icon_url": apk_icon_url,
            "apk_size": apk_size,
            'apk_url': apk_download_url,
            "apk_imgs": apk_img,
            "apk_version": apk_version, "apk_version_code": apk_version_code,
            "apk_updatetime": apk_updatetime,
            "apk_update_readme": apk_update_readme}
        app_info = {"status_code": 1000, "data": get_app_info, "msg": "请求成功"}
    else:
        app_info = {"status_code": 1004, "data": {}, "msg": "获取信息失败"}
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
    headers = {
        "User-Agent": r"com.l99.bed/5.7.1(Android OS 5.0.2,MI 2S)"
    }
    try:
        post_info = requests.post(url_ticket, headers=headers, data=body_ticket).text
        p = re.compile(r'ticket":"(.*?)"},"code')
        ticket_list = re.findall(p, post_info)
        # print('ticket =', ticket_list)
        body_info = {"ticket": '%s' % ticket_list[0]}

    except Exception as err:
        body_info = {"ticket": err}

    # return JsonResponse(body_info)
    return body_info


def show_ticket(request):
    url_ticket_in1 = r'http://192.168.2.171:8080/account/basic/ticket'  # 内网
    url_ticket_in2 = r'http://192.168.2.175:8080/account/basic/ticket'  # 内网
    # url_ticket_out = r'http://192.168.199.126:8080/account/basic/ticket'  # 外网 公司
    url_ticket_out = r'https://apinyx.chuangshangapp.com/account/basic/ticket'  # 外网
    url_login_in1 = r"http://192.168.2.171:8080/account/basic/login"
    url_login_in2 = r"http://192.168.2.175:8080/account/basic/login"
    url_login_out = r"https://apinyx.chuangshangapp.com/account/basic/login"

    headers = {
        "User-Agent": r"com.l99.bed/5.7.0(Android OS 5.0.2,MI 2S)",

    }

    if request.method == "POST" and request.POST:
        ticket_form = Ticket(request.POST)
        valid = ticket_form.is_valid()  # valid 判断是否有效
        if valid:
            form_data = ticket_form.cleaned_data
            # print(type(form_data), form_data)
            ticket_style = form_data["ticket_style"]
            userid = form_data["user_name"].strip()
            password = form_data["user_password"]

            # userid = "137349027"
            # password = "q1234567"
            machine_code_list = ["863121026886804", "867886022015683", "353440060156719"]
            data_ticket = {
                "username": userid,
                "password": password,
                "machine_code": random.choice(machine_code_list),
                "local_name": '深圳',
                "market": "chuangshang_yingyongbao",
                "client:": "key:BedForAndroid",
                "version:": "1.0",
                "lat": "22.541304",
                "lng": "113.948919",

            }
            if ticket_style == "in":
                get_user_info = {}
                import urllib
                url_result = urllib.parse.urlparse(url_ticket_in1)
                if requests.get(url_result.scheme + "://" + url_result.netloc).status_code == 200:
                    get_user_info["ipinfo"] = requests.post(url_login_in1, headers=headers, data=data_ticket).json()
                    get_user_info["ticket"] = get_ticket(url_ticket_in1, userid, password)["ticket"]
                else:
                    url_result = urllib.parse.urlparse(url_ticket_in2)
                    if requests.get(url_result.scheme + "://" + url_result.netloc).status_code == 200:
                        get_user_info["ipinfo"] = requests.post(url_login_in2, headers=headers, data=data_ticket).json()
                        get_user_info["ticket"] = get_ticket(url_ticket_in2, userid, password)["ticket"]
                    else:
                        get_user_info["ticket"] = "内网服务器未开启"
                # print(get_user_info["ticket"])

                if get_user_info["ipinfo"]["code"] == 1000:
                    # import urllib
                    # url_result = urllib.parse.urlparse(url_ticket_in1)
                    # if requests.get(url_result.scheme + "://" + url_result.netloc).status_code == 200:
                    #     get_user_info["ticket"] = get_ticket(url_ticket_in1, userid, password)["ticket"]
                    # else:
                    #     url_result = urllib.parse.urlparse(url_ticket_in2)
                    #     if requests.get(url_result.scheme + "://" + url_result.netloc).status_code == 200:
                    #         get_user_info["ticket"] = get_ticket(url_ticket_in2, userid, password)["ticket"]
                    #     else:
                    #         get_user_info["ticket"] = "内网服务器未开启"

                    get_user_info["account_id"] = get_user_info["ipinfo"]["data"]["user"]["account_id"]
                    # print(get_user_info["account_id"])

                    api_dev_charm = 'https://devapi.chuangshangapp.com/account/info/rank/info?target_id=%s&rank_type=1' % \
                                    get_user_info["account_id"]
                    api_dev_wealth = 'https://devapi.chuangshangapp.com/account/info/rank/info?target_id=%s&rank_type=2' % \
                                     get_user_info["account_id"]
                    api_dev_vip = 'https://devapi.chuangshangapp.com/account/info/rank/info?target_id=%s&rank_type=3' % \
                                  get_user_info["account_id"]

                    charm_info = requests.get(api_dev_charm, headers=headers, timeout=5)
                    if charm_info.status_code == 200:
                        # get_user_info['charm_info'] = requests.get(api_dev_charm, headers=headers).json()
                        get_user_info['charm_info'] = charm_info.json()
                        if get_user_info['charm_info']['code'] == 1000:
                            get_user_info['charm_values'] = get_user_info['charm_info']['data']['current_num']
                            get_user_info['charm_level'] = get_user_info['charm_info']['data']['current_level']
                        get_user_info['wealth_info'] = requests.get(api_dev_wealth).json()
                        if get_user_info['wealth_info']['code'] == 1000:
                            get_user_info['wealth_values'] = get_user_info['wealth_info']['data']['current_num']
                            get_user_info['wealth_level'] = get_user_info['wealth_info']['data']['current_level']
                        get_user_info['vip_info'] = requests.get(api_dev_vip).json()
                        if get_user_info['vip_info']['code'] == 1000:
                            get_user_info['vip_values'] = get_user_info['vip_info']['data']['current_num']
                            get_user_info['vip_level'] = get_user_info['vip_info']['data']['current_level']

            else:
                get_user_info = {}
                # get_ticket_info = get_ticket(url_ticket_out, userid, password)  # 公司内网
                get_user_info["ipinfo"] = requests.post(url_login_out, headers=headers, data=data_ticket).json()
                if get_user_info["ipinfo"]["code"] == 1000:
                    get_user_info["ticket"] = requests.post(url_ticket_out, data=data_ticket).json()["data"]["ticket"]
                    get_user_info["account_id"] = get_user_info["ipinfo"]["data"]["user"]["account_id"]

                    api_idc_charm = 'https://apinyx.l99.com/account/info/rank/info?target_id=%s&rank_type=1' % \
                                    get_user_info["account_id"]
                    api_idc_wealth = 'https://apinyx.l99.com/account/info/rank/info?target_id=%s&rank_type=2' % \
                                     get_user_info["account_id"]
                    api_idc_vip = 'https://apinyx.l99.com/account/info/rank/info?target_id=%s&rank_type=3' % \
                                  get_user_info["account_id"]

                    get_user_info['charm_info'] = requests.get(api_idc_charm).json()
                    if get_user_info['charm_info']['code'] == 1000:
                        get_user_info['charm_values'] = get_user_info['charm_info']['data']['current_num']
                        get_user_info['charm_level'] = get_user_info['charm_info']['data']['current_level']
                    get_user_info['wealth_info'] = requests.get(api_idc_wealth).json()
                    if get_user_info['wealth_info']['code'] == 1000:
                        get_user_info['wealth_values'] = get_user_info['wealth_info']['data']['current_num']
                        get_user_info['wealth_level'] = get_user_info['wealth_info']['data']['current_level']
                    get_user_info['vip_info'] = requests.get(api_idc_vip).json()
                    if get_user_info['vip_info']['code'] == 1000:
                        get_user_info['vip_values'] = get_user_info['vip_info']['data']['current_num']
                        get_user_info['vip_level'] = get_user_info['vip_info']['data']['current_level']

            if get_user_info["ipinfo"]["code"] == 1000:
                if "mobile_phone" in get_user_info["ipinfo"]["data"]["user"].keys():
                    phone = get_user_info["ipinfo"]["data"]["user"]["mobile_phone"]
                    try:
                        appcode = 'f832858116c44a348db4f65376e3f46d'
                        url = 'http://showphone.market.alicloudapi.com/6-1?num=%s' % phone
                        headers = {'Authorization': 'APPCODE %s' % appcode}
                        phone_location_info = requests.get(url, headers=headers).json()
                        location = '%s %s %s' % (phone_location_info["showapi_res_body"]["prov"],
                                                 phone_location_info["showapi_res_body"]["city"],
                                                 phone_location_info["showapi_res_body"]["name"])
                    except Exception as e:
                        location_re = re.findall(r"carrier:'(.+?)'", requests.get(
                            r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=%s" % phone).text)
                        if location_re:
                            location = location_re[0]
                        else:
                            location = "手机号码未知归属地"

            title = "Ticket %s | TestData" % ticket_style
    else:
        ticket_form = Ticket()

    return render(request, "ticket.html", locals())


def device_unlock(request):
    url_api_in = 'http://192.168.2.171:8080/inner/manage/user/untie/device'  # 内网
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
    agent_list = [
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0']
    headers = {
        # 'Referer': '%s' % ref,
        'User-Agent': '%s' % random.choice(agent_list)
    }
    # url_api_in = 'http://192.168.2.175:8080/inner/manage/user/untie/device'  # 内网

    title = "Register Code | TestData"
    if request.method == "POST" and request.POST:
        data_form = RegisterCode(request.POST)
        valid = data_form.is_valid()  # valid 判断是否有效
        if valid:
            form_data = data_form.cleaned_data
            phone = form_data["phone"]
            url_api_out = 'http://guojia.api.l99.com/cgi-bin/vericode.py?mobilePhone=%s&appid=CS' % phone
            data = requests.get(url_api_out, headers=headers, timeout=3).text
    else:
        data_form = RegisterCode()

    return render(request, "register_code.html", locals())


def user_ip(request):
    title = "IP | TestData"
    mygroup_url_ddbot = "https://oapi.dingtalk.com/robot/send?access_token=45776b0caa3979d86cbb758d7aaede3d2c62940bdd04bcfbe96b607a9348f34e"
    ip = get_ip(request)
    dd_text_post(mygroup_url_ddbot, ip, atMoblies=["18679600250"],
                 atAll="false")
    return render(request, "ip.html", locals())


def check_password(request):
    url_login_in = r"http://192.168.2.171:8080/account/basic/login"
    url_login_out = r"https://apinyx.chuangshangapp.com/account/basic/login"


def vest_info(request):
    # b = VestInfo.objects.get(id=3)
    # print(b.position)
    # e = VestAccount.objects.get(account="140578508")
    # print(e.id_set.get())
    # print(request.get_host())  # 服务器地址 + 端口
    if request.get_host().split(":")[0] in settings.IP_LOCAL:
        vest_info = VestInfo.objects.filter(show_status=True).order_by("position")
    if request.method == "POST" and request.POST:
        find_api = "https://apinyx.chuangshangapp.com/account/info/search/user?query="
        url_ticket_out = 'https://apinyx.chuangshangapp.com/account/basic/ticket'  # 外网
        find_id = request.POST.get("myInput", None)
        # print(request.POST)
        if find_id:
            if find_id == "1000":
                if request.get_host().split(":")[0] not in settings.IP_LOCAL:
                    vest_info = VestInfo.objects.filter(show_status=True)
            else:
                result = VestAccount.objects.filter(account__contains=find_id)  # 字段名__模糊查询内容
                if result.exists():
                    find_id = [x["account"] for x in result.values()]
                    find_result = []
                    for uid in find_id:
                        # owner = VestAccount.objects.get(account=uid).id_set.first()
                        name = VestAccount.objects.get(account=uid)
                        owner = name.id_set.first()
                        args = "{%22type%22:%22search%22,%22rows%22:20,%22start%22:%220%22,%22keyword%22:%22long_no:" \
                               + uid + "%20OR%20name:\%22\%22%22}"
                        url = find_api + args
                        headers = get_ticket(url_ticket_out, "139828156", "q1234567")
                        req_api = requests.get(url, headers=headers).json()
                        if req_api["code"] == 1000:
                            user_name = req_api['data']['users'][0]["name"]
                            user_gender = req_api['data']['users'][0]["gender"]
                            find_result.append({'uid': uid, 'owner': owner, 'name': user_name,
                                                'gender': user_gender})
                            name.name = user_name
                            name.gender = user_gender
                            user_name_sql = VestAccount.objects.filter(account=uid).values("name")[0]["name"]
                            user_gender_sql = VestAccount.objects.filter(account=uid).values("gender")[0]["gender"]
                            # print(user_name, user_name_sql)
                            if user_name != user_name_sql:
                                name.save(update_fields=["name"])
                            if user_gender != user_gender_sql:
                                name.save(update_fields=["gender"])
                        else:
                            find_result.append({'uid': uid, 'owner': owner})
                else:
                    find_result = [{'uid': '马甲库未收录'}]

    return render(request, "vest_info.html", locals())


def vest_api(request):
    vest_info = VestInfo.objects.all()
    try:
        vests = []
        for x in vest_info:
            for y in x.id_info.all():
                # print(y.account)
                vests.append(y.account)
        result = {
            "code": 1000,
            "msg": "获取马甲账号列表成功",
            "vests": sorted(vests),
            "exception": None,
        }

    except Exception as e:
        result = {
            "code": 1004,
            "msg": "获取马甲账号列表失败",
            "vests": None,
            "exception": e,
        }

    return JsonResponse(result)
