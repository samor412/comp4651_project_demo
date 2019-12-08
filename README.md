Installation
------------
1. install postgres
2. pg_ctl -D /usr/local/var/postgres start
3. createdb comp4651_project
4. psql -l (to list database)

Before Running
-------------------
1. create database named "comp4651_project"
2. change the config.py to set your database authentication information (e.g. user and password of the database)
3. run python createTable.py

Running the backend
--------------------
1. run the below code to host the backend api in localhost:5000
-> python app.py

2. Take reference on ./sample.js to see how to call backend api in frontend(using JS)

Explanation
--------------------

1. The backend server is hosted by python with python package Flask
![Image of app-py.png](/screenshot/app-py.png)

2. The python files use psycopg2 library to communicate to the database with sql query 
![Image of psycopg2](/screenshot/psycopg2.png)

3. The file sample.js is created to demonstrated to show how to use javascript to communicate to the backend.
![Image of sample-js.png](/screenshot/sample-js.png)

4. The database is hosted in AWS RDS. 
![Image of ams-rds.png](/screenshot/ams-rds.png)

5. The Dockerfile for the backend server.
![Image of DockerFile.png](/screenshot/DockerFile.png)





Reference:
---------------------
1. Return attr after sql
https://stackoverflow.com/questions/5247685/python-postgres-psycopg2-getting-id-of-row-just-inserted

2. JS fetch with request body
https://humanwhocodes.com/snippets/2019/01/nodejs-medium-api-fetch/

3. Use Flusk to host the python backend server
https://stackoverflow.com/questions/32288722/call-python-function-from-js
https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request

4. Python Json Dump 
https://www.w3schools.com/python/python_json.asp

5. Python psycopg2
https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/

6. Hash Password in Python
https://www.vitoshacademy.com/hashing-passwords-in-python/
https://www.vitoshacademy.com/hashing-passwords-in-python/

7. Access_token
https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python
https://stackoverflow.com/questions/244882/what-is-the-best-way-to-implement-remember-me-for-a-website


Run DockerFile:
----------------------
1. Go to the root directory of the folder

2. Build Image
docker build -t comp4651_project .

3. run the container (expose to port 5000)
docker run -p 5000:5000 comp4651_project

