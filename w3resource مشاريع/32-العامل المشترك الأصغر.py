import math
while True:
    #برنامج العامل المشترك الأكبر
    n1= int(input("أدخل الرقم الأول"))
    n2=int(input("أدخل الرقم الثاني"))

    lcm = math.lcm(n1,n2)

    print("العامل المشترك الاصغر", lcm)
    print("--"*10)
