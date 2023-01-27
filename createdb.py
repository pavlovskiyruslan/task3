import sqlite3
import pandas as pd

def db_create():
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
          user_name TEXT)
          ''')

    c.execute('''
          CREATE TABLE IF NOT EXISTS ardess
          (id SERIAL PRIMARY KEY, fk_user_id INTEGER REFERENCES users(user_id), adress TEXT)
          ''')

    c.execute('''
          CREATE TABLE IF NOT EXISTS contact
          (id INTEGER PRIMARY KEY,
          phone_number INTEGER,
          fk_contact INTEGER REFERENCES users(user_id))
          ''')


    conn.commit()
    c.execute('''
        SELECT * FROM contact
    ''')

def insert_into_db():
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('''
          INSERT INTO users (user_name)
                VALUES
                ('Ruslan'),
                ('Andrey'),
                ('Petr'),
                ('Ivan'),
                ('Sardor')
          ''')
    conn.commit()
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('''
        INSERT INTO contact (phone_number, fk_contact)
                VALUES
                (+998974502925, '1'),
                (+998909914239, '1'),
                (+998975551122, '2'),
                (+998909705566, '3'),
                (+998934506699, '4'),
                (+999452345678, '5')
          ''')
    conn.commit()
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('''
          INSERT INTO ardess (fk_user_id, adress)
                VALUES
                ('1', 'Yunusabad 1 11 2'),
                ('2', 'Chilonzor 4 2 1'),
                ('3', 'Yashnobod 2 9 1'),
                ('4', 'Bektemir Kuyluk'),
                ('5', 'Uchtepa 13 1 23')
          ''')
    conn.commit()

def create_user():
    user_name_input = str(input("Введите имя пользователя:"))
    #user_id_input = int(input("Выберите ID"))
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('INSERT INTO users (user_name) VALUES (?)' ,(user_name_input,))
    conn.commit()
    print("Пользователь" + ":" + user_name_input + "--" + "Успешно добавлен")
    c.execute('SELECT user_id FROM users WHERE user_name =?',(user_name_input,))
    records = c.fetchall()
    for row in records:
        user_get_id = row[0]
    print(user_get_id)
    user_adress_input = str(input("Введите Адрес пользователя:"))
    c.execute('INSERT INTO ardess (fk_user_id, adress) VALUES (?,?)', (user_get_id, user_adress_input,))
    print("Адрес добавлен успешно")

    conn.commit()
    c.execute('SELECT users.user_id, users.user_name, ardess.adress  FROM users, ardess WHERE users.user_id = ardess.fk_user_id AND user_id = ?',(user_get_id,))
    df = pd.DataFrame(c.fetchall(), columns=['ID', 'Имя', 'Адрес'])
    print(df)

    #----------------------------------------------------
    #Добавление контактов для пользователя
    #user_get_id  == id Пользователя
    user_phonenumber = str(input("Введите номер телефона пользователя:"))
    c.execute('INSERT INTO contact (fk_contact, phone_number) VALUES (?,?)', (user_get_id, user_phonenumber,))
    print("Номер добавлен успешно")
    conn.commit()
    c.execute('SELECT contact.*, users.user_name, ardess.adress FROM contact INNER JOIN users ON users.user_id = contact.fk_contact INNER JOIN ardess ON users.user_id = ardess.fk_user_id WHERE users.user_id =?',(user_get_id,))
    records = c.fetchall()
    for row in records:
        print(row)


def select_all_users():
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    df = pd.DataFrame(c.fetchall(), columns=['user_id', 'user_name'])
    print(df)

def select_one_user_by_id():
    user_id_input = int(input("Введите ID - пользователя"))
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('SELECT user_id, user_name FROM users WHERE user_id = ?',(user_id_input,))
    df = pd.DataFrame(c.fetchall(), columns=['user_id', 'user_name'])
    print(df)


def show_contact_table():
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('SELECT * FROM contact')
    df = pd.DataFrame(c.fetchall(), columns=['id','contact','fk'])
    print (df)

def user_and_adress():
    conn = sqlite3.connect('users')
    c = conn.cursor()
    user_id_input = int(input("Введите ID - пользователя"))
    c.execute('SELECT users.user_id, users.user_name, ardess.adress  FROM users, ardess WHERE users.user_id = ardess.fk_user_id AND user_id = ?',(user_id_input,))
    df = pd.DataFrame(c.fetchall(), columns=['ID', 'Имя', 'Адрес'])
    print(df)

def user_and_contact():
    user_id_input = int(input("Введите ID - пользователя"))
    conn = sqlite3.connect('users')
    c = conn.cursor()
    c.execute('SELECT contact.phone_number, users.user_name FROM contact INNER JOIN users ON users.user_id = contact.fk_contact WHERE users.user_id = ?',(user_id_input,))
    rows = c.fetchall()
    for row in rows:
        print(row)
def all_info_about_user():
    conn = sqlite3.connect('users')
    c = conn.cursor()
    user_id_input = int(input("Введите ID - пользователя"))
    c.execute('SELECT contact.*, users.user_name, ardess.adress FROM contact INNER JOIN users ON users.user_id = contact.fk_contact INNER JOIN ardess ON users.user_id = ardess.fk_user_id WHERE users.user_id =?', (user_id_input,))
    records = c.fetchall()
    for row in records:
        print(row)