import utils
from flask import Blueprint, request, current_app as app
api_bp = Blueprint('api_bp', __name__, url_prefix='/api')



@api_bp.route('/predict', methods=['GET', 'POST'])
def predict():
	""" This function is called when you send POST request to /api/predict """
	if request.method == 'POST':
		request.get_json(force=True)
		data= request.json
		print('Received data: ', data)
		cur = app.mysql.connection.cursor()
		
		cur.close()
		data_list = utils.create_data_list(data)
		prediction = app.rf.predict_proba([data_list])[0][1].item()
		response = {}
		response['status_code'] = 200
		response['data'] = {}
		response['data']['prediction'] = prediction
		return response, 200

