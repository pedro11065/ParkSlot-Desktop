import psycopg2

def db_list_cars():

    from src.model.database.json_db import json_db_read
    
    try:
        db_login = json_db_read()

        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[1],
            user=db_login[2],
            password=db_login[3]
        )
        cur = conn.cursor()

        cur.execute("SELECT * FROM parkslot_now")

        db_data = cur.fetchall()

        cur.close()
        conn.close()
    except:
        return False
    return True, db_data