import sqlite3
import functools

#### decorator to lof SQL queries
# Complete the code below by writing a decorator log_queries that logs the SQL query before executing it.
# boiler plate code
# def decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # code to execute
#         return func(*args, **kwargs)
#         func()
#     return wrapper
# Actual code
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else 'no query specified')
        print(f"[LOG] Executing SQL Query: {query}")
        return func(*args, **kwargs)
        func()
    return wrapper
        
    
 
 


#""" YOUR CODE GOES HERE"""

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")