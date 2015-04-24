from bottle import template
from configuration import app

class Router():

	@app.route('/')
	def index():
		from controllers.Home import HomeController
		return HomeController.index()

	@app.route('/hello')
	@app.route('/hello/<name>')
	def hello(name='Stranger'):
		from controllers.Hello import HelloController
		return HelloController.index(name)