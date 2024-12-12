from flask import Blueprint, request, jsonify
from src.model.entry.verification_entry import v_entry
from src.model.database.db_register_car import database_create

def entry(data):


    data = [data['plate'], data['custumer_name']]
    plate = data[0]
    custumer_name = data[1]

    data_v_entry = v_entry(plate) #Verificate if plate is true or not.

#--------------------------------------------------------------------RETURN

    if data_v_entry == True:

        entry, error = database_create(plate,custumer_name) #register the car in the database

        if entry:

            return jsonify({"plate": True,
                            "Server": True, 
                            "Error": error}), 200 #if all good, API return code 200 and a .json msg
        
        return jsonify({"plate": True,
                        "Server": False, 
                        "Error": error}), 502 #if not, will tell by .json why went wrong
    
    else:
        
        return jsonify({"plate": False, 
                        "Server": False, 
                        "Error": "Plate isen't in database" }), 400 #if plate insen't valid, will return 400

