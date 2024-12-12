from flask import Blueprint, request, jsonify
from src.model.exit.verification_exit import v_exit
from src.model.database.db_delete_car import db_delete

def exit(data):

    data_v_exit = [data['plate'], 
    data['custumer_name'], 
    data['first_hour'], 
    data['next_hours'],
    data['day']]
    
    plate = data_v_exit[0]
    custumer_name = data_v_exit[1]
    first_hour = data_v_exit[2]
    next_hours = data_v_exit[3]
    day = data_v_exit[4]
    
    exit, to_pay, entry_time, entry_date, error = v_exit(plate,custumer_name,first_hour,next_hours,day) #Verificate if exit request  is valid or not, return if it is or not, how much the custumer will pay, errors and when they entered

#--------------------------------------------------------------------RETURN
    
    if exit == True: 
        
        if db_delete(plate, custumer_name, entry_time, entry_date, to_pay): #will delete the car from table "parkslot_now" and put in with more informations in "parkslot_historic"

            return jsonify({"Exit": True,
                            "placa": True, 
                            "Value": to_pay, 
                            "Server": True, 
                            "Error": error}), 200
        
        return jsonify({"Exit": False , #if plate is valid but some error ocurred when the new files were being write in "parkslot_historic"
                        "placa": True,
                        "Value": "---",
                        "Server": False, 
                        "Error": error}), 502
    
    return jsonify({"Exit": False , #Plate invalid
                    "placa": False, 
                    "Server": False, 
                    "Error": "Car isen't registered"}), 502
