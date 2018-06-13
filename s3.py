from flask import Flask, redirect, request, flash, get_flashed_messages

# FLASK 闪现功能

app = Flask(__name__)
app.secret_key = 'sdfsdf'


@app.route('/index', methods=['GET', 'POST'])
def index():
    val = request.args.get('v')
    if val == 'admin':
        return 'Hello World...'
    flash('time out')
    return redirect('/error')


@app.route('/error', methods=['GET', 'POST'])
def error():
    data = get_flashed_messages()
    msg = data[0]
    return "错误信息: %s" % msg


if __name__ == '__main__':
    app.run()