import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#CRUD - Create Read Update Delete
#SQL - Insert Select UPDATE DELETE

cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}' 
     '('
    'name TEXT,'
    'weight REAL'
    ')'
)


connection.commit()

#Registrar valores nas colunas da tabela
#cuidado ao receber valores de usario, SQL injection.
sql_command = (f'INSERT INTO {TABLE_NAME}'
               '(name, weight) '
               'VALUES '
               '(:name, :weight)')
'''
cursor.execute(sql_command,
                   {'name':'Joshua', 'weight':4}
                    )
'''
#  
#              '(NULL, "Sedgar", 20.20), (NULL, "Lena", 1.89)')

cursor.executemany(sql_command, 
                   (
                      {'name':'Barst','weight': 20},
                      {'name':'Bord','weight': 20},
                      {'name':'Cord','weight': 20},
                      {'name':'Dord','weight': 20},
                      {'name':'Darros','weight': 20}
                   ))

if __name__ == '__main__':
   print(sql_command)
   cursor.execute(f'UPDATE {TABLE_NAME} '
      'SET weight=31.5 '
   'WHERE name = "Dord"'
   )

   cursor.execute(f'SELECT * FROM {TABLE_NAME}')
   for row in cursor.fetchall():
      name,weight = row
      print(name,weight)
   connection.commit()

cursor.close()
connection.close()