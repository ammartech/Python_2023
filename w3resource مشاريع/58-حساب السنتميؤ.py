def inch_and_feet_to_cm (feet, inches):
    total_in =feet*12 + inches
    total_cm = total_in *2.54
    return total_cm

feet=int(input("أدخل قيمة الإرتفاع بالقدم"))
inches=int(input("أدخل قيمة الإرتفاع بالأنش"))

print("المسافة بالسنتيمتر", inch_and_feet_to_cm(feet,inches))
