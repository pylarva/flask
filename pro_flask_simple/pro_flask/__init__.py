#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import *

from .views.account import account
from .views.blog import blog
from .views.user import user

app = Flask(__name__, template_folder='templates', static_folder='statics', static_url_path='/static')
app.config.from_object('settings.DevelopmentConfig')

# 将db注册到App中
db.init_app(app)

app.register_blueprint(account)
app.register_blueprint(blog)
app.register_blueprint(user)
