import keyboard
yes_no = keyboard.create_keyboard(buttons={'0': 'Нет', '1': 'Да'}, num_buttons_per_row=2)
gender_selector = keyboard.create_keyboard(buttons={'0': 'Женский', '1': 'Мужской'}, num_buttons_per_row=2)
range_selector = keyboard.create_keyboard(buttons={'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10'}, num_buttons_per_row=3)

temperature_selector = keyboard.create_keyboard(buttons={'0': '36-36,4', '1': '36,4-36,8', '2': '36,8-37,2', '3': '37,2-37,6', '5': '37,6-38', '5': '38-38,4', '6': '38,4-38,8', '7': '38,8-39,2', '9': '39,2-39,6', '9': '39,6-40', '10': '40 и выше'}, num_buttons_per_row=3)

additional_factors = keyboard.create_keyboard(buttons={'1': 'Были за границей', '2': 'Контактировали с заболевшим', '0': 'Ничего из выше перечисленного'}, num_buttons_per_row=1)
cough_scale = keyboard.create_keyboard(buttons={'0': 'отсутствие кашля', '1': 'единичные случаи кашля', '2': 'редкий кашель в течение дня', '3': 'частый кашель, не влияющий на активность', '4': 'частый кашель, снижающий активность', '5': 'тяжелый кашель, невозможность вести обычную активность'}, num_buttons_per_row=1)
pain_scale = keyboard.create_keyboard(buttons={'0': 'отсутствие боли', '1': 'слабая боль', '2': 'умеренная боль', '3': 'сильная боль', '4': 'очень сильная боль', '5': 'нетерпимая боль'}, num_buttons_per_row=1)
shortness_of_breath_scale = keyboard.create_keyboard(buttons={'0': 'одышка не беспокоит', '1': 'одышка появляется при подъеме или быстрой ходьбе', '2': 'одышка вынуждает ходить медленнее', '3': 'одышка вынуждает делать частые остановки', '4': 'невозможность покинуть дом из-за одышки'}, num_buttons_per_row=1)


