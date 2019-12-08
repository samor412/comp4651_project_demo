import psycopg2
from psycopg2 import sql
import sys
from datetime import datetime, timedelta
from config import user, password, host, port, database
import hashlib
import binascii
import os
import json
from errorMsg import errorMsg

# format:
# python insertRow.py ['post' || 'comment'] [post_comment_id]

def _update_vote(connection, cursor, postOrComment, post_comment_id):
    postgres_insert_query = sql.SQL("""
        Update {} set upvote = upvote + 1 where id = %s RETURNING upvote
        """
    ).format(sql.Identifier("post" if postOrComment == 'post' else 'comment'))

    record_to_insert = (post_comment_id,)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    upvote = cursor.fetchone()[0]

    return upvote


# Program Start
def update_vote_post(post_id):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()

        upvote = _update_vote(connection, cursor, 'post', post_id)
        print("Upvote on Post " + post_id + "  has been created")
        return json.dumps({
            'response': 'success',
            'post_id': post_id,
            'upvote': upvote,
        })

    except (Exception, psycopg2.Error) as error :
        print ("Internal Error", error)
        errorMsg("Internal Error", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def update_vote_comment(comment_id):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()

        upvote = _update_vote(connection, cursor, 'comment', comment_id)
        print("Upvote on Comment" + comment_id + "  has been created")
        return json.dumps({
            'response': 'success',
            'comment_id': comment_id,
            'upvote': upvote,
        })

    except (Exception, psycopg2.Error) as error :
        print ("Internal Error")
        print(error)
        errorMsg("Internal Error")
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

