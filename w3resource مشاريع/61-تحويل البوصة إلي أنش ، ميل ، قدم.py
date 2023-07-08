"""حساب المسافة من القدم إلي بوصة أو يارد أو ميل"""

def convert_in_yd_miles (distance,entry):
    if entry =='ب':
        distance*= 12
        return distance
    elif entry =='ي':
        distance*=(1/3)
        return distance
    elif entry=='م':
        distance*=(1/5280)
        return distance
    else:
        return None

while True:
    print("مرحبا بكم")
    distance=float(input("أدخل القيمة"))
    entry=input("ما هي التحويل المطلوب ميل (م) أم يارد (ي) أم قدم (ق)")
    print(convert_in_yd_miles (distance,entry))
