while True:
    list_test =[1,5,8,3]

    int_input= int(input("أدخل الرقم المطلوب إختباره"))
    try:
        if int_input in list_test:
            print ("صحيح" , "-->" , list_test)
        else:
            print("غير موجود","-->", list_test)
    except ValueError:
        print("قيمة غير صحيحة")
