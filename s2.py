from flask import Flask, views
app = Flask(__name__)

# FLASK CBV架构


def auth(func):
    def inner(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result
    return inner


class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [auth, ]

    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index.POST'


app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint


if __name__ == '__main__':
    app.run()
