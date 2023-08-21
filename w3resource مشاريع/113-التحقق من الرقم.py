import sys
#113
n_input=input("إضافة الرقم")

if n_input.isdigit():
    print("قد تم إضافة الرقم")
else:
    print("خطأ ؛ لم يتم إدخال رقم", file=sys.stderr)
    
