import psycopg2
from django.conf import settings

class Conexao:
    def __init__(self):
        pass
    
    def get_connection():
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='hyIee08`9?5j',
            host='poo-db.c3k0q4komhkp.us-east-1.rds.amazonaws.com',
            port=5432
        )
        return conn
