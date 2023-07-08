
def Kpa_to_others (Kpa):
    psi=Kpa*0.145
    mmHg=Kpa*7.501
    atm=Kpa*0.00987
    return psi , mmHg , atm

while True:
    Kpa= float(input("أدخل القيمة بوحدات الكيلوباسكال"))
    print("القيم هي:",Kpa_to_others (Kpa))


    
