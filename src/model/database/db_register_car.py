import psycopg2
import uuid
from psycopg2 import OperationalError, InterfaceError, DatabaseError

def database_create(plate,custumer_name):
   
    from src.model.database.json_db import json_db_read
    from ..time import time_now

    try:
        
        db_login = json_db_read()
    
        conn = psycopg2.connect(
            host=db_login[0],
            database=db_login[1],
            user=db_login[2],
            password=db_login[3]
        )
        times = time_now()

        entry_time = times[1]
        entry_date = times[0]
        
        cur = conn.cursor()
        id = uuid.uuid4
        # Insert some data into an existing table
        cur.execute(f"INSERT INTO parkslot_now (id, plate, custumer_name, entry_time, entry_date) VALUES ('{id}' '{plate}', '{custumer_name}', '{entry_time}', '{entry_date}' )")

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        return True, None

    except (OperationalError, InterfaceError, DatabaseError) as e:

        if "duplicar" in str(e):
            return False, "Plate already registered"
          
        return False, "Conection Error"
