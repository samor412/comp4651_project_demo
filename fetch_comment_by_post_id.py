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
# python insertRow.py [first_n_post (1-*)] [num_of_post]

def _fetch_latest_comment(cursor, post_id, first_n_comment, num_of_comments):
    sql_select_query = """select c.id, c.created_at, c.created_by, c.post_id, c.content, c.upvote, u.username  from comment c, _user u where c.post_id = %s and u.id = c.created_by order by c.created_at DESC OFFSET %s LIMIT %s """
    cursor.execute(sql_select_query, (post_id, str(int(first_n_comment) - 1), num_of_comments))
    records = cursor.fetchall()

    serialized_comments = []
    for comment in records:
        serialized_comments.append({
            'id': comment[0],
            'created_at': comment[1],
            'created_by': comment[2],
            'post_id': comment[3],
            'content': comment[4],
            'upvote': comment[5],
            'username': comment[6],
        })
    return serialized_comments


# Program Start
def fetch_latest_comment(post_id, first_n_comment, num_of_comments):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()

        comments = _fetch_latest_comment(cursor, post_id, first_n_comment, num_of_comments)
        print("Latest " + first_n_comment + " to " + str(int(first_n_comment) + int(num_of_comments)) + " Comment from Post " + post_id + "  has been fetched")
        return json.dumps({
            'response': 'success',
            'comments': comments,
            'post_id': post_id,
        })

    except (Exception, psycopg2.Error) as error :
        print(error)
        return errorMsg("Internal Error")
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

