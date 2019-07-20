import psycopg2
with psycopg2.connect(dbname = 'obdb', user = 'postgres', password = 'qazwsxedc', host = '192.168.0.110') as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM quests")
        print(cursor.fetchall())