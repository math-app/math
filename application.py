from bottle import Bottle, route, run, template

app = application = Bottle()

@app.route('/')
@app.route('/hello/<name>')
def hello(name = 'Stranger'):
    return template('index', name=name)

@app.error(404)
def error404(error):
    return '<img src="/static/images/nothing.jpg" />'

if __name__ == '__main__':
    run(host='localhost', port=8080)
