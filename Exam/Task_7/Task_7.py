#-----------------ЗАДАЧА №7-----------------------#

'''Создание таблицы, вставка данных, обновление данных:
Ваша задача создать таблицу и вставить в неё данные и
продемонстрировать обновление данных.'''


import sqlite3

conn = sqlite3.connect('Task_7/students_grades.db')
cursor = conn.cursor()
                                                      
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade REAL NOT NULL
);
"""
cursor.execute(create_table_query)
conn.commit()

students = [
    {"name": "Иван", "grade": 8},
    {"name": "Алексей", "grade": 9},
    {"name": "Мария", "grade": 7}
]

for student in students:
    insert_query = """
    INSERT INTO students (name, grade) VALUES (?, ?);
    """
    cursor.execute(insert_query, (student['name'], student['grade']))
conn.commit()


average_query = """
SELECT name, AVG(grade) AS average_grade FROM students GROUP BY name;
"""
cursor.execute(average_query)
students_and_averages = cursor.fetchall()

for student, average in students_and_averages:
    print(f"{student}: {average}")


conn.close()