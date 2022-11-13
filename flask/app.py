from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

def create_app(): 
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'dev'
	toolbar = DebugToolbarExtension(app)
	
	@app.route("/")	
	def hello():
		return "Hi!"

	return app