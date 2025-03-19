from sqlalchemy import BigInteger, DateTime, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from datetime import datetime


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')


async_session = async_sessionmaker(engine)


class Base(AsyncAttrs,DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    data_registration: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(datetime.timezone.utc))  # Исправлено 
    balance: Mapped[float] = mapped_column(Numeric(10, 2), default=0.0)  # Начальный баланс 0.0
    withdrawn: Mapped[float] = mapped_column(Numeric(10, 2), default=0.0)  # Выведено

    # Поля для статистики выполнения задач
    ads_viewed: Mapped[int] = mapped_column(default=0)  # Просмотрено рекламы
    reviews_written: Mapped[int] = mapped_column(default=0)  # Написано отзывов
    partner_tasks_completed: Mapped[int] = mapped_column(default=0)  # Выполнено партнерских заданий
    offline_tasks_completed: Mapped[int] = mapped_column(default=0)  # Оффлайн работ сделано


    # Создание таблицы
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)