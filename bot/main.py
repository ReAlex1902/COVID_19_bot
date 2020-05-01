import questions # A module which holds all questions. Then they will be moved to a database
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, DictPersistence
# Configuration then it will be added to another file
myToken = "1250452288:AAF96rdBNqy9MPM_DO-k_foif_ZicW9yEls"



# Handlers
def start(update, context): # handles /start command which is sent automaticly when you write to the bot
	print('Start callback has been called')
	#print('Saved user data', context.user_data)
	#print('Update object: ', update)
	update.message.reply_text('Добро пожаловать в COVID19VirusHackBot. Данный бот задаст вам несколько вопросов, которые помогут оценить врачам болете ли вы Коронавирусом или нет. Также, когда вы закончите отвечать на вопросы, то бот вычислит вероятность того, а есть ли у вас вирус. Пожалуйста, отвечайте на вопросы честно. Для работы с ботом, вы можете использовать следующие команды: /test - начать тестирование, /help - справка по боту. Берегите себя.')

def test(update, context):
	update.message.reply_text('Тестирование начато.')
	context.user_data['is_testing'] = True
	context.user_data['question_index'] = 0
	update.message.reply_text(questions.questions[0].question_text)

def echo(update, context):
	print('Echo callback has been called')
	print('user data: ', context.user_data)
	if 'is_testing' in context.user_data:
		print('testing')
		question_index = context.user_data['question_index']
		context.user_data[questions.questions[question_index].internal_name] = update.message.text
		question_index = question_index + 1
		context.user_data['question_index'] = question_index
		if question_index <= len(questions.questions) - 1:
			update.message.reply_text(questions.questions[question_index].question_text)
		else:
			update.message.reply_text('Тестирование закончено')
	else:
		print('not testing')
		update.message.reply_text('Напичатайте /test, что бы начать тестирование')


# Bot inicialization
def main():
	import json
	my_persistence = DictPersistence()
	updater = Updater(token=myToken, persistence=my_persistence , use_context=True)
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
