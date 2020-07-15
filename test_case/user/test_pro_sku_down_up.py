import pytest
import uri as uri
from Tools.scripts.make_ctype import method

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

@pytest.mark.up
@pytest.mark.down
@pytest.mark.skip(5>1,reason='跳过')
def test_pronew(pub_data):
    method ="POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '解冻后充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "明哥威武",
  "colors": [
    "black"
  ],
  "price": 1224,
  "productCode": "自动生成 字符串 6 数字字母",
  "productName": "自动生成 字符串 8 数字字母",
  "sizes": [
    "s"
  ],
  "type": "l"
}'''

    json_path = [{"productCode":'$.data[0].productCode'},{"skuCode":'$.data[0].skuCode'}]


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)


@pytest.mark.down
def test_downProdRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '下载某个模板'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'pridCode': '${productCode}'}


    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

    with open("aaa.xls","wb") as f:
        f.write(r.content)  # 获取响应中的（原始数据）二进制数据byte



@pytest.mark.up
def test_updateProdRepertory(pub_data):
    method = "post"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '上传某个模板'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    params={'pridCode': '${productCode}'}
    f = open("aaa.xls", "rb")  # post请求，上传文件
    files = {"file": f}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(files=files,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
    f.close()

