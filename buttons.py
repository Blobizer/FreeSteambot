from aiogram.types import ReplyKeyboardMarkup




sub = ReplyKeyboardMarkup(resize_keyboard=True).add("Подписаться")

unsub = ReplyKeyboardMarkup(resize_keyboard=True).add("❌Отписаться")

cancel = ReplyKeyboardMarkup(resize_keyboard =True).add("Отмена")

#admin-buttons

main_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).insert("Начать рассылку юзерам.").insert("Статистика")


