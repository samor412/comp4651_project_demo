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
# python insertRow.py [user_id] [post_id] [content]

class Error(Exception):
   """Base class for other exceptions"""
   pass

class PostNotExist(Error):
   """Post Not Exist"""
   pass

def _is_post_exist(cursor, post_id):
    sql_select_query = """select * from post where id = %s"""
    cursor.execute(sql_select_query, (post_id,))
    record = cursor.fetchone()

    if record == None:
        return False
    return True

def _add_new_comment(connection, cursor, created_at, created_by, post_id, content):
    postgres_insert_query = """ 
        INSERT INTO comment (created_at, created_by, post_id, content) 
            VALUES (%s,%s,%s,%s) RETURNING id"""

    record_to_insert = (created_at, created_by, post_id, content)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    comment_id = cursor.fetchone()[0]
    return comment_id



# Program Start
def add_new_comment(user_id, post_id, content):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()
        if not _is_post_exist(cursor, post_id):
            raise PostNotExist
        comment_id = _add_new_comment(connection, cursor, datetime.today().strftime("%Y-%m-%d %H:%M:%S"), user_id, post_id, content)
        print("Comment on Post " + post_id + "  has been created")
        return json.dumps({
            'response': 'success',
            'user_id': user_id,
            'comment_id': comment_id,
            'post_id': post_id,
            'content': content,
        })

    except PostNotExist as error:
        return errorMsg("Post is not exist")
    except (Exception, psycopg2.Error) as error :
        print(error)
        return errorMsg("Internal Error")
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

