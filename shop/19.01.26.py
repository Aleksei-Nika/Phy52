# SELECT column, agregate_func FROM table
# WHERE condition
# GROUP BY column
# HAVING condition

# SELECT Employee, SUM(Amount) as TotalAmount
# FROM sales
# GROUP BY Employee
# HAVING TotalAmount > AVG(Amount);

from datetime import date
import sqlite3
db_path = 'company.db'

# def run_having(db_path):
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             select department_id from employees
#             group by department_id
#             having count(employee_id) > 2;
#         ''')
#         print(f'Task1: {cursor.fetchall()}')

#         cursor.execute('''
#             select project_id from tasks
#             group by project_id
#             having max(deadline) > '2025-06-01';
#         ''')
#         print(f'Task2: {cursor.fetchall()}')

#         cursor.execute('''
#             select distinct project_id from projectassignments
#             where assigned_date < '2025-02-01'
#         ''')
#         print(f'Task4: {cursor.fetchall()}')

#         cursor.execute('''
#             select employee_id
#             from projectassignments
#             group by employee_id
#             having count(project_id) = 2;
#         ''')
#         print(f'Task5: {cursor.fetchall()}')

# run_having(db_path)


# INNER JOIN/LEFT JOIN

# SELECT column1, column2
# FROM table1
# JOIN table2
# ON table1.id = table2.id

# select group_name from faculties
# join students 
# on faculties.group_id = students.group_id
# where name = 'Мария';

# INNER JOIN - записи, у которых есть совпадения в обеих таблицах

# LEFT JOIN - все записи из левой таблицы и подходящие из правой таблицы


# def run_join(db_path):
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#         select e.full_name, d.department_name
#         from employees e
#         join departments d
#         on e.department_id = d.department_id;
#         ''')
#         print(f'Task1: {cursor.fetchall()}')

#         cursor.execute('''
#         select e.full_name, c.email
#         from employees e
#         left join contacts c
#         on e.contact_id = c.contact_id;
#         ''')
#         print(f'Task2: {cursor.fetchall()}')

#         cursor.execute('''
#         select p.project_name, count(employee_id)
#         as count_emp_to_project from projects p
#         left join ProjectAssignments pa
#         on p.project_id = pa.project_id
#         group by p.project_id;
#         ''')
#         print(f'Task3: {cursor.fetchall()}') 

#         cursor.execute('''
#         select e.full_name, d.department_name, 
#         dl.city from employees e
#         join departments d
#         on e.department_id = d.department_id
#         join departmentlocations dl
#         on d.department_id = dl.department_id
#         ''')
#         print(f'Task4: {cursor.fetchall()}') 

#         cursor.execute('''
#         select d.department_name, count(e.employee_id) as count_staff
#         from departments d
#         join employees e
#         on d.department_id = e.department_id
#         group by d.department_id
#         having count_staff > 2;     
#         ''')
#         print(f'Task5: {cursor.fetchall()}')

# run_join(db_path)



# 21.01.26
# SELECT col FROM table
# WHERE col ОПЕРАТОР (
#     SELECT col FROM table
#     WHERE condition
# )
# ()
# 1)Скаляр
# 2)Список
# 3)Таблица

def run_queris(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT e.full_name FROM employees e
        JOIN ProjectAssignments pg
        ON e.employee_id = pg.employee_id
        JOIN Projects p
        ON pg.project_id = p.project_id    
        WHERE p.status = 'Active'
        GROUP BY e.employee_id 
        HAVING COUNT(p.project_id)>1;
    ''')
        print(f'Task1: {cursor.fetchall()}')
        
        current_year = date.today().year
        cursor.execute(f'''
    SELECT d.department_name FROM Departments d 
    JOIN Employees e 
    ON d.department_id = e.department_id
    GROUP BY d.department_id
    HAVING AVG({current_year}-strftime('%Y', e.hire_date))
    >            
    (SELECT AVG({current_year}-strftime('%Y', e.hire_date))
    FROM Employees e)
    ''')
        print(f'Task2: {cursor.fetchall()}')

        cursor.execute('''
    SELECT p.project_name FROM Projects p
    WHERE p.project_id NOT IN                    
    (SELECT p.project_id FROM Projects p
     JOIN ProjectAssignments pa
     ON p.project_id = pa.project_id
     JOIN Employees e
     ON pa.employee_id = e.employee_id
     JOIN Departments d
     ON e.department_id = d.department_id 
     WHERE d.department_name = 'Разработка')
    ''')
        print(f'Task3: {cursor.fetchall()}')

        cursor.execute('''
    SELECT dl.Country FROM DepartmentLocations dl
    JOIN Employees e
    ON dl.department_id = e.department_id
    JOIN ProjectAssignments pa
    ON e.employee_id = pa.employee_id
    JOIN Tasks t
    ON pa.project_id = t.project_id
    WHERE t.priority = 'High'
    GROUP BY dl.country
    HAVING COUNT(t.task_id) > 2;
    ''')
        print(f'Task4: {cursor.fetchall()}')

        cursor.execute('''
            SELECT d.department_name FROM Departments d
            WHERE EXISTS(
                SELECT 1 FROM DepartmentLocations dl
                WHERE dl.department_id = d.department_id
            )
        ''')
        print(f'Task5: {cursor.fetchall()}')

        cursor.execute('''
        SELECT AVG(task_count) FROM 
        (SELECT COUNT(task_id) as task_count
        FROM Tasks
        GROUP BY project_id) as tmp_table   
        ''')
        print(f'Task6: {cursor.fetchall()}')

        cursor.execute('''
        SELECT full_name FROM Employees 
        WHERE employee_id = (
            SELECT department_id FROM Departments             
            WHERE department_name = 'Разработка')
        ''')
        print (f'Task: {cursor.fetchall()}')   

run_queris(db_path)


