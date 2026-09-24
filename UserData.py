import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def get_connection():
    conn = sqlite3.connect('Database.db')
    return conn

#Create Table 
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS USERS (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )'''
    )
    conn.commit()
    print("Table Created successfully")
    conn.close()



#Function to add Username and Password
def add_data(username, password):
    conn = get_connection()
    hash_password = generate_password_hash(password)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO USERS (username, password)
        VALUES(?,?)
        ''', (username, hash_password) 
    )
    conn.commit()
    conn.close()



#Fetch details from table
def fetch_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT * FROM USERS
        '''
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#Fetch one user details from table
def find_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT * FROM USERS
        WHERE username = ?
        ''', (username,)
    )
    row = cursor.fetchone()
    conn.close()
    return row



if __name__ == "__main__":
    create_table()
    fetch_data()
