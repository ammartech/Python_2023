while True:
    string_input = str(input(""))

    if string_input[:2] =="Is":
        print (string_input)
    else:
        new_string="Is" + string_input
        print(new_string)
