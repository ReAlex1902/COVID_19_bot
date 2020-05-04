"""Copyright 2020 Alex Malkhasov, Nikita Vronski, Vadim Kholodilo
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import keyboards
from question import Question
questions = []

questions.append(Question('Напишите ваше полное имя?', 'full_name', 'text'))
questions.append(Question('Какая у вас температура?', 'fever', 'bool', keyboards.temperature_selector))
questions.append(Question('Оцените ваш кашель', 'cough', 'bool', keyboards.cough_scale))
questions.append(Question('Оцените ваш уровень одышки', 'shortness_of_breath', 'bool', keyboards.shortness_of_breath_scale))
questions.append(Question('Насколько сильно у вас болит голова?', 'head_ache', 'bool', keyboards.pain_scale))
questions.append(Question('Насколько сильно у вас болит горло?', 'sore_throat', 'bool', keyboards.pain_scale))
questions.append(Question('Укажите ваш возраст', 'age', 'text'))
questions.append(Question('Какой ваш пол?', 'gender', 'bool', keyboards.gender_selector))
questions.append(Question('Выберите одно утверждение из списка ниже, которое относится к вам', 'additional_factor', 'bool', keyboards.additional_factors))


#  function get_bool_value converts words to boolean values. For example, yes or YES or Yes will be converted to 1 or True
def get_bool_value(answer):
	answer = answer.lower()
	if answer == 'yes' or answer == 'да':
		return 1
	if answer == 'no' or answer == 'нет':
		return 0
	return -1
