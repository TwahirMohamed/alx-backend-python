import  mysql.connector

class DatabaseConnection(object):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connector = None

    def __enter__(self):
        print("Connecting to the Database ...")
        try:
            self.connector = mysql.connector.connect(self.connection_string)
        except Exception:
            print("Connection Error")
        else:
            print("Connected to the database.")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        if exc_type:
            print("An error occurred:", exc_val)
        return False  # Propagate exceptions if any

# Using the custom context manager
with DatabaseConnection("test.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print("User Records:")
    for row in results:
        print(row)

