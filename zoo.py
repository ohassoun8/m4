# 11.1

def hours():
    print('Open 9-5 daily')

import zoo
zoo.hours()



# 11.2
def hours():
    print('Open 9-5 daily')

import zoo as menagerie
menagerie.hours()




# 16.8

import sqlite3

# Connect to the db
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
''')

# Commit and close conn
conn.commit()
conn.close()

import sqlite3

# Connect to database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Select and print titles
cursor.execute('SELECT title FROM books ORDER BY title ASC')
for row in cursor.fetchall():
    print(row[0])

# Close conn
conn.close()
# you need to install sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, select

# Connect to database
engine = create_engine('sqlite:///books.db')
connection = engine.connect()
metadata = MetaData()

# books table
books = Table('books', metadata, autoload_with=engine)

# Create a query
query = select(books.c.title).order_by(books.c.title)

# Executing
result = connection.execute(query)

# Print
for row in result:
    print(row.title)

# Close conn
connection.close()