from bottle import Bottle

app = application = Bottle()

@app.error(404)
def error404(error):
    return '<img src="/static/images/nothing.jpg" />'