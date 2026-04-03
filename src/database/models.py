from datetime import datetime
from typing import Annotated

from sqlalchemy import BigInteger, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


intpk = Annotated[int, mapped_column(primary_key=True, type_=BigInteger)]
created_at = Annotated[datetime, mapped_column(default=datetime.utcnow)]
update_at = Annotated[datetime, mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)]
user_id = Annotated[int, mapped_column(ForeignKey('users.id'))]
storage = Annotated[dict, mapped_column(default={}, type_=JSON)]
big_int = Annotated[int, mapped_column(type_=BigInteger)]


class UsersOrm(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id: Mapped[intpk]
    role: Mapped[str] = mapped_column(default='user')
    storage: Mapped[storage]
    update_at: Mapped[update_at]
    created_at: Mapped[created_at]


class PersonalDataOrm(Base):
    __tablename__ = 'personal_data'
    __table_args__ = {'extend_existing': True}

    id: Mapped[intpk]
    user_id: Mapped[user_id]
    name: Mapped[str] = mapped_column(default='')
    surname: Mapped[str] = mapped_column(default='')
    phone_number: Mapped[str]
    email: Mapped[str]
    patronymic: Mapped[str] = mapped_column(default='')
