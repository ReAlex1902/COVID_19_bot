import requests
import json
dic = {}
dic['cough'] = 2
dic['fever'] = 3
dic['sore_throat'] = 0
dic['shortness_of_breath'] = 4
dic['head_ache'] = 0
dic['age'] = 25
dic['gender'] = 1
dic['additional_factor'] = 1

URL = 'http://localhost:5000/api/predict?token=123'
result = requests.post(url=URL, data=json.dumps(dic))


