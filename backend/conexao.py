import psycopg2
from django.conf import settings

class Conexao:
    def __init__(self):
        pass
    
    def get_connection():
        db_config = settings.DATABASES['default']
        conn = psycopg2.connect(
            dbname=db_config['NAME'],
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            host=db_config['HOST'],
            port=db_config['PORT']
        )
        return conn
