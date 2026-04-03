from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from ..config.config_reader import (DATABASE_NAME, DATABASE_PASSWORD, DATABASE_PORT,
                                    DATABASE_URI, DATABASE_USER)


async_engin = create_async_engine(
    url=f'postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@'
        f'{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}',
    # echo=True,
)

async_session_factory = async_sessionmaker(
    autocommit=False, autoflush=False, bind=async_engin, class_=AsyncSession,
)


async def init_db() -> None:
    from models import UsersOrm  # noqa

    async with async_engin.begin() as connection:
        if input('drop base database? (y/n): ') == 'y':
            if input('send password: ') == DATABASE_PASSWORD:
                print('deleting the database...')
                await connection.run_sync(Base.metadata.drop_all)
                print('deleting the database is complete')
            else:
                print('password incorrect. Canceling drop the database')
        await connection.run_sync(Base.metadata.create_all)


class Base(DeclarativeBase):
    # @declared_attr.directive
    # def __tablename__(cls) -> str:
    #     return cls.__name__.lower() + 's'
    pass
