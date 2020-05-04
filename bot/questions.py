import keyboards
import question
questions = []

questions.append(question.Question('Напишите ваше полное имя?', 'full_name', 'text'))
questions.append(question.Question('Какая у вас температура?', 'fever', 'bool', keyboards.temperature_selector))
questions.append(question.Question('Есть ли у вас кашель? (0 - кашля нет, 10 - сильный кашель)', 'cough', 'bool', keyboards.range_selector))
questions.append(question.Question('Беспокоит ли вас отдышка? (0 - нет, 10 - очень сильная)', 'shortness_of_breath', 'bool', keyboards.range_selector))
questions.append(question.Question('Есть ли у вас головная боль?(0 - нет совсем, 10 - очень сильная)', 'head_ache', 'bool', keyboards.range_selector))
questions.append(question.Question('Болит ли у вас горло? (0 - не болит совсем, 10 - сильная боль)', 'sore_throat', 'bool', keyboards.range_selector))
questions.append(question.Question('Укажите ваш возраст', 'age', 'text'))
questions.append(question.Question('Какой ваш пол?', 'gender', 'bool', keyboards.gender_selector))


#  function get_bool_value converts words to boolean values. For example, yes or YES or Yes will be converted to 1 or True
def get_bool_value(answer):
	answer = answer.lower()
	if answer == 'yes' or answer == 'да':
		return 1
	if answer == 'no' or answer == 'нет':
		return 0
	return -1
