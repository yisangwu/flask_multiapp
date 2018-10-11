import flask
from flask import Flask

flask_1 = Flask(__name__)


@flask_1.route('/')
def index():
	return 'this is flask 1 web index~!'

