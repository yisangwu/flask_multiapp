import flask
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask version is:%s' % flask.__version__

@app.route('/show_list')	
def display_list():
	x_list = []
	for _ in range(10):
		x_list.append('#')
	return str(x_list)
	
@app.route('/show_int/<int:id>')
def display_int(id):
	return 'show int is:%u' % id

@app.route('/show_path/<path:spath>')
def display_path(spath):
	return 'show path is:%s' % path

	
@app.route('/user/<username>')
def search(username):
	return 'search name is:%s' % username
	

@app.route('/test/<int:type>')
def for_test(type):
	if type == 1:
		return url_for('index')
	elif type == 2:
		return url_for('display_list')
	elif type == 3:
		return url_for('display_int', id=123456)
	elif type == 4:
		return url_for('display_path', spath='/a/b/c/d/e/f')
	elif type == 5:
		return url_for('search', username='hello world')
	else:
		return 'wrong type!~~'

	
if __name__ == '__main__':
	app.run(
		host='0.0.0.0',
		port=8577,
		debug=True
	)
	