'''برنامج يطلب منكم مقارنة المدخلة ببعضها ؛ وإذا اختلفت قيمة فإنه يظهر رسالة خطأ'''


def multi_compare(*vars):
    for i in vars:
        if i !=vars[0]:
            return "ليسوا نفس القيمة"
    return "الأرقام المدخلة متساوين"

print(multi_compare(4,5,4,3,3))
print(multi_compare(4,4,4,4,4))
print(multi_compare(4,5,4,10,10))
