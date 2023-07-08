
#57-برنامج لحساب الوتر

def hypoten_calcuator(a,b):
    hypo=float(((a**2)+(b**2))**(1/2))
    return hypo

while True:
    print("برنامج لحساب الوتر")
    a=float(input("أدخل رقم الضلع الأول"))
    b=float(input("أدخل رقم الضلع الثاني"))
    print(hypoten_calcuator(a,b))
