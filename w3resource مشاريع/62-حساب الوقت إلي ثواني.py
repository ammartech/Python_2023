
def to_seconds (years,months,weeks,days,hour, minutes, seconds):
    to_seconds= ((years*12*4*7*3600*24)+(months*4*7*3600*24)+(weeks*7*24*3600)+(days*24*3600)+(hour*3600)+(minutes*60)+seconds)
    return to_seconds
while True:
    years=float(input("عدد السنوات"))
    months=float(input("عدد الأشهر"))
    weeks=float(input("عدد الأسابيع"))
    days=float(input("عدد الأيام"))
    hour= float(input("عدد الساعات"))
    minutes=float(input("عدد الدقائق"))
    seconds=float(input("عدد الثواني"))
    print("عدد الثواني الكلية", to_seconds (years,months,weeks,days,hour, minutes, seconds))
                 
