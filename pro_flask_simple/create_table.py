# !/usr/bin/env python
# -*- coding:utf-8 -*-

from pro_flask_simple.pro_flask import db
from pro_flask_simple.pro_flask import app

with app.app_context():
    db.create_all()

