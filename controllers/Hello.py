from bottle import template

class HelloController():

	def index(name):
		return template('index', name=name)