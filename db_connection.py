# db_connection.py

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       # Put your actual password
        database="chatbot_db",  # Your DB name
        port=3306
    )
