from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)

# 导入配置文件
app.config.from_object('setting.DevelopmentConfig')

USER_LIST = {
    1: {'name': 'admin', 'pwd': 'pwd123', 'info': 'WARNING: Do not use the development a production environment.'},
    2: {'name': 'user01', 'pwd': 'user123', 'info': 'WARNING: environment.'}
}


# 页面传参
@app.route('/detail/<int:nid>', methods=['GET'])
def detail(nid):
    info = USER_LIST.get(nid)
    return render_template('detail.html', info=info)


# session && URL别名
@app.route('/index', methods=['GET'])
def index():
    user = session.get('user_info')
    if not user:
        url = url_for('l1')
        return redirect(url)
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
            return redirect('index.html')
        return render_template('login.html', error='user or password error...')


if __name__ == '__main__':
    app.run()
