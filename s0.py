# !/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

r = redis.Redis(host='172.16.1.141', port='6379', password='myredis')
r.set('foo', 'Bar')
print(r.get('foo'))