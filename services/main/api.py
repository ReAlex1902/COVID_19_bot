from flask import Blueprint
api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/', methods=['GET'])
def home():
	return '<h1> test application </h1>'

@api_bp.route('/predict', methods=['GET'])
def predict():
	return 'prediction ok'
