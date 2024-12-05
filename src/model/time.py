import time 

def time_now():
    data_month = time.strftime("%d/%m/%y")
    data_hour = time.strftime("%H:%M")

    return data_month, data_hour