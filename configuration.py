from bottle import Bottle, template

app = application = Bottle()

@app.error(404)
def error404(error):
    return template("error404")