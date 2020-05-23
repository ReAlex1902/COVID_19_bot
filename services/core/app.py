import os
import pickle
from views import api_bp
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
def main():
	# Checking environment variables
# If all of them are set, they are added to the app.config  object
	if os.environ.get('MYSQL_HOST') == None:
		print('ERROR: MYSQL_HOST environment variable is not set')
		exit()
	else:
		app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
	if os.environ.get('MYSQL_USER') == None:
		print('ERROR: MYSQL_USER environment variable is not set')
		exit()
	else:
		app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
	if os.environ.get('MYSQL_PASSWORD') == None:
		print('ERROR: MYSQL_PASSWORD environment variable is not set')
		exit()
	else:
		app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
	if os.environ.get('MYSQL_DB') == None:
		print('ERROR: MYSQL_DB environment variable is not set')
		exit()
	else:
		app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
	app.config['MYSQL_CURSORCLASS'] = 'DictClass'
	try:
		app.mysql = MySQL(app)
	except Error as e:
		print('ERROR: unable to connect to the database: ', e)

	# Loading the random forest algorithm
# It will be loaded only once in order to increase performance
	rf = pickle.load(open('Random_Forest.sav', 'rb'))
	app.rf = rf
	app.register_blueprint(api_bp) # contains all API methods
	app.run()

if __name__ == '__main__':
	main()
