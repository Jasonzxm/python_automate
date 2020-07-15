import random

import allure
import uri as uri
from Tools.scripts.make_ctype import method
import requests
from test_case.conftest import pub_data
from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''


#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tools.api import request_tool

@allure.title("扣款接口-账户余额不足场景")
# 修改用例标题
@allure.feature("用户管理模块")
# 一级分类
@allure.story("充值提现模块")
# 二级分类
def test_recharge(db):
    with allure.step("第一步,执行sql、语句"):
        res =db.select_execute("select account_name from t_cst_account where STATUS=0 AND account_name is not null")
    with allure.step("第二步，查询结果随机获取一个，取第一条数据"):
        account_name=random.choice(res)[0]
    with allure.step("第三步，准备请求数据"):
        data={
  "accountName":account_name,
  "changeMoney": 111
}

    with allure.step("第四步，发送请求数据"):
        r = requests.request("post",url="http://192.168.1.151:8084/acc/recharge",json=data)
    with allure.step("第五步，获取请求结果"):
        print(r.text)
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)
    with allure.step("第六步、获取响应内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响应正文",allure.attachment_type.TEXT)
    with allure.step("第七步、断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("账户余额不足","预期结果",allure.attachment_type.TEXT)
        assert "账户余额不足" in r.text





    # pytest test_case/test_allure.py --alluredir=reports/xml

    # allure generate reports/xml -o reports/html