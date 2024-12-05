from datetime import datetime

def total_to_pay(entry_time,entry_data,first_hour_price,next_hours_price,day_price):

    entry_datetime_str = f"{entry_data} {entry_time}"
    
    try:
        entry_datetime = datetime.strptime(entry_datetime_str, "%d/%m/%y %H:%M")
    except ValueError as e:
        print(f"Error parsing date/time: {e}")
        return None
    
    now_datetime = datetime.now()
    
    time_difference = now_datetime - entry_datetime
    
    time_difference_hours = time_difference.total_seconds() / 3600
    time_difference_hours = round(time_difference_hours, 2)


    if time_difference_hours <= 1:
        to_pay = first_hour_price
        return round(to_pay,2)
    
    if time_difference_hours > 1 and time_difference_hours < 24:
        to_pay = first_hour_price + (next_hours_price * (time_difference_hours - 1))
        return round(to_pay,2)
    
    if time_difference_hours >= 24:
        pay_24 = day_price * (round(time_difference_hours/24))
        pay_rest_24 = time_difference_hours % 24
        pay_rest_24 = pay_rest_24 * next_hours_price

        to_pay = pay_24 + pay_rest_24
        return round(to_pay,2)
