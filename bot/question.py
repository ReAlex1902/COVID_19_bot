"""Copyright 2020 Alex Malkhasov, Nikita Vronski, Vadim Kholodilo
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

class Question:
	""" If you want to add questions. You have to create an instance of this class for each question. See an example in questions.py
	methods
	---------
	__init__ - constructor
	"""

	def __init__(self, question_text, internal_name, answer_type, keyboard = None):
		""" constructor
		parameters
---------
self : object : instance of this class,
		question_text : str : text of your question,
		internal_name : str : this name is used to add a question to answers dictionary,
		answer_type : str : type of your question's answer can be int (number), choice (keyboard will be attached), text (a regular string),
		keyboard : telegram.InlineKeyboardButton : if you want to attach a keyboard to your question, pick one from keyboards.py or create it on your own
		"""
		self.question_text = question_text
		self.internal_name = internal_name
		self.answer_type = answer_type
		self.keyboard = keyboard
