'''
https://www.tutorialspoint.com/python3/python_database_access.htm
'''

import pymysql


class ConnectionFactory(object):
    @staticmethod
    def get_connection():
        return pymysql.connect(host="localhost",
                               user="root",
                               password="",
                               db="python_design_patterns")


if __name__ == '__main__':
    # Open database connection
    db = ConnectionFactory.get_connection()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print(f"Database version : {data[0]}")

    # disconnect from server
    db.close()
