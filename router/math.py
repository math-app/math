from bottle import template
from common.decorator import route


class Router():

    @route('/')
    def index():
        return template('index', name="to home")

    @route('/hello/<name>')
    def hello(name='Stranger'):
        return template('index', name=name)