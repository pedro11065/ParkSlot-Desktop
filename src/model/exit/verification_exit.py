
from src.model.database.db_search_car import db_search
from src.model.exit.calculate_exit import total_to_pay

def verify_values(first_hour,next_hours,day):

    if first_hour.isnumeric(): 
        first_hour = int(first_hour)
        if first_hour >= 0:
        
            if next_hours.isnumeric():
                next_hours = int(next_hours)
                if next_hours >= 0:

                    if day.isnumeric():
                        day = int(day)
                        if day >= 0:
                            return True, None

                        return False,"Invalid day value"
                    return False,"Invalid day value"
                
                return False,"Invalid next hours value"
            return False,"Invalid next hours value"
        
        return False,"Invalid first hour value"
    return False,"Invalid first hour value"
            

def calculate_to_pay(plate, custumer_name, first_hour, next_hours, day):

        search_data = plate
        car, db_data = db_search(search_data)

        if car == False:
            return False, None, None, None, db_data
        
        entry_time = db_data.get('entry_time')
        entry_date = db_data.get('entry_data')
        first_hour_price = int(first_hour)
        next_hours_price = int(next_hours)
        day_price = int(day)


        to_pay = total_to_pay(entry_time,entry_date,first_hour_price,next_hours_price,day_price)

    
        return True, to_pay, entry_time, entry_date, None
       

def v_exit(plate,custumer_name,first_hour,next_hours,day):

    values, error  = verify_values(first_hour,next_hours,day)

    if values:    
        exit, to_pay, entry_time, entry_date, error = calculate_to_pay(plate, custumer_name, first_hour, next_hours, day)
        return exit, to_pay, entry_time, entry_date, error

    return values, None, None, None, error 