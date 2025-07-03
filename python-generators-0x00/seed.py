import mysql.connector
from mysql.connector import errorcode
import config

# Prototypes:
# * def connect_db() :- connects to the mysql database server
# * def create_database(connection):- creates the database ALX_prodev if it does not exist
# * def connect_to_prodev() connects the the ALX_prodev database in MYSQL
# * def create_table(connection):- creates a table user_data if it does not exists with the required fields
# * def insert_data(connection, data):- inserts data in the database if it does not exist

# Database connection details (replace with your own)
def connect_db():
    """Method to connect to the mysql  database server"""
    try:
        connection  = mysql.connector.connect(
            host= config.host,
            user= config.user,
            password= config.password
        )
        print("Connection successful")
        return connection

    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
        return None
    

def create_database(connection):
    try:
        mycursor = connection.cursor()

        # Creating database
        mycursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database 'ALX_prodev' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        if mycursor:
            mycursor.close()


def connect_to_prodev():
    """Method that connects ALX_prodev database in MYSQL"""
    try:
        cnx = mysql.connector.connect(
            host="localhost",  # Or the IP address/hostname of your MySQL server
            user="your_username",
            password="your_password",
            database="ALX_prodev"
        )
        print("Connected to MySQL database successfully!")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_table(connection):
    """Creates user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id UUID PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Table 'user_data' ensured to exist.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        if cursor:
            cursor.close()

def insert_data(connection, data):
    """
    Inserts data into user_data if username and email do not exist.
    Expects data as a dict: {'user_id': ..., 'username': ..., 'email': ...}
    """
    try:
        cursor = connection.cursor()

        # Check if user exists
        query = """
            SELECT user_id FROM user_data WHERE username = %s OR email = %s
        """
        cursor.execute(query, (data['username'], data['email']))
        existing = cursor.fetchone()

        if existing:
            print("User with this username or email already exists. No insert performed.")
        else:
            insert_query = """
                INSERT INTO user_data (user_id, username, email)
                VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (data['user_id'], data['username'], data['email']))
            connection.commit()
            print("User data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    finally:
        if cursor:
            cursor.close()

