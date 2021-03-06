import functools
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)

# 导入配置文件
app.config.from_object('setting.DevelopmentConfig')

USER_LIST = {
    1: {'name': 'admin', 'pwd': 'pwd123', 'info': 'WARNING: Do not use the development a production environment.'},
    2: {'name': 'user01', 'pwd': 'user123', 'info': 'WARNING: environment.'}
}


# 登陆验证
def wapper(func):
    # 帮助我们保存原函数的元信息 保存原函数的函数名等
    @functools.wraps(func)
    def inner(*args, **kwargs):
        user = session.get('user_info')
        if not user:
            return redirect('/login')
        return func(*args, **kwargs)
    return inner


# 页面传参
# 添加验证装饰器 1、必须添加到第一层 2、路由必须制定不同的endpoint
@app.route('/detail/<int:nid>', methods=['GET'], endpoint='l3')
@wapper
def detail(nid):
    info = USER_LIST.get(nid)
    return render_template('detail.html', info=info)


# session && URL别名
@app.route('/index', methods=['GET'], endpoint='l2')
@wapper
def index():
    # user = session.get('user_info')
    # if not user:
    #     url = url_for('l1')
    #     return redirect(url)
    if request.method == 'GET':
        return render_template('index.html', user=USER_LIST)


@app.route('/login', methods=['GET', 'POST'], endpoint='l1')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'admin' and pwd == 'admin':
            session['user_info'] = user
            return redirect('/index')
        return render_template('login.html', error='user or password error...')


@app.route('/macro', methods=['GET'])
def macro():
    return render_template('macro.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
