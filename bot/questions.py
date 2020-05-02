import question
questions = []

questions.append(question.Question('Ваше полное имя? (Напишите сообщением ваше полное имя)', 'full_name', 'text'))
questions.append(question.Question('Наблюдаете ли вы у себя следующие симптомы: повышенная температура, недомогание, слабость, боль в костях? (Ответте да, если хотя бы 1 из симптомов у вас есть)', 'fever', 'bool'))
questions.append(question.Question('Есть ли у вас кашель?', 'cough', 'bool'))
questions.append(question.Question('Беспокоит ли вас отдышка?', 'shortness_of_breath', 'bool'))
questions.append(question.Question('Есть ли у вас головная боль?', 'head_ache', 'bool'))
questions.append(question.Question('Болит ли у вас горло?', 'sore_throat', 'bool'))
questions.append(question.Question('Ваш возраст - 60 или старше?', 'age_60_and_above', 'bool'))
questions.append(question.Question('Ваш пол мужской?', 'gender', 'bool'))


#  function get_bool_value converts words to boolean values. For example, yes or YES or Yes will be converted to 1 or True
def get_bool_value(answer):
	answer = answer.lower()
	if answer == 'yes' or answer == 'да':
		return 1
	if answer == 'no' or answer == 'нет':
		return 0
	return -1

