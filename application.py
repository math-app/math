from bottle import Bottle, route, run, template

app = application = Bottle()

@app.route('/')
def hello():
    return template('<b>Index {{teste}}</b>!', teste="page")

@app.route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
    run(host='localhost', port=8080)
