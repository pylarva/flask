import functools
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)

# Hook函数

USER_LIST = {
    1: {'name': 'admin', 'pwd': 'pwd123', 'info': 'WARNING: Do not use the development a production environment.'},
    2: {'name': 'user01', 'pwd': 'user123', 'info': 'WARNING: environment.'}
}


# 登陆验证功能 类似于Django的中间件
@app.before_request
def process_request(*args, **kwargs):
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login')
    return None


@app.after_request
def process_response(response):
    return response


@app.route('/index', methods=['GET'], endpoint='l2')
def index():
    if request.method == 'GET':
        return render_template('index.html', user=USER_LIST)


# 定制错误信息
@app.errorhandler(404)
def err_404(*arg):
    return '404错误了...'


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


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
