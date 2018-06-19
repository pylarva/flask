# !/usr/bin/env python
# -*- coding:utf-8 -*-

# session原理及自定义session
# 1) 请求刚到来创建特殊字典, 并添加到上下文环境Local中
#    调用关系:
#    self.session_interface.open_session(self, request)
#    由于默认的app中session_interface=SecureCookieSessionInterface()
#       SecureCookieSessionInterface().open_session(self, request)
#    自定制session_interface=MySessionInterface()
#       MySessionInterface().open_session()
# 2) 响应视图
#    session -> LocalProxy -> 偏函数 -> LocalStack -> Local
# 3）请求终止
#    self.session_interface.save_session(self, request)
#    由于默认的app中session_interface=SecureCookieSessionInterface()
#       SecureCookieSessionInterface().save_session(self, request)
#    自定制session_interface=MySessionInterface()
#       MySessionInterface().save_session()

# flask_session组件
# 将flask的session存储在其他数据库如redis

from redis import Redis
from flask import Flask, session
from flask_session import RedisSessionInterface

app = Flask(__name__)
app.secret_key = 'sdfdfsdfsdf'


conn = Redis(host='172.16.1.141', port='6379', password='myredis')
app.session_interface = RedisSessionInterface(conn, key_prefix='__flask_')


@app.route('/', methods=['GET'])
def index():
    session['xxx'] = 123
    return 'Hello...'

if __name__ == '__main__':
    app.run(port=5001)