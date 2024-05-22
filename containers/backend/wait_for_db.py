import time
import MySQLdb 

def check_database():
    try:
        connection = MySQLdb.connect(
            host="db", 
            user="root", 
            passwd="pwd",
            db="alpha_archives" 
        )
        connection.close()
        return True
    except MySQLdb.OperationalError:
        return False

if __name__ == "__main__":
    print("Waiting for database to be ready...")
    time.sleep(10) 
    while not check_database():
        print("Waiting for database to be ready...")
        time.sleep(5) 
    print("Database is ready.")