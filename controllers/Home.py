from bottle import template

class HomeController():

	def index():
		return template('index', name="to hame")