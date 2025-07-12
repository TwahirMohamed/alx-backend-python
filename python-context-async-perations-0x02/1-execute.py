import mysql.connector

class ExecuteQuery:
    def __init__(self, connection_params):
        self.connection_params = connection_params
        self.connector = None

    def __enter__(self):
        print("Connecting to the Database ...")
        try:
            self.connector = mysql.connector.connect(**self.connection_params)
        except Exception as e:
            print("Connection Error:", e)
        else:
            print("Connected to the database.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connector:
            self.connector.close()
            print("Connection closed.")
        if exc_type:
            print("An error occurred:", exc_val)
        return False  # Propagate exception

    def run_query(self, query, params=None):
        if not self.connector:
            print("No active connection.")
            return None
        try:
            cursor = self.connector.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Exception as e:
            print("Query failed:", e)
            return None
# Example of Usage 
connection_params = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

with ExecuteQuery(connection_params) as db:
    query = "SELECT * FROM users WHERE age > %s"
    results = db.run_query(query, (30,))
    print("User Records:")
    for row in results:
        print(row)