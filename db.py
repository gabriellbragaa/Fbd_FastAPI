import psycopg2

def get_db_connection():
    return psycopg2.connect(
            dbname='empresa',    
            user='postgres',
            password='12345678',
            host='localhost',
            port='5432'
        )
        