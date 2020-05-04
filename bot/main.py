import pickle
import questions # A module which holds all questions. Then they will be moved to a database
import keyboards
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
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
	lst.append(int(dic['age']))
	lst.append(dic['gender'])
	lst.append(dic['additional_factor'])
	return lst

def create_report(prediction, answers):
	report = 'Вы больны с вероятностью '
	report += str(prediction)
	report += '%'
	if prediction > 30:
		report += '\n\n Рекомендация: \n \
		Вероятность того, что вы инфецированы слишком высока. Что делать: \n \
		1. Сохранять спокойствие. 100% гарантии вам может дать только тест. \n \
		2. Ждать звонка от врача. Втечении 24 часов с вами свяжется врач. \n \
		3. Исключить любые контакты с родственниками и людьми вокруг.'
	return report

# Handlers
def start(update, context): # handles /start command which is sent automaticly when you write to the bot
	print('Start callback has been called')
	#print('Saved user data', context.user_data)
	#print('Update object: ', update)
	update.message.reply_text('Добро пожаловать в COVID-19 diagnostic bot. \n\n \
	Данный бот задаст вам несколько вопросов, которые помогут оценить врачам оценить ваше состояние Коронавирусом. \
	Также, когда вы закончите вводить свои данные, бот вычислит вероятность заболевания. \n\n \
	Пожалуйста, отвечайте на вопросы честно. \n\n \
	Для работы с ботом, вы можете использовать следующие команды: \n \
	/test - начать тестирование, \n \
	/help - справка по боту. \n\n \
	Берегите себя.')

def test(update, context): # handles /test command
	update.message.reply_text('Тестирование начато.')
	update.message.reply_text('На вопросы ниже отвечайте по шкале от 0 до 10, если явно не сказано другое.')
	context.user_data['is_testing'] = True
	context.user_data['question_index'] = 0
	context.user_data['answers'] = {}
	msg = update.message.reply_text(questions.questions[0].question_text)
	chat_id = msg.chat_id
	message_id = msg.message_id
	context.chat_data['message_id'] = message_id
	context.chat_data['chat_id'] = chat_id

def echo(update, context): # Handles all messages and buttons
	print('Echo callback has been called')
	if 'is_testing' in context.user_data and context.user_data['is_testing'] == True:
		message = update.message
		answer = None
		if update.callback_query != None:
			update.callback_query.answer()
			answer = int(update.callback_query.data)
			message = update.callback_query.message
		else:
			answer = update.message.text
			context.chat_data['message_id'] = -1
			context.chat_data['chat_id'] = -1
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
				keyboard = questions.questions[question_index].keyboard
				reply_markup = InlineKeyboardMarkup(keyboard)
				if context.chat_data['message_id'] != -1 and context.chat_data['chat_id'] != -1:
					context.bot.edit_message_text(chat_id=context.chat_data['chat_id'], message_id=context.chat_data['message_id'], text=questions.questions[question_index].question_text, reply_markup=reply_markup)
				else:
					msg = message.reply_text(questions.questions[question_index].question_text, reply_markup=reply_markup)
					context.chat_data['chat_id'] = msg.chat_id
					context.chat_data['message_id'] = msg.message_id
			else:
				context.bot.edit_message_text(chat_id=context.chat_data['chat_id'], message_id=context.chat_data['message_id'], text=questions.questions[question_index].question_text)
		else:
			context.bot.edit_message_text(chat_id=context.chat_data['chat_id'], message_id=context.chat_data['message_id'], text='Тестирование завершено')
			context.user_data['is_testing'] = False
			lst = create_data_list(context.user_data['answers'])
			print([lst])
			rf = pickle.load(open('Random_Forest.sav', 'rb'))
			result = rf.predict_proba([lst])
			prediction = round(result[0][1].item() * 100, 2)
			report = create_report(prediction, {})
			print('prediction', result[0][1].item())
			context.bot.edit_message_text(chat_id=context.chat_data['chat_id'], message_id=context.chat_data['message_id'], text=report)
	else:
		update.message.reply_text('Напечатайте /test, что бы начать тестирование')

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

if __name__ == '__main__':
	main()
