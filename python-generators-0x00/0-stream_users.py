from multiprocessing import connection
import mysql.connector
import seed
def stream_users():
    """
    This function connects to a MYSQL databases and retrieves data from user_data table.
    """
    #establishing the connection
    connection = seed.connect_to_prodev()

    #Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    #Retrieving single row
    sql = '''SELECT * from user_data'''

    #Executing the query
    cursor.execute(sql)

    # Using python generators to iterate through the rows
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    

    # #Fetching 1st row from the table
    # result = cursor.fetchone();
    # print(result)

    # #Fetching all rows from the table
    # result = cursor.fetchall();
    # print(result)

    # Closing the cursor
    cursor.close()

    #Closing the connection
    connection.close()