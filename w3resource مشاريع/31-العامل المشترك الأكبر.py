import math
while True:
    #برنامج العامل المشترك الأكبر
    n1= int(input("أدخل الرقم الأول"))
    n2=int(input("أدخل الرقم الثاني"))

    gcd = math.gcd(n1,n2)

    print("العامل المشترك الأكبر", gcd)
    print("--"*10)
