""" Copyright 2020 Alex Malkhasov, Nikita Vronski, Vadim Kholodilo
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, DictPersistence, CallbackQueryHandler
import pickle
from questions import questions # A module which holds all questions. Then they will be moved to a database
import keyboards # This module has a lot of prebuilt keyboards. It is also a good example for Keyboard.py class
import config # Bot's settings

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

def create_report(prediction, answers):
	""" This function creates the report for a user based on prediction from the model """
	report = 'Вы больны с вероятностью '
	report += str(prediction)
	report += '%'
	report += '\n\n Рекомендации: \n'
	if prediction > 30:
		report += 'Вероятность того, что вы инфецированы слишком высока. Что делать: \n\
		1. Сохранять спокойствие. 100% гарантии вам может дать только медицинский тест. \n\
		2. Ждать звонка от врача. Втечение 24 часов с вами свяжется врач. \n\
		3. Исключить, на сколько это возможно, любые контакты с родственниками и людьми вокруг.'
	else:
		report += 'Хоть бот и вычислил достаточно малую вероятность того, что вы заражены, но это не значит, что вы действительно полностью здоровы. Помните, что самым точным показателем того, что вы здоровы, является тест на Каронавирус'
	return report

# Handlers
def start(update, context):
	""" This function handles /start command """
	update.message.reply_text('Добро пожаловать в COVID-19 diagnostic bot. \n\n\
	Данный бот задаст вам несколько вопросов, которые помогут оценить врачам ваше состояние. \
	Также, когда вы закончите вводить свои данные, бот вычислит вероятность заболевания. \n\n\
	Пожалуйста, отвечайте на вопросы честно. \n\n\
	Для работы с ботом, вы можете использовать следующие команды: \n\
	/test - начать тестирование, \n\
	Берегите себя.')

def test(update, context): # handles /test command
	update.message.reply_text('Тестирование начато. \n\n \
	Внимание! Бот собирает конфеденциальную информацию: \
	имя, фамилию, номер мобильного телефона и адрес при необходимости \n \
	Данная информация собирается ботом в целях связи с вами и никогда не будет передана третьим лицам без вашего на то согласия \n \
	Продолжая пользоваться ботом, вы принимаете данные условия.')
	context.user_data['is_testing'] = True
	context.user_data['question_index'] = 0
	context.user_data['answers'] = {}
	msg = update.message.reply_text(questions[0].question_text)
	chat_id = msg.chat_id
	message_id = msg.message_id
	context.chat_data['message_id'] = message_id
	context.chat_data['chat_id'] = chat_id

def echo(update, context):
	""" Handles all messages and buttons """
	if 'is_testing' in context.user_data and context.user_data['is_testing'] == True:
		question_index = context.user_data['question_index']
		message = update.message
		answer = None
		if update.callback_query != None:
			update.callback_query.answer()
			answer = int(update.callback_query.data)
			message = update.callback_query.message
		else:
			answer = update.message.text
			if questions[question_index].answer_type == 'int':
				if not answer.isdigit():
					message.reply_text('Ответ должен быть напечатан одним числом')
					return
			context.chat_data['message_id'] = -1
			context.chat_data['chat_id'] = -1
		context.user_data['answers'][questions[question_index].internal_name] = answer
		question_index = question_index + 1
		context.user_data['question_index'] = question_index
		if question_index <= len(questions) - 1:
			if questions[question_index].answer_type == 'choice':
				keyboard = questions[question_index].keyboard
				reply_markup = InlineKeyboardMarkup(keyboard)
				if context.chat_data['message_id'] != -1 and context.chat_data['chat_id'] != -1:
					context.bot.edit_message_text(chat_id=context.chat_data['chat_id'], message_id=context.chat_data['message_id'], text=questions[question_index].question_text, reply_markup=reply_markup)
				else:
					msg = message.reply_text(questions[question_index].question_text, reply_markup=reply_markup)
					context.chat_data['chat_id'] = msg.chat_id
					context.chat_data['message_id'] = msg.message_id
			else:
				context.bot.edit_message_text(chat_id=context.chat_data['chat_id'], message_id=context.chat_data['message_id'], text=questions[question_index].question_text)
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
