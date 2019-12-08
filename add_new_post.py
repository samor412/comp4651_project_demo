import psycopg2
import sys
from datetime import datetime, timedelta
from config import user, password, host, port, database
import hashlib
import binascii
import os
import json
from errorMsg import errorMsg

# format:
# python insertRow.py [user_id] [title] [content]

def _add_new_post(connection, cursor, create_at, created_by, title, content):
    postgres_insert_query = """ 
        INSERT INTO post (created_at, created_by, title, content) 
            VALUES (%s,%s,%s,%s) RETURNING id"""

    record_to_insert = (create_at, created_by, title, content)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    post_id = cursor.fetchone()[0]

    return post_id


# Program Start
def add_new_post(user_id, title, content):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()

        post_id = _add_new_post(connection, cursor, datetime.today().strftime("%Y-%m-%d %H:%M:%S"), user_id, title, content)
        print("Post " + title + "  has been created")

        return json.dumps({
            'response': 'success',
            'post_id': post_id,
            'user_id': user_id,
            'title': title,
            'content': content,
        })

    except (Exception, psycopg2.Error) as error :
        print ("Internal Error")
        print(error)
        return errorMsg("Internal Error")
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

