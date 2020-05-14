# helpers
def create_data_list(dic):
	""" This function creates a list from a data dictionary where all user data is stored """
	lst = []
	lst.append(dic['cough'])
	lst.append(dic['fever'])
	lst.append(dic['sore_throat'])
	lst.append(dic['shortness_of_breath'])
	lst.append(dic['head_ache'])
	lst.append(int(dic['age']))
	lst.append(dic['gender'])
	lst.append(dic['additional_factor'])
	return lst

