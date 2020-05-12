from api import api_bp
from flask import Flask
app = Flask(__name__)
def main():
	app.config['DEBUG'] = True
	app.register_blueprint(api_bp) # contains all API methods
	app.run()

if __name__ == '__main__':
	main()
