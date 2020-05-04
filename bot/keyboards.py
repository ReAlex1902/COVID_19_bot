import keyboard
yes_no = keyboard.create_keyboard(buttons={'0': 'Нет', '1': 'Да'}, num_buttons_per_row=2)
gender_selector = keyboard.create_keyboard(buttons={'0': 'Женский', '1': 'Мужской'}, num_buttons_per_row=2)
range_selector = keyboard.create_keyboard(buttons={'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10'}, num_buttons_per_row=3)

temperature_selector = keyboard.create_keyboard(buttons={'0': '36-36,4', '1': '36,4-36,8', '2': '36,8-37,2', '3': '37,2-37,6', '5': '37,6-38', '5': '38-38,4', '6': '38,4-38,8', '7': '38,8-39,2', '9': '39,2-39,6', '9': '39,6-40', '10': '40 и выше'}, num_buttons_per_row=3)

additional_factors = keyboard.create_keyboard(buttons={'1': 'Были за границей', '2': 'Контактировали с заболевшим', '0': 'Ничего из выше перечисленного'}, num_buttons_per_row=1)

