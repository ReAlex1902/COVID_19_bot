import pickle
from views import api_bp
from flask import Flask
app = Flask(__name__)
def main():
	# Loading the random forest algorithm
# It will be loaded only once in order to increase performance
	rf = pickle.load(open('Random_Forest.sav', 'rb'))
	app.rf = rf
	app.register_blueprint(api_bp) # contains all API methods
	app.run()

if __name__ == '__main__':
	main()
