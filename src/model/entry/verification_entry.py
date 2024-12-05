
def v_entry(plate):

    def verification_plate(plate):

        contLetter = 0
        contNum = 0

        if len(plate) == 7:   
            for i, item in enumerate(plate):

                if item.isalpha() and (i == 0 or i == 1 or i == 2 or i ==4):
                    contLetter += 1

                elif item.isdigit() and (i == 3 or i == 4 or i == 5 or i == 6):                      
                    contNum += 1
                        
            if (contLetter == 3 and contNum == 4) or (contLetter == 4 and contNum == 3):    
                plate_true = 1
                    
                if plate_true == 1:  

                    return True
                
        return False
    
    if verification_plate(plate):
        return True
    return False 