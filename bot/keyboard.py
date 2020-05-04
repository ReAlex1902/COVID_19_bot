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


