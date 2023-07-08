''' 97- الكلمات المفتاحية في اللغة  ، ملوحظة : الموقع أخطا في التعبير في هذا السؤال فقد طلب المتغيرات المهمة ؛ ولكن الحل
علي أنها الكلمات المفتاحية لذا وجب التنبيه'''
import builtins

special_variables = [var for var in dir(builtins) if var.startswith('__') and var.endswith('__')]
for var in special_variables:
    print(var)
print("---"*44)

import keyword

keywords = keyword.kwlist
for kw in keywords:
    print(kw)
