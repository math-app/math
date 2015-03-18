from bottle import run
from router.math import Router
from configuration import app, application

mathApp = Router()

if __name__ == '__main__':
    run(host='localhost', port=8080)
