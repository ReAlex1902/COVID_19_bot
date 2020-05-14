from flask import Blueprint, request
api_bp = Blueprint('api_bp', __name__, url_prefix='/api')



@api_bp.route('/predict/<id>', methods=['GET', 'POST'])
def predict(id):
	""" is called when you access the URL /api/predict
	parameters:
	id - id of a patient for whom the prediction is needed
	if the id is not specifide, you have to  provide JSON string with all data
	For more information see api.md """

	if request.method == 'GET':
		return '99'
	if request.method == 'POST':
		data = request.form['data']
		return data
	return 'Method is not allowed'

