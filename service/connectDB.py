import mariadb
import sys


def getDB():
    try:
        conn = mariadb.connect(
            user="root",
            password="admin",
            host="127.0.0.1",
            port=3306,
            database="elearning"

        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
