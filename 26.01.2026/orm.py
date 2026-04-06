from typing import Optional
import sqlalchemy
from sqlalchemy import Engine, String, Integer, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, MappedColumn, mapped_column, relationship
# Mapped[int]
# Mapped[str]

engine = sqlalchemy.create_engine('sqlite:///example1.db', echo=True)

#Базовы класс для моделей
class Base(DeclarativeBase):
    pass
# Модель это класс в ORM, модель называем в единственном числе

class User(Base):
    __tablename__ = 'users' # имя таблицы во множественном числе
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True) # ограничение на вводимое количество символов
    age: Mapped[int] = mapped_column(Integer)
    full_name: Mapped[Optional[str]] # Может быть Null
    posts: Mapped[list['Post']] = relationship(back_populates='author')

class Post(Base):
    __tablename__ = 'Post'
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str]
    users_id: Mapped[str] = mapped_column(ForeignKey('users.id')) #Через имя таблица
    author: Mapped['User'] = relationship(back_populates='posts')

Base.metadata.create_all(engine) # создаст модели на основе модели наследуемых от Base

with Session(engine) as session:
    new_user = User(name='Ivan', age='10', full_name='Ivan Ivanov')
    session.add(new_user)
    session.commit()

    query = select(User).where(User.name=='Ivan')
    user = session.scalar(query)
    print(f'Пользователь: {user.full_name, user.age}')