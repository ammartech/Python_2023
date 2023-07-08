def convert_to_int_float(str_number):
    converted_list=[]
    for item in str_number:
        try:
            number =float(item)
            if number.is_integer():
                converted_list.append(int(number))
            else:
                converted_list.append(number)
        except ValueError:
            converted_list.append(None)
    return converted_list

test_list=["77", "98.9", "98.8789", "pi", "invalid", "pu"]
final =convert_to_int_float(test_list)
for n, item in zip (test_list,final):
    if final is not None:
        print(f"{n} لـ {item}")
    else:
        print(f"{n} غير ممكن")


