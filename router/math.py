from bottle import template
from configuration import app


class Router():

    @app.route('/')
    def index():
        return template('index', name="to home")

    @app.route('/hello/<name>')
    def hello(name='Stranger'):
        return template('index', name=name)