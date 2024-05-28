
#-------------------ЗАДАЧА №6-----------------------#

'''Создание таблицы и вставка данных: Напишите программу,
которая создает таблицу в базе данных SQLite и вставляет в нее
данные.'''

import sqlite3


def create_bd(name_db):
    
    conn = sqlite3.connect(name_db)
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    
    ''')
    
    conn.commit()
    cur.close()
    conn.close()
 
def adding_data(name_db): 
    
    conn = sqlite3.connect(name_db)
    cur = conn.cursor()
    
    cur.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)", 
        ('Sergei', 22)
    )
    cur.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)", 
        ('Natalya', 19)
    )
    cur.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)", 
        ('Ivan', 23)
    )    
    
    conn.commit()
    cur.close()
    conn.close()
    
create = create_bd('Task_6/data.db')    
add_data = adding_data('Task_6/data.db')