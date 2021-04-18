#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    ce=cp=co=0
    #min=len(patient_medical_speciality_list)
    for x in patient_medical_speciality_list:
        if 'P'==x:
            cp=cp+1
        elif 'E'==x:
            ce+=1
        elif 'O'==x:
            co+=1
    if cp>ce and cp>co:
        speciality='P'
    elif cp<ce and ce>co:
        speciality='E'
    else:
        speciality='O'
    return medical_speciality[speciality]

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)