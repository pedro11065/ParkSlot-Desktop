import psycopg2
from psycopg2 import OperationalError, InterfaceError, DatabaseError


def db_search(search_data):

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

        plate = search_data

        cur.execute(f"SELECT * FROM parkslot_now WHERE plate = '{plate}';")

        db_data = cur.fetchall()

        cur.close()
        conn.close()

        return True, {"car_id":db_data[0][0], 
                "plate" : db_data[0][1],       
                "entry_time" : db_data[0][3], 
                "entry_data" : db_data[0][4],
                "custumer_name" : db_data[0][2]}
    
    except:
        return False, "Car isen't isen't registered"    

#except (OperationalError, InterfaceError, DatabaseError) as e: