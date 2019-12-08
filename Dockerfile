FROM python:3

COPY * /backend/

RUN pip install psycopg2 flask
RUN chmod +x /backend/*.py

CMD [ "python", "/backend/app.py" ]

EXPOSE 5000