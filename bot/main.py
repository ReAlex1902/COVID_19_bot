from model import *
import questions # A module which holds all questions. Then they will be moved to a database
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, DictPersistence
import config
# helpers
# function create_list creates list putting all data from the dictionary in the right order. Then this list is sent to the model
def create_data_list(dic):
	lst = []
	lst.append(dic['cough'])
	lst.append(dic['fever'])
	lst.append(dic['sore_throat'])
	lst.append(dic['shortness_of_breath'])
	lst.append(dic['head_ache'])
	lst.append(dic['age_60_and_above'])
	lst.append(dic['gender'])
	lst.append(0) # I hav no clue what the last parameter is. When I figure it out. I'll add it to the questions. For now it's just zero
	return lst

def create_report(prediction, answers):
	if prediction == 1:
		return 'Болен.'
	else:
		return 'Здоров.'

# Handlers
def start(update, context): # handles /start command which is sent automaticly when you write to the bot
	print('Start callback has been called')
	#print('Saved user data', context.user_data)
	#print('Update object: ', update)
	update.message.reply_text('Добро пожаловать в COVID19VirusHackBot. Данный бот задаст вам несколько вопросов, которые помогут оценить врачам болете ли вы Коронавирусом или нет. Также, когда вы закончите отвечать на вопросы, то бот вычислит вероятность того, а есть ли у вас вирус. Пожалуйста, отвечайте на вопросы честно. Для работы с ботом, вы можете использовать следующие команды: /test - начать тестирование, /help - справка по боту. Берегите себя.')

def test(update, context):
	update.message.reply_text('Тестирование начато.')
	update.message.reply_text('На вопросы ниже отвечайте да или нет. Если явно не сказано другое. Регистр ответов не важен')
	context.user_data['is_testing'] = True
	context.user_data['question_index'] = 0
	context.user_data['answers'] = {}
	update.message.reply_text(questions.questions[0].question_text)

def echo(update, context):
	print('Echo callback has been called')
	print('user data: ', context.user_data)
	if 'is_testing' in context.user_data and context.user_data['is_testing'] == True:
		print('testing')
		question_index = context.user_data['question_index']
		answer = update.message.text
		if questions.questions[question_index].answer_type == 'bool':
			answer = questions.get_bool_value(answer)
			if answer == -1:
				update.message.reply_text('Неверное значение. Напишите да или нет')
				return
		context.user_data['answers'][questions.questions[question_index].internal_name] = answer
		question_index = question_index + 1
		context.user_data['question_index'] = question_index
		if question_index <= len(questions.questions) - 1:
			update.message.reply_text(questions.questions[question_index].question_text)
		else:
			update.message.reply_text('Тестирование закончено')
			context.user_data['is_testing'] = False
			lst = create_data_list(context.user_data['answers'])
			load_model = get_model()
			result = load_model(lst)
			report = create_report(result[0][0], {})
			print('prediction', result[0][0])
			update.message.reply_text(report)
	else:
		print('not testing')
		update.message.reply_text('Напичатайте /test, что бы начать тестирование')

# Bot inicialization
def main():
	my_persistence = DictPersistence()
	updater = Updater(token=config.token, persistence=my_persistence , use_context=True)
	disp = updater.dispatcher
	start_handler = CommandHandler('start', start)
	disp.add_handler(start_handler)
	echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
	disp.add_handler(echo_handler)
	test_handler = CommandHandler('test', test)
	disp.add_handler(test_handler)
	updater.start_polling()
	updater.idle()

main()
