import sqlite3

database_connection = sqlite3.connect('database\student_records.db')
cursor = database_connection.cursor()
print('Database created and connected successfully')

try:
    sqlite_create_table_query = '''CREATE TABLE record (    name TEXT,
                                                            regno TEXT,
                                                            branch TEXT,
                                                            gender TEXT,
                                                            age INTEGER,
                                                            contact INTEGER,
                                                            email TEXT
                                                        );'''
    cursor.execute(sqlite_create_table_query)
    database_connection.commit()
    print('Table created')
    cursor.close()

except Exception:
    print("There was some error while creating the table")