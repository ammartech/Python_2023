def bmi_calculation(w,h):
    bmi= w/(h**2)
    return bmi


while True:
    w=float(input("الوزن"))
    h=float(input("الطول"))
    print("Bmi",bmi_calculation(w,h))

