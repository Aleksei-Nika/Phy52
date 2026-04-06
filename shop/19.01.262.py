# SELECT column, agregate_func FROM table
# WHERE condition
# GROUP BY column
# HAVING condition

# SELECT Employee, SUM(Amount) as TotalAmount
# FROM sales
# GROUP BY Employee
# HAVING TotalAmount > AVG(Amount);

import sqlite3
db_path = 'company.db'

def run_having(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            select department_id from employees
            group by department_id
            having count(employee_id) > 2;
        ''')
        print(f'Task1: {cursor.fetchall()}')

run_having(db_path)