import psycopg2
from datetime import datetime, timedelta
from config import user, password, host, port, database
try:
    connection = psycopg2.connect(user = user,
                                  password = password,
                                  host = host,
                                  port = port,
                                  database = database)
    cursor = connection.cursor()
    print("You are connected" + "\n")

    cursor.execute(open("./sql/createTable.sql", "r").read())
    connection.commit()
    print("_user, post, comment table created")


except (Exception, psycopg2.Error) as error :
    print ("Internal Error")
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
