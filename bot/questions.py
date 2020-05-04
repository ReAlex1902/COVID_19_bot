import keyboards
import question
questions = []

questions.append(question.Question('Напишите ваше полное имя?', 'full_name', 'text'))
questions.append(question.Question('Какая у вас температура?', 'fever', 'bool', keyboards.temperature_selector))
questions.append(question.Question('Оцените ваш кашель', 'cough', 'bool', keyboards.cough_scale))
questions.append(question.Question('Оцените ваш уровень одышки', 'shortness_of_breath', 'bool', keyboards.shortness_of_breath_scale))
questions.append(question.Question('Насколько сильно у вас болит голова?', 'head_ache', 'bool', keyboards.pain_scale))
questions.append(question.Question('Насколько сильно у вас болит горло?', 'sore_throat', 'bool', keyboards.pain_scale))
questions.append(question.Question('Укажите ваш возраст', 'age', 'text'))
questions.append(question.Question('Какой ваш пол?', 'gender', 'bool', keyboards.gender_selector))
questions.append(question.Question('Выберите одно утверждение из списка ниже, которое относится к вам', 'additional_factor', 'bool', keyboards.additional_factors))


#  function get_bool_value converts words to boolean values. For example, yes or YES or Yes will be converted to 1 or True
def get_bool_value(answer):
	answer = answer.lower()
	if answer == 'yes' or answer == 'да':
		return 1
	if answer == 'no' or answer == 'нет':
		return 0
	return -1
