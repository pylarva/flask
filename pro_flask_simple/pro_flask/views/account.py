#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, template_rendered, request_started
from flask import request
from ..db_helper import SQLHelper
from flask.signals import _signals

account = Blueprint('account', __name__)


# 信号
def print_template_rendered(sender, template, context, **extra):
    print(sender)
    print('Using template: %s with context: %s' % (template.name, context))
    print(request.url)


def print_request_started(sender, **extra):
    print('Request request_started start..')
    print(request.url)


# 注册信号
# template_rendered.connect(print_template_rendered)
# request_started.connect(print_request_started)


@account.route('/login.html', methods=['GET', "POST"])
def login():
    # obj = SQLHelper()
    # result = obj.fetch_all('select * from mysql.user', [])
    # for item in result:
    #     print(item)
    return render_template('login.html')
