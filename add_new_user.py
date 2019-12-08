import psycopg2
import sys
from datetime import datetime, timedelta
from config import user, password, host, port, database
import hashlib
import binascii
import os
import secrets
import json
from errorMsg import errorMsg


# format:
# python insertRow.py [username] [password] [first_name] [last_name]

class Error(Exception):
   """Base class for other exceptions"""
   pass

class UserExist(Error):
   """User already exists"""
   pass


def is_account_exist(cursor, username):
    sql_select_query = """select * from _user where username = %s"""
    cursor.execute(sql_select_query, (username,))
    record = cursor.fetchone()

    print(record)
    if record == None:
        return False
    return True

def hashPassword(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii') # Remember this

    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    key = binascii.hexlify(key)
    return key.decode('ascii'), salt.decode('ascii')

def _add_new_user(connection, cursor, create_at, username, password, password_salt, first_name, last_name):
    postgres_insert_query = """ 
        INSERT INTO _user (create_at, username, password, password_salt, first_name, last_name) 
            VALUES (%s,%s,%s,%s,%s,%s)"""

    record_to_insert = (create_at, username, password, password_salt, first_name, last_name)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

    access_token = secrets.token_hex(20)
    sql_select_query = """update _user set access_token = %s where username = %s RETURNING id"""
    cursor.execute(sql_select_query, (access_token, username))
    connection.commit()
    user_id = cursor.fetchone()[0]

    return user_id, access_token



# Program Start
def add_new_user(username, password1, first_name, last_name):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()
        print(is_account_exist(cursor, username))
        if is_account_exist(cursor, username):
            raise UserExist
        else:
            key, salt = hashPassword(password1)
            user_id, access_token = _add_new_user(connection, cursor, datetime.today().strftime("%Y-%m-%d %H:%M:%S"), username, key, salt, first_name, last_name)
            print(username + " account has been created")
            return json.dumps({
                'response': 'success',
                'user_id': user_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'access_token': access_token
            })

    except UserExist as error:
        print ("User already exists")
        return errorMsg("User already exists")
    except (Exception, psycopg2.Error) as error :
        print ("Internal Error", error)
        return errorMsg("Internal Error", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

