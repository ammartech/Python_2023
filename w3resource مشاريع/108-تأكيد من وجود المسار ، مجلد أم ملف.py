import os

while True:
    print("***"*20)
    Enter = input(":أدخل المسار")
    print(os.path.lexists(Enter))
    print(os.path.islink(Enter))
    print(os.path.exists(Enter))
    if os.path.isfile(Enter):
        print("المسار عبارة عن ملف")
        print(os.path.abspath(Enter)," : المسار")
    elif os.path.isdir(Enter):
        print("المسار عبارة عن مجلد")
        print(os.path.abspath(Enter),"المسار")
    else:
        print("المسار غير موجود أصلا")

