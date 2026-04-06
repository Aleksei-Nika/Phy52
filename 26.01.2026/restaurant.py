from typing import Optional
import sqlalchemy
from sqlalchemy import Engine, String, Float, Integer, ForeignKey, select, not_
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, MappedColumn, mapped_column, relationship
from sqlalchemy.exc import NoResultFound

engine = sqlalchemy.create_engine('sqlite:///restaurant.db')

class Base(DeclarativeBase):
    pass

order_items = sqlalchemy.Table(
    'order_items', # название таблицы
    Base.metadata,
    sqlalchemy.Column('order_id', ForeignKey('orders.id'), primary_key=True),
    sqlalchemy.Column('dish_id', ForeignKey('dishes.id'), primary_key=True)
)

class RestTable(Base):
    __tablename__ = 'tables'
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    orders: Mapped[list['Order']] = relationship(back_populates='table')
    capacity: Mapped[int]
    is_available: Mapped[bool] = mapped_column(nullable=True)

class Dish(Base):
    __tablename__ = 'dishes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    callories: Mapped[float] = mapped_column(default=0, nullable=True)
    price: Mapped[float]
    orders: Mapped[list['Order']] = relationship(back_populates='dishes', secondary=order_items)

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(default='принят')
    table_id: Mapped[int] = mapped_column(ForeignKey('tables.id'))
    table: Mapped[RestTable] = relationship(back_populates='orders')
    dishes: Mapped[list[Dish]] = relationship(back_populates='orders', secondary=order_items)
    @property
    def total_price(self)->float:
        return sum(dish.price for dish in self.dishes)

# Base.metadata.create_all(engine)

# with Session(engine) as session:
#     table1 = RestTable(number=1, capacity=1)
#     pizza = Dish(name='Маргарита', price=800.0)
#     pasta = Dish(name='Карбанара', price=700.0)
#     cake = Dish(name='Чизкейк', price= 500.0)

#     table2 = RestTable(number=2, capacity=2)
#     order2 = Order(table = table2)
#     order2.dishes.append(pasta)
#     order2.dishes.append(cake)

#     new_order = Order(table=table1)
#     new_order.dishes.append(pizza)
#     new_order.dishes.append(pasta)
#     session.add_all([table1, table2, pizza, pasta, cake, new_order, order2])
#     session.commit()
#     print('Данные добавлены')

# with Session(engine) as session:
#     query = select(Order).where(Order.id==1)
#     my_order = session.scalar(query)
#     print(f'Сумма заказа: {my_order.id}: {my_order.total_price} руб.')

# def get_free_tables(session: Session):
#     query = select(Order.table_id).where(Order.status == 'принято')
#     query2 = select(RestTable).where(not_(RestTable.id.in_(query)))
#     return session.scalars(query2).all()

# with Session(engine) as session:
#     tabels = get_free_tables(session)
#     if tabels:
#         print(f'Кол-во свободных столов: {len(tabels)}')
#         for t in tabels:
#             print(f'#{t.number}, Вместительность: {t.capacity}')
#     else:
#         print('Столы не найдены')

# def get_popular_dish(session: Session):
#     query = select(Dish.name, sqlalchemy.func.count(order_items.c.order_id).label('total_sales')).join(order_items).group_by(Dish.id).order_by(sqlalchemy.func.count(order_items.c.order_id).desc())
#     return session.execute(query).all()

# with Session(engine) as session:
#     dishes = get_popular_dish(session)
#     max_count = dishes[0][1]
#     for row in dishes:
#         dish_name = row.name
#         sales_count = row.total_sales
#         if sales_count == max_count:
#             print(f'Самое популярное блюдо {dish_name}')

# def get_dish(session: Session, order_id: int, dish_name: str):
#     try:
#         # 1. ищем блюдо
#         query = select(Dish).where(Dish.name==dish_name)
#         dish = session.execute(query).scalar_one()

#         # 2. ищем заказ
#         order = session.get(Order, order_id)
#         if not order:
#             print('заказ не найден')
#             return

#         # Добавляем блюдо в заказ
#         order.dishes.append(dish)
#         session.commit()
#         print(f'Блюдо {dish_name} добавлено в заказ')
#     except NoResultFound:
#         print(f'Ошибка: блюдо {dish_name} не найдено')
#     except Exception as e:
#         session.rollback()
#         print(f'Произошла непредвиденная ошибка: {e}')

# with Session(engine) as session:
#     get_dish(session, 1,  'Чизкейк')

# alembic upgrade 