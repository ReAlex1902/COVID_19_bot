"""Copyright 2020 Alex Malkhasov, Nikita Vronski, Vadim Kholodilo
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from telegram import InlineKeyboardButton

def create_keyboard(buttons, num_buttons_per_row):
	keyboard = []
	labels = list(buttons.values())
	values = list(buttons.keys())
	num_buttons = len(buttons)
	num_additional_buttons = num_buttons % num_buttons_per_row # If buttons are not distributed equally. E.G. When we have 11 buttons, but we want to have 3 buttons per row. We can put only 9 which is not what we want to see. To fix it, all buttons left will be placed on the last row.
	k = num_buttons - num_additional_buttons
	for i in range (0, k, num_buttons_per_row):
		row = []
		for j in range(num_buttons_per_row):
			row.append(InlineKeyboardButton(labels[i + j], callback_data=values[i + j]))
		keyboard.append(row)

	additional_row = []
	#k -= 1
	for i in range(num_additional_buttons):
		additional_row.append(InlineKeyboardButton(labels[k + i], callback_data=values[k + i]))
	keyboard.append(additional_row)

	return keyboard


