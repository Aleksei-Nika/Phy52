import sqlite3

def create_table_products():
    with sqlite3.connect('shop.db') as conn:
        conn.execute('''
            create table if not exists products(
            id integer primary key autoincrement,
            name text unique,
            price real not null, 
            quantity integer not null,
            is_available integer default 1                                                                 
            );
            ''')
        print('Таблица Products создана')

def create_table_users():
    with sqlite3.connect('shop.db') as conn:
        conn.execute(
            '''
            create table if not exists users(
            id integer primary key autoincrement,
            name text unique,
            phone text not null,
            is_admin integer default 0);
            '''
        )
        print('Таблица Users создана')

def create_table_orders():
    with sqlite3.connect('shop.db') as conn:
        conn.execute('''
            create table if not exists orders(
            id integer primary key autoincrement,
            total_amount real,
            order_data text
            );
        ''')
        print('Таблица Orders создана')

def fill_products():
    data = [
        ('Ноутбук', 50_000, 10),
        ('Мышь', 1_500, 50),
        ('Клавиатура', 3_000, 20),
    ]
    with sqlite3.connect('shop.db') as conn:
        conn.executemany(
            '''insert into products (name, price, quantity)
            values (?, ?, ?);
            ''', data)
        conn.commit()
        print('Products заполнена данными')

def fill_users():
    data = [
        ('Alexanrd', '80000000000'),
        ('Alexei', '89999999999'),
        ('Pavel', '88888888888')
    ]
    with sqlite3.connect('shop.db') as conn:
        conn.executemany(
            '''
            insert into users (name, phone)
            values (?, ?);
            ''', data)
        conn.commit()
        print('Users заполнена данными')

def fill_orders():
    data = [
        (1_000.0, '2025-12-05'),
        (5_050.0, '2025-12-24'),
        (1_500.0, '2026-01-10')
    ]
    with sqlite3.connect('shop.db') as conn:
        conn.executemany(
            '''
            insert into orders (total_amount, order_data)
            values (?, ?);
            ''', data)
        conn.commit()
        print('Orders заполнена данными')

def create_table_order_details():
    with sqlite3.connect('shop.db') as conn:
        conn.execute(
            '''
            create table if not exists order_details(
            id integer primary key autoincrement,
            order_id integer,
            product_id integer,
            quantity integer not null,
            foreign key (order_id) references orders(id),
            foreign key (product_id) references products(id)
            );
            '''
        )
        print('Таблица Order Details создана')

def fill_order_details():
    data = [
            (1, 1, 3),
            (1, 2, 1),
            (2, 3, 2)
        ]
    with sqlite3.connect('shop.db') as conn:
        conn.executemany('''
            insert into order_details(order_id, product_id, quantity)
            values (?, ?, ?)
            ''', data)
        conn.commit()
        print('Order details заполнена данными')

def alter_table():
    with sqlite3.connect('shop.db') as conn:
        try:
            conn.execute('''
                alter table orders add column
                user_id integer references users(id);
                ''')
            print('Ключ в orders добавлен')
        except sqlite3.OperationalError:
            pass
        conn.execute('''
            update orders set user_id = 1
            where id = 1;
            ''')
        print('Orders таблица обновлена')

def agregation_func():
    with sqlite3.connect('shop.db') as conn:
        cursor = sqlite3.cursor()
        conn.execute(
            '''
            select sum(quantity), avg(price)
            from products
            '''
        )
        

if __name__ == '__main__':
    create_table_products()
    create_table_users()
    create_table_orders()
    # fill_products()
    # fill_users()
    # fill_orders()

    create_table_order_details()
    # fill_order_details()

    alter_table()

