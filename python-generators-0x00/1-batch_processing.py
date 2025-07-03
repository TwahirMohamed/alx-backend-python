import mysql.connector
import config
import seed

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches of batch_size."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """Process batches and print users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get("age", 0) > 25:
                print(user)
