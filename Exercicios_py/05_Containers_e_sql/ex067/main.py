import dotenv
import pymysql
import pymysql.cursors
import os
from pathlib import Path

TABLE_NAME = 'customers'

dotenv.load_dotenv(dotenv_path=Path(__file__).parent / '.env')

print(os.getenv('MYSQL_HOST'))



connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)
with connection:
    with connection.cursor() as cursor:
        sql_comm = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(50) NOT NULL,
            idade INT NOT NULL,
            PRIMARY KEY (id)
        )
        """
         # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)  # type: ignore

    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
#        result = cursor.execute(sql, data2)  # type: ignore

#    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age": 33, },
            {"name": "Júlia", "age": 74, },
            {"name": "Rose", "age": 53, },
        )
#        result = cursor.executemany(sql, data3)  # type: ignore
#    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
        )
#        result = cursor.executemany(sql, data4)  # type: ignore
#    connection.commit()          


    with connection.cursor() as cursor:
        sql = f'SELECT * FROM {TABLE_NAME}'
        cursor.execute(sql)


#Delete WHERE
    with connection.cursor() as cursor:

        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id > 100'    
        )

        cursor.execute(sql)  
        connection.commit()

    with connection.cursor() as cursor:

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id = %s'    
        )
 
        cursor.execute(sql,('Gemma',40,96))  
        connection.commit()

    with connection.cursor() as cursor:
        resultFromSelect = cursor.execute('SELECT * FROM customers')
        data6 = cursor.fetchall()

        cursor.execute(f'SELECT id from {TABLE_NAME} '
                                          'ORDER BY id DESC LIMIT 1')
        lastidfromselect = cursor.fetchone()

        print('len de data',len(data6))
        print('result from select: ',resultFromSelect)
        print('rowcount', cursor.rowcount)
        print('lastrowid por select',
              lastidfromselect['id'])