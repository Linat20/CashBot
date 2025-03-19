from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню бота
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='📱 Мой кабинет')],
                                     [KeyboardButton(text='💸 Заработать')],
                                     [KeyboardButton(text='🆘 О боте | Помощь')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='Выберите пункт меню...')


# Кнопка <Вывести средства> в личном кабинете
withdraw = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вывести средства', callback_data='withdraw')]])


# Раздел "Заработать"
task = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🎁 Партнерские задания', callback_data='pz')],
                                     [InlineKeyboardButton(text='💬 Написание отзывов', callback_data='no')],
                                     [InlineKeyboardButton(text='👁 Просмотр рекламы', callback_data='pr'),
                                     InlineKeyboardButton(text='💼 Оффлайн работа', callback_data='or')]])


# Раздел "Оффлайн работа"
offline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Курьер в сервис Яндекс.Еда (+22 500 за 7 дней)', callback_data='task1')],
    [InlineKeyboardButton(text='✅ Курьер/Повар-кассир в Burger King (+8000 за 1 день)', callback_data='task2')],
    [InlineKeyboardButton(text='✅ Работа в Т-Банке (Ваша ЗП + бонус от бота +2500)', callback_data='task3')],
    [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
])


partnerprogram = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти на витрину', url='https://ppdu.ru/3be683a4-5370-49b2-a961-f47c14c0ef55')],
    [InlineKeyboardButton(text='Вознаграждения', callback_data='rewards')]])  





# Новая клавиатура для раздела "О боте | Помощь"
help_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Частые вопросы (FAQ)"), 
          KeyboardButton(text="Инструкции и руководства")],
        [KeyboardButton(text="Контактная информация")],
        [KeyboardButton(text="Политика конфиденциальности"),
         KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)