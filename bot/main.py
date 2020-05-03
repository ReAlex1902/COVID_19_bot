from model import *
import questions # A module which holds all questions. Then they will be moved to a database
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, DictPersistence, CallbackQueryHandler
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
	report = 'Вы больны с вероятностью '
	report += str(prediction)
	report += '%'
	return report

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
	id = update.message.reply_text(questions.questions[0].question_text)
	print('bot message id is ', id.message_id)

def echo(update, context):
	print('Echo callback has been called')
	if 'is_testing' in context.user_data and context.user_data['is_testing'] == True:
		message = update.message
		answer = None
		if update.callback_query != None:
			update.callback_query.answer(text='Ответ принят', show_alrt=True)
			answer = int(update.callback_query.data)
			message = update.callback_query.message
		else:
			answer = update.message.text
		question_index = context.user_data['question_index']
		if questions.questions[question_index].answer_type == 'bool':
			#answer = questions.get_bool_value(answer)
			if answer == -1:
				message.reply_text('Неверное значение. Напишите да или нет')
				return
		context.user_data['answers'][questions.questions[question_index].internal_name] = answer
		question_index = question_index + 1
		context.user_data['question_index'] = question_index
		if question_index <= len(questions.questions) - 1:
			if questions.questions[question_index].answer_type == 'bool':
				keyboard = [[InlineKeyboardButton("Да", callback_data=1), InlineKeyboardButton("Нет", callback_data=0)]]
				reply_markup = InlineKeyboardMarkup(keyboard)
				message.edit_text(questions.questions[question_index].question_text, reply_markup=reply_markup)
			else:
				message.edit_text(questions.questions[question_index].question_text)
		else:
			message.edit_text('Тестирование закончено')
			context.user_data['is_testing'] = False
			lst = create_data_list(context.user_data['answers'])
			load_model = get_model()
			result = load_model(lst)
			prediction = round(result[0][1].item() * 100, 2)
			report = create_report(prediction, {})
			print('prediction', result[0][1].item())
			message.edit_text(report)
	else:
		update.message.reply_text('Напичатайте /test, что бы начать тестирование')

def error(update, context):
	print('error: ', context.error)

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
	disp.add_error_handler(error)
	callback_query_handler = CallbackQueryHandler(echo)
	disp.add_handler(callback_query_handler)
	updater.start_polling()
	updater.idle()

main()
