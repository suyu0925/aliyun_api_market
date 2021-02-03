import sys
import os
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()
appcode = os.getenv("APPCODE")


def sjsys():
    """ 贵州数据宝网络科技有限公司
        https://market.aliyun.com/products/57126001/cmapi00035240.html
    """
    host = 'http://sjsys.market.alicloudapi.com'
    path = '/communication/personal/1979'
    method = 'POST'
    bodys = {}
    url = host + path

    bodys['idcard'] = '''32132419860817421X'''
    bodys['mobile'] = '''13636643334'''
    bodys['name'] = '''张三'''
    post_data = urlencode(bodys).encode('utf-8')
    request = Request(url, data=post_data, method=method)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content-Type
    request.add_header(
        'Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urlopen(request)
    content = response.read()
    if (content):
        print(content)


def shumaidata():
    """ 杭州数脉科技有限公司
        https://market.aliyun.com/products/57000002/cmapi026100.html
    """
    host = 'https://mobile3elements.shumaidata.com'
    path = '/mobile/verify_real_name'
    method = 'POST'
    bodys = {}
    url = host + path

    bodys['idcard'] = '''32132419860817421X'''
    bodys['mobile'] = '''13636643334'''
    bodys['name'] = '''张三'''
    post_data = urlencode(bodys).encode('utf-8')
    request = Request(url, data=post_data, method=method)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content-Type
    request.add_header(
        'Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urlopen(request)
    content = response.read()
    if (content):
        print(content)
