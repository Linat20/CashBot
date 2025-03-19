from sqlalchemy import DateTime, Numeric
from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select
from datetime import datetime, timezone
import pytz  # Импортируйте pytz

async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select (User).where (User.tg_id==tg_id))


        if not user:
             # Создаем нового пользователя с заполнением всех необходимых полей

            msk_timezone = pytz.timezone('Europe/Moscow')  # Задать временную зону для МСК
            now_msk = datetime.now(msk_timezone)  # Получаем текущее время в МСК

            new_user = User(
                tg_id=tg_id,
                data_registration=now_msk,  # Устанавливаем текущее время регистрации по МСК
                balance=0.0,  # Начальный баланс
                withdrawn=0.0,  # Начальная сумма вывода
                ads_viewed=0,  # Количество просмотренной рекламы
                reviews_written=0,  # Количество написанных отзывов
                partner_tasks_completed=0,  # Выполненные партнерские задания
                offline_tasks_completed=0  # Офлайн работы
            )
            session.add(new_user)  # Добавляем нового пользователя в сессию
            await session.commit()  # Коммитим изменения в базе данных


async def get_user_data(tg_id: int) -> dict:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalars().first()
        
        if user:
            return {
                "tg_id": user.tg_id,
                "data_registration": user.data_registration,
                "balance": user.balance,
                "withdrawn": user.withdrawn,
                "ads_viewed": user.ads_viewed,
                "reviews_written": user.reviews_written,
                "partner_tasks_completed": user.partner_tasks_completed,
                "offline_tasks_completed": user.offline_tasks_completed,
            }
    return None