import flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_1 import flask_1
from flask_2 import flask_2

dm = DispatcherMiddleware(
	flask_1,
	{'/two': flask_2}
)

if __name__ == '__main__':
	run_simple('127.0.0.1', 8577, dm)
