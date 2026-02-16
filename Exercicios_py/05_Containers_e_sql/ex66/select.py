import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} '
               'WHERE weight = "20" ')

row = cursor.fetchone()
print(row)
'''
for row in cursor.fetchall():
    name,weight = row
    print(name,weight)
'''

cursor.close()
connection.close()