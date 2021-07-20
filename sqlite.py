import psycopg2
from psycopg2 import Error



def conn():
    try:
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password=" ",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        

        
        return cursor, connection

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

def create_table():
    cursor, connection = conn()
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE FreeSteamBot
                          (USER_ID           INT    NOT NULL,
                          STATUS         BOOL); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()


def get_subs():
    cursor, connection = conn()

    cursor.execute("select USER_ID from FreeSteamBot where status = True ")

    a = cursor.fetchall()
    
    
    cursor.close()
    connection.close()

    return a


def add_sub(user_id):
    cursor, connection = conn()

    cursor.execute(f""" INSERT INTO FreeSteamBot (USER_ID, STATUS) VALUES ({user_id}, {True})""")

    connection.commit()

    cursor.close()
    connection.close()


def edit_sub(user_id, status):
    cursor, connection = conn()

    cursor.execute(f"""Update FreeSteamBot set STATUS = {status} where user_id = {user_id}""")

    connection.commit()

    cursor.close()
    connection.close()

def subs_exist(user_id):
    cursor, connection = conn()

    cursor.execute(f"select * from FreeSteamBot where USER_ID = {user_id} ")

    a = cursor.fetchall()

    cursor.close()
    connection.close()

    return a 


a = get_subs()

for i in a:
    print(i[0])