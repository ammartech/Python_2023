numbers = input("أدخل القيم المطلوب إدخالها")
number_list = [str(num) for num in numbers.split(",")]
number_tuple = tuple(number_list)
print("List :", number_list)
print("Tuple :",number_tuple)
