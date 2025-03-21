from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
import app.database.requests as rq
import pytz  # Импортируйте pytz
from datetime import datetime
from aiogram.types import FSInputFile
import os

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    user_name = message.from_user.first_name
    welcome_message = (f"🌟 <strong>Добро пожаловать в CashBot!</strong> 🌟\n\n"
                       f"Привет, {user_name}! Мы рады видеть вас среди наших пользователей!\n\n"
                       f"💰 <strong>CashBot</strong> — ваш надежный компаньон на пути к заработку онлайн. Здесь вы найдете:\n"
                       f"- 📋 Уникальные задания\n"
                       f"- 🎯 Партнерские программы\n"
                       f"- 🎁 Специальные предложения и бонусы\n"
                       f"- 🔍 Актуальные новости и советы по заработку\n\n"
                       f"🚀 <strong>Что делать дальше?</strong>\n"
                       f"- Ознакомьтесь с доступными заданиями, выбрав вариант 'Заработать'.\n"
                       f"- Узнайте о партнерских программах.\n"
                       f"- Проверьте раздел 'Мой кабинет', чтобы отслеживать свой прогресс!\n\n"
                       f"💬 Вступайте в наш чат, где вам всегда будут рады! <a href='https://t.me/+PVA49PzAQUQ3MjMy'>Присоединиться к чату</a>\n\n"
                       f"Мы всегда готовы помочь вам добиться успеха, так что не стесняйтесь задавать вопросы!\n\n"
                       f"✨ <strong>Начните зарабатывать прямо сейчас!</strong> ✨")
   
    await message.answer(welcome_message, reply_markup=kb.main, parse_mode='HTML')

@router.message(F.text == '💸 Заработать')
async def cmd_task(message: Message):
    # Приветственное сообщение для раздела "Заработать"
    welcome_task_message = (
        "💼 Добро пожаловать в раздел 'Заработать'!\n\n"
        "Здесь вы найдете различные задания, которые помогут вам начать зарабатывать деньги онлайн и оффлайн.\n"
        "Выбирайте подходящие задания и действуйте, чтобы увеличить свой доход. Успехов!"
    )
    
    await message.answer(welcome_task_message)  # Отправляем приветственное сообщение
    await message.answer('Выберите подходящее задание:',reply_markup=kb.task)


@router.callback_query(F.data == 'or')
async def off_work(callback: CallbackQuery):
    await callback.answer('Отличный выбор!')
    await callback.message.answer('Выберите предложения:', reply_markup=kb.offline_keyboard)


@router.callback_query(F.data == 'task1')
async def yandex(callback: CallbackQuery):
    await callback.answer('Отличный выбор!')
    # URL изображения
    photo_url = "https://i.postimg.cc/BZTdrqbw/220721-Y-eda-0578.png"
    # Текст инструкции с ссылкой
    text_instruction = (
        "🚀 **Партнер сервиса Яндекс Еда в поисках курьеров!** 🚀\n"
        "✨ Хочешь сам выбирать время и локации для доставок?\n\n"
        "💰 **Выплаты:**\n"
        "💵 Для велокурьеров до 3500 ₽ в день;\n"
        "🎯 Повышенный приоритет на заказах для велокурьеров;\n"
        "🚴‍♂️ Официальные партнеры сервиса, где вы можете арендовать транспорт;\n"
        "🎉 Различные акции и бонусы, которые помогут увеличить ваш доход!\n\n"
        "📱 Потребуется телефон на базе Android 7 и выше или iPhone с версией iOS от 13.\n\n"
        "🤝 Присоединяйся к партнеру сервиса Яндекс Еда!\n\n"
        "🔍 **Что предлагаем?**\n"
        "🕒 Гибкое расписание, которое вы выбираете сами;\n"
        "📍  Удобные локации в городе;\n"
        "🎓 Возможность совмещать с работой или учебой.\n\n"
        "🤑 Доходность вакансии: за 100 выполненных заказов вы получите ~17 500 руб. (На это уходит примерно 7 дней)\n"
        "💲  За регистрацию по нашей ссылке Вы дополнительно получите 5 000 руб. (Важно: вы должны зарегистрироваться впервые!)\n\n" \
        "❓  Если остались вопросы по вакансии, задайте вопрос менеджеру @CashBot\n\n"
        "🔗 [Нажмите здесь, чтобы оставить заявку](https://reg.eda.yandex.ru/?advertisement_campaign=forms_for_agents&user_invite_code=0a1e210f18ac4e12a91e6014c98c4a87&utm_content=blank)"
    )
  
    await callback.message.answer_photo(photo=photo_url, caption=text_instruction, parse_mode='Markdown')   


@router.callback_query(F.data == 'task2')
async def burger(callback: CallbackQuery):
    await callback.answer('Отличный выбор!')
    # URL изображения
    photo_url = "https://i.postimg.cc/VLFNbD8W/300x300.png"
    # Текст инструкции с ссылкой
    text_instruction = (
        "🍔 **Работа в «Бургер Кинг»!** 🍔\n\n"
        "🔥 **Вакансии:**\n"
        "📦 **КУРЬЕР:**\n"
        "- Возраст 18+\n"
        "- Водительские права категории B (или M, A)\n"
        "- Желание учиться и развиваться\n\n"
        
        "🥗 **ПОВАР-КАССИР:**\n"
        "- Знание русского языка\n"
        "- Возраст 18+\n"
        "- Опыт не обязателен\n\n"
        
        "💰 **Что мы предлагаем?**\n"
        "- Еженедельные выплаты и чаевые\n"
        "- Бесплатное питание\n"
        "- Гибкий график\n\n"
         "💌 **Не упусти свой шанс!**\n"
        "🤑 Доходность вакансии: за одну смену вы получите ~5000 руб. (В зависимости от города)\n"
        "💲  За регистрацию по нашей ссылке Вы дополнительно получите 3 000 руб. (Важно: вы должны зарегистрироваться впервые!)\n\n" \
        "❓  Если остались вопросы по вакансии, задайте вопрос менеджеру @CashBot\n\n"
        "🔗 [Нажмите здесь, чтобы оставить заявку](https://trk.ppdu.ru/click/TPjjlqqS?erid=2SDnjdu6ZqS)"
    )
  
    await callback.message.answer_photo(photo=photo_url, caption=text_instruction, parse_mode='Markdown')  


@router.callback_query(F.data == 'task3')
async def burger(callback: CallbackQuery):
    await callback.answer('Отличный выбор!')
    # URL изображения
    photo_url = "https://i.postimg.cc/4xQ4hD8B/09cfed52-ab14-4c01-9b26-2d010533ce37.png"
    # Текст инструкции с ссылкой
    text_instruction = (
        "🚀 *Вакансии Т-Банка*\n\n"
        "*Не нужно высшее образование или опыт!*\n"
        "📞 *Представители*\n"
        "📊 *Операторы колл-центра*\n"
        "💼 *Менеджеры по продаже услуг*\n"
        "📝 *Специалисты по документообороту*\n"
        "🤝 *Консультанты*\n"
        "💳 *Специалисты по взысканию*\n"
        "👥 *Рекрутеры*\n\n"
        "💡 *Преимущества*:\n"
        "- Гибкие графики и достойная зарплата.\n"
        "- Поддержка и обучение от наставников.\n"
        "- Перспективы карьерного роста.\n\n"
        "🛤️ *Путь кандидата*:\n"
        "- Перейдите по ссылке ниже.\n"
        "- Выберите город и вакансию.\n"
        "- Заполните данные и пройдите обучение.\n\n"
        "💼 *Сделайте шаг к новой карьере в Т-Банке!*\n"
        "💲 За регистрацию по нашей ссылке Вы дополнительно получите 2500 руб.\n\n"
        "❓ Если остались вопросы по вакансии, задайте вопрос менеджеру @CashBot\n\n"
        "🔗 [Нажмите здесь, чтобы оставить заявку](https://trk.ppdu.ru/click/3uNod0HC?erid=2SDnjcbs16H)"

    )
  
    await callback.message.answer_photo(photo=photo_url, caption=text_instruction, parse_mode='Markdown') 


@router.callback_query(F.data == 'rewards')
async def send_rewards(callback: CallbackQuery):
    await callback.answer('Файл загружен')
    
    # Получаем абсолютный путь к файлу
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Вознаграждения.xlsx')
    
    
    # Проверка существования файла
    if not os.path.exists(file_path):
        await callback.message.answer("Файл не найденн.")
        print("Файл не найден:", file_path)  # Для отладки
        return
    
    # Создание объекта FSInputFile
    input_file = FSInputFile(file_path)
    
    # Отправка файла Excel
    await callback.message.answer_document(input_file)



@router.callback_query(F.data == 'pz')
async def pz_pz(callback: CallbackQuery):
    await callback.answer('Отличный выбор!')
    partner_tasks_text = (
        "🌟 <strong>Партнерские задания</strong> 🌟\n\n"
        "Данный раздел предназначен для оформления различных финансовых инструментов:\n"
        "💳 <strong>Дебетовые и кредитные карты</strong>\n"
        "💳 <strong>Платежные стикеры</strong>\n"
        "🏦 <strong>Вклады</strong>\n"
        "🚗 <strong>ОСАГО</strong>\n"
        "и многое другое!\n\n"
        "Чтобы увидеть полный список доступных заданий, нажмите кнопку <strong>\"Перейти в витрину\"</strong>. 📋\n\n"
        "🔍 В зависимости от того, какую карту вы выбрали, наш бот выплачивает <strong>бонусы</strong>! \n"
        "💰 Сумму вознаграждений для каждого продукта можно скачать, нажав на кнопку <strong>\"Вознаграждения\"</strong>."
    )
    await callback.message.answer(partner_tasks_text, parse_mode='HTML', reply_markup=kb.partnerprogram)

@router.message(F.text == '📱 Мой кабинет')
async def cmd_lk(message: Message):
    tg_id = message.from_user.id  # Получаем Telegram ID пользователя
    user_data = await rq.get_user_data(tg_id)  # Получаем данные пользователя из БД

     # Приветственное сообщение для личного кабинета
    welcome_lk_message = (
        "👋 Добро пожаловать в Личный кабинет!\n\n"
        "Здесь вы можете отслеживать свою активность и баланс, а также выводить заработанные средства.\n"
        "Убедитесь, что вы знакомы со всеми возможностями, которые предлагает CashBot!"
    )

    if user_data:
        # Преобразуем дату регистрации в московское время, если она отсутствует
        registration_time = user_data['data_registration'].astimezone(pytz.timezone('Europe/Moscow'))

        # Вычисляем количество дней в боте
        now_msk = datetime.now(pytz.timezone('Europe/Moscow'))  # Получаем текущее время в МСК
        days_in_bot = (now_msk - registration_time).days


        await message.answer(welcome_lk_message)  # Отправка приветственного сообщения
        await message.answer(
            f'📱 Личный кабинет:\n➖➖➖➖➖➖➖➖➖\n'
            f'🆔 Мой ID: {user_data["tg_id"]}\n'
            f'🕜 Дней в боте: {days_in_bot}\n'
            f'➖➖➖➖➖➖➖➖➖\n'
            f'✅ Выполнено:\n'
            f'👁 Просмотр рекламы: {user_data["ads_viewed"]}\n'
            f'📝 Написание отзывов: {user_data["reviews_written"]}\n'
            f'👤 Партнерские задания: {user_data["partner_tasks_completed"]}\n'
            f'🏭 Оффлайн работа: {user_data["offline_tasks_completed"]}\n'
            f'➖➖➖➖➖➖➖➖➖\n'
            f'💳 Баланс:\n'
            f'● Основной: {user_data["balance"]}\n'
            f'● Выведено: {user_data["withdrawn"]}\n',
            reply_markup=kb.withdraw
        )
    else:
        await message.answer("🔴 Пользователь не найден в базе данных.")



@router.message(F.text == '🆘 О боте | Помощь')
async def help_section(message: Message):
    help_text = (
        "🤖 <strong>О боте</strong>\n"
        "Я бот, который помогает вам зарабатывать деньги онлайн, выполняя различные задания.\n"
        "Вот что я могу:\n"
        "- 📋 Предоставить уникальные задания\n"
        "- 🎁 Информировать о партнерских программах\n"
        "- 💬 Ответить на ваши вопросы\n"
        "- 💼 Обеспечить доступ к вашему личному кабинету\n\n"
        "<strong>Как я могу помочь вам?</strong>"
    )
    await message.answer(help_text, reply_markup=kb.help_keyboard, parse_mode='HTML')


@router.message(F.text == "Частые вопросы (FAQ)")
async def faq(message: Message):
    faq_text = (
        "❓ <strong>Часто задаваемые вопросы:</strong>\n"
        "1. Как начать зарабатывать с ботом?\n   - Просто выполните задания, которые я предоставляю.\n"
        "2. Как вывести заработанные деньги?\n   - Перейдите в раздел вывода средств в профиле.\n"
        "3. Как связаться с поддержкой?\n   - Перейдите в раздел 'Контактная информация'."
    )
    await message.answer(faq_text, parse_mode='HTML')

@router.message(F.text == "Инструкции и руководства")
async def instructions(message: Message):
    instructions_text = (
        "📜 <strong>Инструкции по использованию бота:</strong>\n"
        "1. Выберите задание из списка доступных.\n"
        "2. Ознакомьтесь с условиями выполнения.\n"
        "3. Выполните задание и отправьте результат.\n"
        "4. Получите вознаграждение на ваш баланс."
    )
    await message.answer(instructions_text, parse_mode='HTML')

@router.message(F.text == "Контактная информация")
async def contact_info(message: Message):
    contact_text = (
        "📞 <strong>Контактная информация:</strong>\n"
        "- Напишите на email: cashbot.officiall@gmail.com\n"
        "- Напишите в личные сообщения администратору: @CashBot_admin\n"
        "- Задавайте вопросы <a href='https://t.me/+PVA49PzAQUQ3MjMy'>в чате</a>"
    )
    await message.answer(contact_text, parse_mode='HTML')


@router.message(F.text == "Политика конфиденциальности")
async def privacy_policy(message: Message):
    privacy_text = (
        "🔒 <strong>Политика конфиденциальности:</strong>\n"
        "Мы заботимся о вашей конфиденциальности и не передаем ваши данные третьим лицам."
    )
    await message.answer(privacy_text, parse_mode='HTML')




@router.message(F.text == "Назад")
async def back_to_menu(message: Message):
   await message.answer(text="Вы вернулись в главное меню.", reply_markup=kb.main)    