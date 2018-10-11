import flask
from flask import Flask

flask_2 = Flask(__name__)

@flask_2.route('/')
def index():
	return 'this flask 2 web index~!'