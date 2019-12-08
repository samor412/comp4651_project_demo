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

def _fetch_latest_post(cursor, first_n_post, num_of_posts):
    sql_select_query = """select * from post order by created_at DESC OFFSET %s LIMIT %s """
    cursor.execute(sql_select_query, (str(int(first_n_post) - 1), num_of_posts))
    record = cursor.fetchall()

    return record


# Program Start
def fetch_latest_post(first_n_post, num_of_posts):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()

        posts = _fetch_latest_post(cursor, first_n_post, num_of_posts)
        serialized_posts = []
        for post in posts:
            serialized_posts.append({
                'id': post[0],
                'created_at': post[1],
                'created_by': post[2],
                'title': post[3],
                'content': post[4],
                'upvote': post[5],
            })
        print("Latest Post from " + first_n_post + " to " + str(int(first_n_post) + int(num_of_posts)) + "  has been fetched")
        return json.dumps({
            'response': 'success',
            'posts': serialized_posts,
        })

    except (Exception, psycopg2.Error) as error :
        print(error)
        print ("Internal Error")
        return errorMsg("Internal Error")
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

