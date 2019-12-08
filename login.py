import psycopg2
import sys
from datetime import datetime, timedelta
from config import user, password, host, port, database
import hashlib
import binascii
import os
import secrets
from errorMsg import errorMsg
import json

# format:
# python login.py [username] [password]

class Error(Exception):
   """Base class for other exceptions"""
   pass

class InvalidAuthError(Error):
   """Incorrect Password or Username"""
   pass

class InvalidAccessCode(Error):
   """Incorrect Access Code"""
   pass


def is_account_exist(cursor, username):
    sql_select_query = """select * from _user where username = %s"""
    cursor.execute(sql_select_query, (username,))
    record = cursor.fetchone()

    if record == None:
        return False
    return True

def get_salt(cursor, username):
    sql_select_query = """select password_salt from _user where username = %s"""
    cursor.execute(sql_select_query, (username,))
    salt = cursor.fetchone()
    return salt[0]

def hashPasswordWithSalt(password, salt):
    salt = salt.encode('ascii') # Remember this
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    key = binascii.hexlify(key)
    return key.decode('ascii')

def _login(connection, cursor, username, password):
    salt = get_salt(cursor, username)
    hashed_password = hashPasswordWithSalt(password, salt)
    sql_select_query = """select * from _user where username = %s and password = %s"""
    cursor.execute(sql_select_query, (username, hashed_password))
    record = cursor.fetchone()

    if record == None:
        raise InvalidAuthError
    else:
        access_token = secrets.token_hex(20)
        sql_select_query = """update _user set access_token = %s where username = %s RETURNING id, first_name, last_name"""
        cursor.execute(sql_select_query, (access_token, username))
        record = cursor.fetchone()
        connection.commit()
        user_id, first_name, last_name = record[0], record[1], record[2]

        return user_id, first_name, last_name, access_token

def _login_with_access_token(cursor, user_id, access_token):
    sql_select_query = """select * from _user where id = %s and access_token = %s"""
    cursor.execute(sql_select_query, (user_id, access_token))
    record = cursor.fetchone()
    print(record)
    if record != None:
        return {
            'user_id': record[0],
            'username': record[2],
            'first_name': record[5],
            'last_name': record[6], 
            'access_token': record[7], 
        }
    else:
        return False


# Program Start

def login(username, password1):
    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()
        if not is_account_exist(cursor, username):
            raise InvalidAuthError

        user_id, first_name, last_name, access_token = _login(connection, cursor, username, password1)
        print("User "+ username + " has logged in, access_token " + access_token + " is generated for cookie")
        return json.dumps({
                'response': 'success',
                'user_id': user_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'access_token': access_token
            })

    except InvalidAuthError as error:
        print ("Incorrect Password or Username")
        return errorMsg("Incorrect Password or Username")
    except (Exception, psycopg2.Error) as error :
        print ("Internal Error")
        return errorMsg("Internal Error")

    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def login_with_access_token(user_id, access_token):

    try:
        connection = psycopg2.connect(user = user,
                                    password = password,
                                    host = host,
                                    port = port,
                                    database = database)
        cursor = connection.cursor()

        record = _login_with_access_token(cursor, user_id, access_token)
        print("User "+ user_id + " has logged in with access_token " + access_token)
        if record:
            print(record.get('user_id'))
            return json.dumps({
                'response': 'success',
                'user_id': record.get('user_id'),
                'username': record.get('username'),
                'first_name': record.get('first_name'),
                'last_name': record.get('last_name'),
                'access_token': record.get('access_token')
            })
        else:
            raise InvalidAccessCode

    except InvalidAccessCode as error:
        print ("Invalid Access Code")
        return errorMsg("Invalid Access Code")
    except InvalidAuthError as error:
        print ("Incorrect Password or Username")
        return errorMsg("Incorrect Password or Username")
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

