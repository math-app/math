from configuration import app

"""
Decorator to apply route on class method
The default decoretor from bottle doesnt work with method
"""
def route(path, method="GET"):
    def decorator(func):
        app.route(path, method, func)
        return func
    return decorator